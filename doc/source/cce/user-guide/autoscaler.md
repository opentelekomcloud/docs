# autoscaler<a name="cce_01_0154"></a>

## Introduction<a name="section25311744154917"></a>

The  autoscaler  resizes a cluster based on  pod  scheduling status and resource usage.

CCE simplifies the creation, upgrade, and manual scaling of Kubernetes clusters, in which traffic loads change over time. To balance resource usage and workload performance of nodes, Kubernetes introduces the autoscaler add-on to automatically resize a cluster based on the resource usage required for workloads deployed in the cluster.

The autoscaler is applied in the following two scenarios:

-   Automatic scale-up is triggered if there are pods that failed to be scheduled onto any nodes in a cluster due to insufficient node resources. The add-on follows the "No Less, No More" policy. If three cores are required for creating a pod and there are four-core and eight-core nodes, a four-core node is preferentially created.

    >![](/images/icon-note.gif) **NOTE:**   
    >An auto scale-up will be performed only when either of the following conditions has been met:  
    >-   Node resources are insufficient.  
    >-   No node affinity settings are included in other scheduling configurations. For more information about node affinity configuration, see  [Configuring Affinity and Anti-Affinity Scheduling](configuring_affinity_and_anti_affinity_scheduling).  

-   If a node in a cluster is not fully used for a period of time and the pods on the node can be scheduled to other nodes, a scale-down is automatically performed to remove the node.

## Constraints<a name="section202191122814"></a>

-   Only clusters of v1.9.10-r2 and later support autoscaler.
-   This autoscaler add-on cannot be used with the CPU-usage-based node autoscaler.

