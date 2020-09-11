# Creating a Cluster<a name="css_01_0011"></a>

To use CSS, create a cluster first.

## Procedure<a name="section781857123412"></a>

1.  Log in to the CSS management console.
2.  On the  **Dashboard**  or  **Clusters**  page, click  **Create Cluster**  to switch to the  **Create Cluster**  page.
3.  Specify  **Region**  and  **AZ**.

    **Region**: Select the region for the cluster from drop-down menu to the right of  **Region**. Currently, only region eu-de is supported.

    **AZ**: An AZ contains one or multiple physical data centers. Each AZ has independent cooling, fire extinguishing, moisture-proof, and electricity facilities. Within an AZ, computing, network, storage, and other resources are logically divided into multiple clusters. AZs within a region are interconnected using high-speed optical fibers to allow users to build cross-AZ high-availability systems. Select the AZ associated with the cluster's region.

4.  Set basic information about the cluster. Specifically, specify  **Version**  and  **Name**.

    -   **Version**: Version 6.2.3 is supported.
    -   **Name**: Enter a cluster name containing 4 to 32 characters. Only letters, digits, hyphens \(-\), and underscores \(\_\) are allowed. The value must start with a letter.

    **Figure  1**  Configuring basic information<a name="fig1850961952412"></a>  
    ![](figures/configuring-basic-information.png "configuring-basic-information")

