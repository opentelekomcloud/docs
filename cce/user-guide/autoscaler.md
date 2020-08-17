# autoscaler<a name="cce_01_0154"></a>

## Introduction<a name="section25311744154917"></a>

The autoscaler resizes a cluster based on pod scheduling status and resource usage.

CCE simplifies the creation, upgrade, and manual scaling of Kubernetes clusters, in which traffic loads change over time. To balance resource usage and workload performance of nodes, Kubernetes introduces the autoscaler add-on to automatically resize a cluster based on the resource usage required for workloads deployed in the cluster.

The autoscaler is applied in the following two scenarios:

-   Automatic scale-up is triggered if there are pods that failed to be scheduled onto any nodes in a cluster due to insufficient node resources. The add-on follows the "No Less, No More" policy. If three cores are required for creating a pod and there are four-core and eight-core nodes, a four-core node is preferentially created.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >An auto scale-up will be performed only when either of the following conditions has been met:
    >-   Node resources are insufficient.
    >-   No node affinity settings are included in other scheduling configurations. For more information about node affinity configuration, see  [Configuring Affinity and Anti-Affinity Scheduling](configuring-affinity-and-anti-affinity-scheduling.md).

-   If a node in a cluster is not fully used for a period of time and the pods on the node can be scheduled to other nodes, a scale-down is automatically performed to remove the node.

## Constraints<a name="section202191122814"></a>

-   Only clusters of v1.9.10-r2 and later support autoscaler.
-   This autoscaler add-on cannot be used with the CPU-usage-based node autoscaler.