## Installing the Add-on<a name="section15573161754711"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Marketplace**  tag page, click  **Install Add-on**  under  **autoscaler**.
2.  On the  **Install Add-on**  page, select the cluster and the add-on version, and click  **Next**.
3.  Configure add-on installation parameters listed in  [Table 1](#table1582194517429).

    **Table  1**  Basic settings

    <a name="table1582194517429"></a>
    <table><thead align="left"><tr id="row178187453428"><th class="cellrowborder" valign="top" width="18.82%" id="mcps1.2.4.1.1"><p id="p14818104534219"><a name="p14818104534219"></a><a name="p14818104534219"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.050000000000004%" id="mcps1.2.4.1.2"><p id="p181814453425"><a name="p181814453425"></a><a name="p181814453425"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.13%" id="mcps1.2.4.1.3"><p id="p102901135192211"><a name="p102901135192211"></a><a name="p102901135192211"></a>Add-on Version</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row178631475226"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.2.4.1.1 "><p id="p386464792210"><a name="p386464792210"></a><a name="p386464792210"></a>Add-on Specifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p1861133733913"><a name="p1861133733913"></a><a name="p1861133733913"></a>Possible values:</p>
    <a name="ul1634319358233"></a><a name="ul1634319358233"></a><ul id="ul1634319358233"><li><strong id="b15151353408"><a name="b15151353408"></a><a name="b15151353408"></a>Single</strong>: The add-on has only one instance.</li><li><strong id="b1756816417401"><a name="b1756816417401"></a><a name="b1756816417401"></a>HA</strong>: The add-on has multiple instances for higher availability. This mode requires more compute resources.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.3 "><p id="p111958230594"><a name="p111958230594"></a><a name="p111958230594"></a>Available in all versions</p>
    </td>
    </tr>
    <tr id="row921611101579"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.2.4.1.1 "><p id="p13217111055715"><a name="p13217111055715"></a><a name="p13217111055715"></a>Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p93701640145120"><a name="p93701640145120"></a><a name="p93701640145120"></a>Number of instances that will be created to match the selected add-on specifications. The number cannot be modified.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.3 "><p id="p2264124945914"><a name="p2264124945914"></a><a name="p2264124945914"></a>Available in all versions</p>
    </td>
    </tr>
    <tr id="row087474432717"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.2.4.1.1 "><p id="p17875104414275"><a name="p17875104414275"></a><a name="p17875104414275"></a>Container</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p1437014065110"><a name="p1437014065110"></a><a name="p1437014065110"></a>CPU and memory quotas of the container allowed for the selected add-on specifications. The quotas cannot be modified.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.3 "><p id="p179441523596"><a name="p179441523596"></a><a name="p179441523596"></a>Available in all versions</p>
    </td>
    </tr>
    <tr id="row142784417388"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.2.4.1.1 "><p id="p11271944133814"><a name="p11271944133814"></a><a name="p11271944133814"></a>Key pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p14156122010527"><a name="p14156122010527"></a><a name="p14156122010527"></a>Key pair for logging in to the node to be added.</p>
    <p id="p82711005516"><a name="p82711005516"></a><a name="p82711005516"></a>Select an existing key pair and use it to log in to the node as the <strong id="b842352706152154"><a name="b842352706152154"></a><a name="b842352706152154"></a>root</strong> user.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.3 "><p id="p235916510391"><a name="p235916510391"></a><a name="p235916510391"></a>Available in all versions</p>
    </td>
    </tr>
    <tr id="row4286336194017"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.2.4.1.1 "><p id="p14286203613402"><a name="p14286203613402"></a><a name="p14286203613402"></a><span class="keyword" id="keyword19846240134014"><a name="keyword19846240134014"></a><a name="keyword19846240134014"></a>Auto Scale-In</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p95247442409"><a name="p95247442409"></a><a name="p95247442409"></a><strong id="b352484410403"><a name="b352484410403"></a><a name="b352484410403"></a>Off</strong>: Auto scale-down is not allowed. Only auto scale-up is allowed.</p>
    <p id="p6524124417400"><a name="p6524124417400"></a><a name="p6524124417400"></a><strong id="b175242044184018"><a name="b175242044184018"></a><a name="b175242044184018"></a>On</strong>: Auto scale-down is allowed for both existing and added nodes.</p>
    <a name="ul152418448406"></a><a name="ul152418448406"></a><ul id="ul152418448406"><li><strong id="b1152474474010"><a name="b1152474474010"></a><a name="b1152474474010"></a>Idle Time (min)</strong>: Time for which a node should be unneeded before it is eligible for scale-down. Default value: 10 minutes.</li><li><strong id="b195241344114013"><a name="b195241344114013"></a><a name="b195241344114013"></a>Resource Usage</strong>: If the percentage of both CPU and memory usage on a node is below this threshold, auto scale-down will be triggered to delete the node from the cluster. The default value is 0.5, which means 50%.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.3 "><p id="p828673613406"><a name="p828673613406"></a><a name="p828673613406"></a>Available in all versions</p>
    </td>
    </tr>
    <tr id="row10588111641417"><td class="cellrowborder" valign="top" width="18.82%" headers="mcps1.2.4.1.1 "><p id="p20580042144816"><a name="p20580042144816"></a><a name="p20580042144816"></a>Node Pool Configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.050000000000004%" headers="mcps1.2.4.1.2 "><p id="p106311133304"><a name="p106311133304"></a><a name="p106311133304"></a>A node pool is a group of compute nodes with the same node type (VM or BMS), specifications, and labels. When the cluster needs to be scaled up, autoscaler will automatically select nodes from these node pools to the cluster. If no custom node pool is available, autoscaler will use the default node pool.</p>
    <p id="p2087715518406"><a name="p2087715518406"></a><a name="p2087715518406"></a>Click <strong id="b16709165713368"><a name="b16709165713368"></a><a name="b16709165713368"></a>Add Node Pool Configuration</strong> and set the following parameters:</p>
    <a name="ul378119275614"></a><a name="ul378119275614"></a><ul id="ul378119275614"><li><strong id="b1869716517332"><a name="b1869716517332"></a><a name="b1869716517332"></a>AZ</strong>: A physical region where resources use independent power supplies and networks. AZs are physically isolated but interconnected through the internal network.</li><li><strong id="b8584599566"><a name="b8584599566"></a><a name="b8584599566"></a>OS</strong>: OS of the nodes to be created.</li><li><strong id="b713584464116"><a name="b713584464116"></a><a name="b713584464116"></a>Taints</strong>: No taints are added by default.<div class="p" id="p7853111720153"><a name="p7853111720153"></a><a name="p7853111720153"></a>Taints allow nodes to repel a set of pods. You can add a maximum of 10 taints for each node pool. Each taint contains the following parameters:<a name="ul17274222121015"></a><a name="ul17274222121015"></a><ul id="ul17274222121015"><li><strong id="b6921811213"><a name="b6921811213"></a><a name="b6921811213"></a>Key</strong>: A key must contain 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed. A DNS subdomain name can be used as the prefix of a key.</li><li><strong id="b17301821282"><a name="b17301821282"></a><a name="b17301821282"></a>Value</strong>: A value must start with a letter or digit and can contain a maximum of 63 characters, including letters, digits, hyphens (-), underscores (_), and periods (.).</li><li><strong id="b838411376810"><a name="b838411376810"></a><a name="b838411376810"></a>Effect</strong>: Available options are <strong id="b10854184131219"><a name="b10854184131219"></a><a name="b10854184131219"></a>NoSchedule</strong>, <strong id="b15432119161211"><a name="b15432119161211"></a><a name="b15432119161211"></a>PreferNoSchedule</strong>, and <strong id="b73476124120"><a name="b73476124120"></a><a name="b73476124120"></a>NoExecute</strong>.</li></ul>
    <div class="notice" id="note77443231113"><a name="note77443231113"></a><a name="note77443231113"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul104271158181515"></a><a name="ul104271158181515"></a><ul id="ul104271158181515"><li>If taints are used, you must configure tolerations in the YAML files of pods. Otherwise, scale-up may fail or pods cannot be scheduled onto the added nodes.</li><li>Taints cannot be modified after configuration. Incorrect taints may cause a scale-up failure or prevent pods from being scheduled onto the added nodes.</li></ul>
    </div></div>
    </div>
    </li><li><strong id="b76081141194516"><a name="b76081141194516"></a><a name="b76081141194516"></a>Resource Tags</strong>: Resource tags can be added to classify resources.<div class="note" id="note1873655813232"><a name="note1873655813232"></a><a name="note1873655813232"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1682495163615"><a name="p1682495163615"></a><a name="p1682495163615"></a>You can create predefined tags in Tag Management Service (TMS). Predefined tags are visible to all service resources that support the tagging function. You can use predefined tags to improve tag creation and migration efficiency.</p>
    </div></div>
    </li><li><strong id="b651061314582"><a name="b651061314582"></a><a name="b651061314582"></a>Specifications</strong>: CPU and memory of the added nodes.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19.13%" headers="mcps1.2.4.1.3 "><p id="p369616371304"><a name="p369616371304"></a><a name="p369616371304"></a>Available only in certain versions</p>
    </td>
    </tr>
    </tbody>
    </table>

    To configure more add-on parameters, click  **Advanced Settings**  at the bottom of this page.

    **Table  2**  Advanced settings

    <a name="table9850103573510"></a>
    <table><thead align="left"><tr id="row4607144693512"><th class="cellrowborder" valign="top" width="18.529999999999998%" id="mcps1.2.4.1.1"><p id="p39151855123517"><a name="p39151855123517"></a><a name="p39151855123517"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.629999999999995%" id="mcps1.2.4.1.2"><p id="p18915195517356"><a name="p18915195517356"></a><a name="p18915195517356"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.84%" id="mcps1.2.4.1.3"><p id="p1412212191402"><a name="p1412212191402"></a><a name="p1412212191402"></a>Add-on Version</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row385043515351"><td class="cellrowborder" valign="top" width="18.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p129911124203017"><a name="p129911124203017"></a><a name="p129911124203017"></a>Total Nodes</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.2 "><p id="p29911924143017"><a name="p29911924143017"></a><a name="p29911924143017"></a>The total number of nodes up to which the cluster can be scaled.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.2.4.1.3 "><p id="p436632542"><a name="p436632542"></a><a name="p436632542"></a>Available in all versions</p>
    </td>
    </tr>
    <tr id="row1785163517352"><td class="cellrowborder" valign="top" width="18.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p09919249305"><a name="p09919249305"></a><a name="p09919249305"></a>Total Cores</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.2 "><p id="p10991724113018"><a name="p10991724113018"></a><a name="p10991724113018"></a>The total number of cores up to which the cluster can be scaled.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.2.4.1.3 "><p id="p16496194815118"><a name="p16496194815118"></a><a name="p16496194815118"></a>Available in all versions</p>
    </td>
    </tr>
    <tr id="row208511335113518"><td class="cellrowborder" valign="top" width="18.529999999999998%" headers="mcps1.2.4.1.1 "><p id="p7991152414302"><a name="p7991152414302"></a><a name="p7991152414302"></a>Total Memory (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.629999999999995%" headers="mcps1.2.4.1.2 "><p id="p199916247301"><a name="p199916247301"></a><a name="p199916247301"></a>The total memory up to which the cluster can be scaled.</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.84%" headers="mcps1.2.4.1.3 "><p id="p5197195215113"><a name="p5197195215113"></a><a name="p5197195215113"></a>Available in all versions</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  When the configuration is complete, click  **Install**.

    After the installation is complete, you can view the add-on instance on the  **Add-on Instance**  tab page. This indicates that the add-on has been installed in the current cluster.


## Uninstalling the Add-on<a name="section610455514114"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Instance**  tab page, select the cluster and click  **Uninstall**  under  **autoscaler**.
2.  In the dialog box that is displayed, click  **Yes**  to uninstall the add-on.