5.  Set host specifications of the cluster.

    **Table  1**  Parameter description

    <a name="table950951922414"></a>
    <table><thead align="left"><tr id="row14509181918241"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p150917199243"><a name="p150917199243"></a><a name="p150917199243"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p1350941916247"><a name="p1350941916247"></a><a name="p1350941916247"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15509111982410"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1350910198248"><a name="p1350910198248"></a><a name="p1350910198248"></a><span class="parmname" id="parmname141962575562"><a name="parmname141962575562"></a><a name="parmname141962575562"></a><b>Nodes</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p2050931982412"><a name="p2050931982412"></a><a name="p2050931982412"></a>Number of nodes in a cluster.</p>
    </td>
    </tr>
    <tr id="row65090196243"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1250951902416"><a name="p1250951902416"></a><a name="p1250951902416"></a><span class="parmname" id="parmname645391945713"><a name="parmname645391945713"></a><a name="parmname645391945713"></a><b>Node Specifications</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p1550931910245"><a name="p1550931910245"></a><a name="p1550931910245"></a>Flavor of nodes in a cluster. Currently, the following specifications are supported: <strong id="b185681557231"><a name="b185681557231"></a><a name="b185681557231"></a>css.medium.8</strong>, <strong id="b109714214242"><a name="b109714214242"></a><a name="b109714214242"></a>css.large.8</strong>, <strong id="b1318376152419"><a name="b1318376152419"></a><a name="b1318376152419"></a>css.xlarge.8</strong>, <strong id="b1084719942417"><a name="b1084719942417"></a><a name="b1084719942417"></a>css.2xlarge.8</strong>, and <strong id="b1984911128247"><a name="b1984911128247"></a><a name="b1984911128247"></a>css.4xlarge.8</strong>.</p>
    <p id="p1550911912412"><a name="p1550911912412"></a><a name="p1550911912412"></a>After you select a node specification, the CPU and memory corresponding to the current specification are displayed below the parameter. For example, if you select <strong id="b685720320818"><a name="b685720320818"></a><a name="b685720320818"></a>css.medium.8</strong>, then <strong id="b38701031782"><a name="b38701031782"></a><a name="b38701031782"></a>1 vCPUs | 8 GB</strong> will be displayed in the lower part, indicating that your selected node specification contains one vCPU and 8 GB memory.</p>
    </td>
    </tr>
    <tr id="row175091919122413"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p650921919248"><a name="p650921919248"></a><a name="p650921919248"></a><span class="parmname" id="parmname14282191413313"><a name="parmname14282191413313"></a><a name="parmname14282191413313"></a><b>Node Storage Type</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p650911918249"><a name="p650911918249"></a><a name="p650911918249"></a>In the current version, the following options are available: <strong id="b28211641156"><a name="b28211641156"></a><a name="b28211641156"></a>Common I/O</strong>, <strong id="b13880344954"><a name="b13880344954"></a><a name="b13880344954"></a>High I/O</strong>, and <strong id="b68612481958"><a name="b68612481958"></a><a name="b68612481958"></a>Ultra-high I/O</strong>.</p>
    </td>
    </tr>
    <tr id="row250912197249"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1950921962418"><a name="p1950921962418"></a><a name="p1950921962418"></a><span class="parmname" id="parmname995054917511"><a name="parmname995054917511"></a><a name="parmname995054917511"></a><b>Node Storage Capacity</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p16509181952416"><a name="p16509181952416"></a><a name="p16509181952416"></a>Storage space. Its value is related to node specifications and varies with node specifications.</p>
    <a name="ul189461316669"></a><a name="ul189461316669"></a><ul id="ul189461316669"><li>Value range of flavor <strong id="b1848992610451"><a name="b1848992610451"></a><a name="b1848992610451"></a>css.medium.8</strong>: 40 GB to 640 GB</li><li>Value range of flavor <strong id="b1851033122314"><a name="b1851033122314"></a><a name="b1851033122314"></a>css.large.8</strong>: 40 GB to 1,280 GB</li><li>Value range of flavor <strong id="b91201547112313"><a name="b91201547112313"></a><a name="b91201547112313"></a>css.xlarge.8</strong>: 40 GB to 2,560 GB</li><li>Value range of flavor <strong id="b279692713247"><a name="b279692713247"></a><a name="b279692713247"></a>css.2xlarge.8</strong>: 80 GB to 5,120 GB</li><li>Value range of flavor <strong id="b142962316246"><a name="b142962316246"></a><a name="b142962316246"></a>css.4xlarge.8</strong>: 160 GB to 10,240 GB</li></ul>
    </td>
    </tr>
    <tr id="row6127934194011"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1470610457401"><a name="p1470610457401"></a><a name="p1470610457401"></a><span class="parmname" id="parmname995218114711"><a name="parmname995218114711"></a><a name="parmname995218114711"></a><b>Disk Encryption</b></span></p>
    </td>
    <td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p17127834194017"><a name="p17127834194017"></a><a name="p17127834194017"></a>If you select this option, the nodes you selected for the created cluster use encrypted EVS disks to enhance data security in the cluster. By default, this option is not selected. After the cluster is created, you cannot modify the setting of this option. Therefore, exercise caution when performing the setting.</p>
    <p id="p0239911125713"><a name="p0239911125713"></a><a name="p0239911125713"></a>After you select this option, you need to select an available key from the <strong id="b11607121916479"><a name="b11607121916479"></a><a name="b11607121916479"></a>Key Name</strong> drop-down list box. If no key is available, click <span class="uicontrol" id="uicontrol1932561718598"><a name="uicontrol1932561718598"></a><a name="uicontrol1932561718598"></a><b>Create/View Key</b></span> to go to the KMS management console and create or modify a key. For details, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/kms/en-us_topic_0034330265.html" target="_blank" rel="noopener noreferrer">Creating a CMK</a>.</p>
    <p id="p2062119166388"><a name="p2062119166388"></a><a name="p2062119166388"></a>Enabling disk encryption has no impact on your operations on a cluster (such as accessing the cluster, importing data to the cluster, and much more). However, after you enable disk encryption, operation performance deteriorates by about 10%.</p>
    <div class="note" id="note134725562016"><a name="note134725562016"></a><a name="note134725562016"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul67444552406"></a><a name="ul67444552406"></a><ul id="ul67444552406"><li>If the cluster is in the <span class="parmname" id="parmname849182212433"><a name="parmname849182212433"></a><a name="parmname849182212433"></a><b>Available</b></span> state and the key used for disk encryption is in the <span class="parmname" id="parmname1667300112"><a name="parmname1667300112"></a><a name="parmname1667300112"></a><b>Pending deletion</b></span> or <span class="parmname" id="parmname166616307112"><a name="parmname166616307112"></a><a name="parmname166616307112"></a><b>disable</b></span> state or has been deleted after a cluster is created, cluster capacity expansion is not allowed, while other operations on the cluster, such as restarting the cluster, creating snapshots, restoring the cluster, and importing data to the cluster are not affected. In addition, this key cannot be used for cluster creation in the future.</li><li>After a cluster is created, do not delete the key used by the cluster. Otherwise, the cluster will become unavailable.</li><li>The Default Master Keys cannot be used to create grants. Specifically, you cannot use Default Master Keys whose aliases end with <span class="parmvalue" id="parmvalue12881641114711"><a name="parmvalue12881641114711"></a><a name="parmvalue12881641114711"></a><b>/default</b></span> in KMS to create clusters.</li></ul>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

    **Figure  2**  Configuring host specifications<a name="fig6524919122413"></a>  
    ![](figures/configuring-host-specifications.png "configuring-host-specifications")