## Installing the Add-on<a name="section15573161754711"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Marketplace**  tag page, click  **Install Add-on**  under  **autoscaler**.
2.  On the  **Install Add-on**  page, select the cluster and the add-on version, and click  **Next: Configuration**.
3.  Configure add-on installation parameters listed in  [Table 1](#table1582194517429).

    **Table  1**  Basic settings

    <a name="table1582194517429"></a>
    <table><thead align="left"><tr id="row178187453428"><th class="cellrowborder" valign="top" width="21.14%" id="mcps1.2.4.1.1"><p id="p14818104534219"><a name="p14818104534219"></a><a name="p14818104534219"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="26.889999999999997%" id="mcps1.2.4.1.2"><p id="p67821316195019"><a name="p67821316195019"></a><a name="p67821316195019"></a>Add-on Version</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.970000000000006%" id="mcps1.2.4.1.3"><p id="p181814453425"><a name="p181814453425"></a><a name="p181814453425"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row178631475226"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.4.1.1 "><p id="p386464792210"><a name="p386464792210"></a><a name="p386464792210"></a>Add-on Specifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p187822016135018"><a name="p187822016135018"></a><a name="p187822016135018"></a>Available in all versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.970000000000006%" headers="mcps1.2.4.1.3 "><p id="p1861133733913"><a name="p1861133733913"></a><a name="p1861133733913"></a>Possible values:</p>
    <a name="ul1634319358233"></a><a name="ul1634319358233"></a><ul id="ul1634319358233"><li><strong id="b15151353408"><a name="b15151353408"></a><a name="b15151353408"></a>Single</strong>: The add-on has only one instance.</li><li><strong id="b1756816417401"><a name="b1756816417401"></a><a name="b1756816417401"></a>HA</strong>: The add-on has multiple instances for higher availability. This mode requires more compute resources.</li></ul>
    </td>
    </tr>
    <tr id="row921611101579"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.4.1.1 "><p id="p13217111055715"><a name="p13217111055715"></a><a name="p13217111055715"></a>Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p978271665019"><a name="p978271665019"></a><a name="p978271665019"></a>Available in all versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.970000000000006%" headers="mcps1.2.4.1.3 "><p id="p93701640145120"><a name="p93701640145120"></a><a name="p93701640145120"></a>Number of instances that will be created to match the selected add-on specifications. The number cannot be modified.</p>
    </td>
    </tr>
    <tr id="row087474432717"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.4.1.1 "><p id="p17875104414275"><a name="p17875104414275"></a><a name="p17875104414275"></a>Container</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p18782181655013"><a name="p18782181655013"></a><a name="p18782181655013"></a>Available in all versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.970000000000006%" headers="mcps1.2.4.1.3 "><p id="p1437014065110"><a name="p1437014065110"></a><a name="p1437014065110"></a>CPU and memory quotas of the container allowed for the selected add-on specifications. The quotas cannot be modified.</p>
    </td>
    </tr>
    <tr id="row142784417388"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.4.1.1 "><p id="p11271944133814"><a name="p11271944133814"></a><a name="p11271944133814"></a>Key pair</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p5557537162118"><a name="p5557537162118"></a><a name="p5557537162118"></a>Available only in certain versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.970000000000006%" headers="mcps1.2.4.1.3 "><p id="p14156122010527"><a name="p14156122010527"></a><a name="p14156122010527"></a>Key pair for logging in to the node to be added.</p>
    </td>
    </tr>
    <tr id="row7820124544210"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.4.1.1 "><p id="p7820184519425"><a name="p7820184519425"></a><a name="p7820184519425"></a><span class="keyword" id="keyword100872799152224"><a name="keyword100872799152224"></a><a name="keyword100872799152224"></a>Auto Scale-In</span></p>
    </td>
    <td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p18783316205019"><a name="p18783316205019"></a><a name="p18783316205019"></a>Available in all versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.970000000000006%" headers="mcps1.2.4.1.3 "><p id="p15974173353612"><a name="p15974173353612"></a><a name="p15974173353612"></a><strong id="b71141930125416"><a name="b71141930125416"></a><a name="b71141930125416"></a>Off</strong>: Auto scale-down is not allowed. Only auto scale-up is allowed.</p>
    <p id="p597311174372"><a name="p597311174372"></a><a name="p597311174372"></a><strong id="b127022174555"><a name="b127022174555"></a><a name="b127022174555"></a>On</strong>: Auto scale-down is allowed for both existing and added nodes.</p>
    <a name="ul20302135243"></a><a name="ul20302135243"></a><ul id="ul20302135243"><li><strong id="b17363726987"><a name="b17363726987"></a><a name="b17363726987"></a>Idle Time (min)</strong>: Time for which a node should be unneeded before it is eligible for scale-down. Default value: 10 minutes.</li><li><strong id="b8909114211199"><a name="b8909114211199"></a><a name="b8909114211199"></a>Resource Usage</strong>: If the percentage of both CPU and memory usage on a node is below this threshold, auto scale-down will be triggered to delete the node from the cluster. The default value is 0.5, which means 50%.</li><li><strong id="b202941912112817"><a name="b202941912112817"></a><a name="b202941912112817"></a>Scaledown Delay After Scaleup</strong>: The time after scale-up that the scale-down evaluation will resume. Default value: 10 minutes.</li><li><strong id="b1231414234318"><a name="b1231414234318"></a><a name="b1231414234318"></a>Scaledown Delay After Node Deletion</strong>: The time after node deletion that the scale-down evaluation will resume. Default value: 10 minutes.</li><li><strong id="b1833570143215"><a name="b1833570143215"></a><a name="b1833570143215"></a>Scaledown Delay After Failure</strong>: The time after a scale-down failure that the scale-down evaluation will resume. Default value: 3 minutes.</li><li><strong id="b3786135619320"><a name="b3786135619320"></a><a name="b3786135619320"></a>Max empty bulk delete</strong>: The maximum number of empty nodes that can be deleted at the same time. Default value: 10.</li><li><strong id="b138444433363"><a name="b138444433363"></a><a name="b138444433363"></a>Node Recheck Timeout</strong>: The timeout before autoscaler checks again the node that could not be previously removed. Default value: 5 minutes.</li></ul>
    <div class="note" id="note15581214141911"><a name="note15581214141911"></a><a name="note15581214141911"></a><span class="notetitle"> NOTE: </span><div class="notebody"><div class="p" id="p424619478180"><a name="p424619478180"></a><a name="p424619478180"></a>If a node is consistently unneeded for a significant amount of time (default: 10 min), it will be considered for removal. However, the following pods cannot be removed from a cluster:<a name="ul128441417142719"></a><a name="ul128441417142719"></a><ul id="ul128441417142719"><li>Pods with restrictive <strong id="b842352706152513"><a name="b842352706152513"></a><a name="b842352706152513"></a>PodDisruptionBudget</strong></li><li>Pods with local storage</li><li>Pods that cannot be moved elsewhere due to various constraints (lack of resources, non-matching node selectors or affinity, matching anti-affinity, etc)</li><li>Pods that have the <strong id="b842352706153017"><a name="b842352706153017"></a><a name="b842352706153017"></a>"cluster-autoscaler.kubernetes.io/safe-to-evict": "false"</strong> annotation</li><li>Kube-system pods that are not run on the node by default, excluding the pods created by DaemonSets</li><li>Pods that are not created by deployments, ReplicaSets, jobs, StatefulSets, or other controllers</li></ul>
    </div>
    </div></div>
    </td>
    </tr>
    <tr id="row10588111641417"><td class="cellrowborder" valign="top" width="21.14%" headers="mcps1.2.4.1.1 "><p id="p20580042144816"><a name="p20580042144816"></a><a name="p20580042144816"></a>Node Pool Configuration</p>
    </td>
    <td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.4.1.2 "><p id="p778321665013"><a name="p778321665013"></a><a name="p778321665013"></a>Available only in certain versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.970000000000006%" headers="mcps1.2.4.1.3 "><p id="p106311133304"><a name="p106311133304"></a><a name="p106311133304"></a>A node pool is a group of compute nodes with the same node type, specifications, and labels. When the cluster needs to be scaled up, autoscaler will automatically select nodes from these node pools to the cluster. If no custom node pool is available, autoscaler will use the default node pool.</p>
    <p id="p2087715518406"><a name="p2087715518406"></a><a name="p2087715518406"></a>Click <strong id="b16709165713368"><a name="b16709165713368"></a><a name="b16709165713368"></a>Add Node Pool Configuration</strong> and set the following parameters:</p>
    <a name="ul378119275614"></a><a name="ul378119275614"></a><ul id="ul378119275614"><li><strong id="b1869716517332"><a name="b1869716517332"></a><a name="b1869716517332"></a>AZ</strong>: A physical region where resources use independent power supplies and networks. AZs are physically isolated but interconnected through the internal network.</li><li><strong id="b8584599566"><a name="b8584599566"></a><a name="b8584599566"></a>OS</strong>: OS of the nodes to be created.</li><li><strong id="b713584464116"><a name="b713584464116"></a><a name="b713584464116"></a>Taints</strong>: No taints are added by default.<div class="p" id="p7853111720153"><a name="p7853111720153"></a><a name="p7853111720153"></a>Taints allow nodes to repel a set of pods. You can add a maximum of 10 taints for each node pool. Each taint contains the following parameters:<a name="ul17274222121015"></a><a name="ul17274222121015"></a><ul id="ul17274222121015"><li><strong id="b6921811213"><a name="b6921811213"></a><a name="b6921811213"></a>Key</strong>: A key must contain 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed. A DNS subdomain name can be used as the prefix of a key.</li><li><strong id="b17301821282"><a name="b17301821282"></a><a name="b17301821282"></a>Value</strong>: A value must start with a letter or digit and can contain a maximum of 63 characters, including letters, digits, hyphens (-), underscores (_), and periods (.).</li><li><strong id="b838411376810"><a name="b838411376810"></a><a name="b838411376810"></a>Effect</strong>: Available options are <strong id="b10854184131219"><a name="b10854184131219"></a><a name="b10854184131219"></a>NoSchedule</strong>, <strong id="b15432119161211"><a name="b15432119161211"></a><a name="b15432119161211"></a>PreferNoSchedule</strong>, and <strong id="b73476124120"><a name="b73476124120"></a><a name="b73476124120"></a>NoExecute</strong>.</li></ul>
    <div class="notice" id="note77443231113"><a name="note77443231113"></a><a name="note77443231113"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul104271158181515"></a><a name="ul104271158181515"></a><ul id="ul104271158181515"><li>If taints are used, you must configure tolerations in the YAML files of pods. Otherwise, scale-up may fail or pods cannot be scheduled onto the added nodes.</li><li>Taints cannot be modified after configuration. Incorrect taints may cause a scale-up failure or prevent pods from being scheduled onto the added nodes.</li></ul>
    </div></div>
    </div>
    </li><li><strong id="b76081141194516"><a name="b76081141194516"></a><a name="b76081141194516"></a>Resource Tags</strong>: Resource tags can be added to classify resources.<div class="note" id="note1873655813232"><a name="note1873655813232"></a><a name="note1873655813232"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1682495163615"><a name="p1682495163615"></a><a name="p1682495163615"></a>You can create predefined tags in Tag Management Service (TMS). Predefined tags are visible to all service resources that support the tagging function. You can use predefined tags to improve tag creation and migration efficiency.</p>
    </div></div>
    </li><li><strong id="b651061314582"><a name="b651061314582"></a><a name="b651061314582"></a>Specifications</strong>: CPU and memory of the added nodes.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    To configure more add-on parameters, click  **Advanced Settings**  at the bottom of this page.

    **Table  2**  Advanced settings

    <a name="table9850103573510"></a>
    <table><thead align="left"><tr id="row4607144693512"><th class="cellrowborder" valign="top" width="20.747925207479252%" id="mcps1.2.4.1.1"><p id="p39151855123517"><a name="p39151855123517"></a><a name="p39151855123517"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="20.54794520547945%" id="mcps1.2.4.1.2"><p id="p855211155116"><a name="p855211155116"></a><a name="p855211155116"></a>Add-on Version</p>
    </th>
    <th class="cellrowborder" valign="top" width="58.70412958704129%" id="mcps1.2.4.1.3"><p id="p18915195517356"><a name="p18915195517356"></a><a name="p18915195517356"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row385043515351"><td class="cellrowborder" valign="top" width="20.747925207479252%" headers="mcps1.2.4.1.1 "><p id="p129911124203017"><a name="p129911124203017"></a><a name="p129911124203017"></a>Total Nodes</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54794520547945%" headers="mcps1.2.4.1.2 "><p id="p6552211145111"><a name="p6552211145111"></a><a name="p6552211145111"></a>Available in all versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.70412958704129%" headers="mcps1.2.4.1.3 "><p id="p29911924143017"><a name="p29911924143017"></a><a name="p29911924143017"></a>The total number of nodes up to which the cluster can be scaled.</p>
    </td>
    </tr>
    <tr id="row1785163517352"><td class="cellrowborder" valign="top" width="20.747925207479252%" headers="mcps1.2.4.1.1 "><p id="p09919249305"><a name="p09919249305"></a><a name="p09919249305"></a>Total Cores</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54794520547945%" headers="mcps1.2.4.1.2 "><p id="p1155221145112"><a name="p1155221145112"></a><a name="p1155221145112"></a>Available in all versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.70412958704129%" headers="mcps1.2.4.1.3 "><p id="p10991724113018"><a name="p10991724113018"></a><a name="p10991724113018"></a>The total number of cores up to which the cluster can be scaled.</p>
    </td>
    </tr>
    <tr id="row208511335113518"><td class="cellrowborder" valign="top" width="20.747925207479252%" headers="mcps1.2.4.1.1 "><p id="p7991152414302"><a name="p7991152414302"></a><a name="p7991152414302"></a>Total Memory (GB)</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54794520547945%" headers="mcps1.2.4.1.2 "><p id="p6552111114512"><a name="p6552111114512"></a><a name="p6552111114512"></a>Available in all versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.70412958704129%" headers="mcps1.2.4.1.3 "><p id="p199916247301"><a name="p199916247301"></a><a name="p199916247301"></a>The total memory up to which the cluster can be scaled.</p>
    </td>
    </tr>
    <tr id="row1855315467519"><td class="cellrowborder" valign="top" width="20.747925207479252%" headers="mcps1.2.4.1.1 "><p id="p1627256173617"><a name="p1627256173617"></a><a name="p1627256173617"></a>Auto Scale-Out</p>
    </td>
    <td class="cellrowborder" valign="top" width="20.54794520547945%" headers="mcps1.2.4.1.2 "><p id="p1298713575516"><a name="p1298713575516"></a><a name="p1298713575516"></a>Available only in certain versions</p>
    </td>
    <td class="cellrowborder" valign="top" width="58.70412958704129%" headers="mcps1.2.4.1.3 "><p id="p11311054125310"><a name="p11311054125310"></a><a name="p11311054125310"></a><strong id="b340112810534"><a name="b340112810534"></a><a name="b340112810534"></a>Triggered when there are pods unscheduled</strong>:  Selected by default and can be deselected.</p>
    <p id="p9473161514537"><a name="p9473161514537"></a><a name="p9473161514537"></a><strong id="b1147421516534"><a name="b1147421516534"></a><a name="b1147421516534"></a>Utilization Scale-up</strong>: Select this option to allow auto scale-up to be triggered when cluster resource usage reaches the threshold.</p>
    <a name="ul2047421555319"></a><a name="ul2047421555319"></a><ul id="ul2047421555319"><li><strong id="b24741215145320"><a name="b24741215145320"></a><a name="b24741215145320"></a>Cpu Utilization</strong>: The autoscaler adds nodes if the CPU usage of the node pool reaches the specified limit.</li><li><strong id="b5474415195312"><a name="b5474415195312"></a><a name="b5474415195312"></a>Memory Utilization</strong>: The autoscaler adds nodes if the memory usage of the node pool reaches the specified limit.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

4.  When the configuration is complete, click  **Install**.

    After the installation is complete, you can view the add-on instance on the  **Add-on Instance**  tab page. This indicates that the add-on has been installed in the current cluster.


## Uninstalling the Add-on<a name="section610455514114"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Instance**  tab page, select the cluster and click  **Uninstall**  under  **autoscaler**.
2.  In the dialog box that is displayed, click  **Yes**  to uninstall the add-on.