6.  Set network specifications of the cluster. Specifically, specify  **VPC**,  **Subnet**, and  **Security Group**.

    -   **VPC**: A VPC is a secure, isolated, logical network environment.

        Select the target VPC. Click  **View VPC**  to enter the VPC management console to view the created VPC names and IDs. If no VPC is available, create a VPC.

        >![](/images/icon-note.gif) **NOTE:**   
        >The selected VPC must contain CIDRs. Otherwise, cluster creation will fail. By default, a created VPC contains CIDRs.  

    -   **Subnet**: A subnet provides dedicated network resources that are isolated from other networks for higher network security.

        Select the target subnet. You can access the VPC management console to view the names and IDs of the existing subnets in the target VPC.

    -   **Security Group**: A security group is a collection of access control rules for ECSs that have the same security protection requirements and are mutually trusted in a VPC. To view more details about the security group, click  **View Security Group**.

        >![](/images/icon-note.gif) **NOTE:**   
        >Ensure that  **Port/Range**  is  **All**  or a port range including port  **9200**  for the selected security group.  

    -   **Communication Encryption**: If you enable the communication encryption function, you will access the cluster using HTTPS to secure your data. After the cluster is created, you cannot modify the setting of this option. Therefore, exercise caution when performing the setting. By default, the communication encryption function is enabled.

        ![](figures/icon-open-dt.png)  indicates to enable the communication encryption function, and  ![](figures/icon-close.png)  indicates to disable the communication encryption function.

        If the communication encryption function is enabled, the CSS server processes the SSL requests from the client and the security certificate of the CSS server has been configured by default. Please be aware that the certificate is shared between all CSS instances.

        Enabling this function in a cluster will affect the procedure of accessing the cluster or importing data to the cluster. For details, see  [Accessing a Cluster](accessing-a-cluster.md),  [Using Logstash to Import Data to Elasticsearch](using-logstash-to-import-data-to-elasticsearch.md), and  [Using Kibana or APIs to Import Data to Elasticsearch](using-kibana-or-apis-to-import-data-to-elasticsearch.md).

    **Figure  3**  Configuring network specifications<a name="fig18345172316477"></a>  
    ![](figures/configuring-network-specifications.png "configuring-network-specifications")

7.  Click  **Next**  to switch to the  **Confirm**  page.
8.  After the specifications are confirmed, click  **Submit**.
9.  Click  **Back to Cluster List**  to switch to the  **Clusters**  page. The cluster you created is listed on the displayed page and its status is  **Creating**. If the cluster is successfully created, its status will change to  **Available**.

    If the cluster fails to be created, create the cluster again as prompted.


