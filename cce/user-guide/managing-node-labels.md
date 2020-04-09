# Managing Node Labels<a name="cce_01_0004"></a>

You can add different labels to nodes and define different attributes for labels. By using these  node labels, you can quickly understand the characteristics of each node.

## Node Label Usage Scenario<a name="section825504204814"></a>

Node labels are mainly used in the following scenarios:

-   Node management: Node labels are used to classify nodes.
-   Affinity and anti-affinity between a workload and node:
    -   Some workloads require a large CPU, some require a large memory, some require a large I/O, and other workloads may be affected. In this case, you are advised to add different labels to nodes. When deploying a workload, you can select node affinity deployment of the corresponding label to ensure the normal operation of the system. Otherwise, node anti-affinity deployment can be used.
    -   A system can be divided into multiple modules. Each module consists of multiple microservices. To ensure the efficiency of subsequent O&M, you can add a module label to each node so that each module can be deployed on the corresponding node, does not interfere with other modules, and can be easily developed and maintained on its node.


## Inherent Label of a Node<a name="section74111324152813"></a>

After a node is created, some fixed labels exist and cannot be deleted. For details about these labels, see  [Table 1](#table83962234533).

**Table  1**  Inherent label of a node

<a name="table83962234533"></a>
<table><thead align="left"><tr id="row941112314533"><th class="cellrowborder" valign="top" width="34%" id="mcps1.2.3.1.1"><p id="p1541113238536"><a name="p1541113238536"></a><a name="p1541113238536"></a>Key</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.3.1.2"><p id="p1741119232538"><a name="p1741119232538"></a><a name="p1741119232538"></a>Value</p>
</th>
</tr>
</thead>
<tbody><tr id="row186452248235"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1664611247230"><a name="p1664611247230"></a><a name="p1664611247230"></a>failure-domain.beta.kubernetes.io/is-baremetal</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p10646132416235"><a name="p10646132416235"></a><a name="p10646132416235"></a>Indicates whether the node is a bare-metal node.</p>
<p id="p878819218284"><a name="p878819218284"></a><a name="p878819218284"></a><strong id="b137781937201815"><a name="b137781937201815"></a><a name="b137781937201815"></a>False</strong> indicates that the node is not a bare-metal node.</p>
</td>
</tr>
<tr id="row1441182305312"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p841172365311"><a name="p841172365311"></a><a name="p841172365311"></a>failure-domain.beta.kubernetes.io/region</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p38743391437"><a name="p38743391437"></a><a name="p38743391437"></a>Indicates the region where the node is located.</p>
</td>
</tr>
<tr id="row11411923145318"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p6411182312531"><a name="p6411182312531"></a><a name="p6411182312531"></a>failure-domain.beta.kubernetes.io/zone</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p04681235194313"><a name="p04681235194313"></a><a name="p04681235194313"></a>Indicates the AZ where the node is located.</p>
</td>
</tr>
<tr id="row85011821447"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p950218211147"><a name="p950218211147"></a><a name="p950218211147"></a>node.kubernetes.io/subnetid</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p950282110419"><a name="p950282110419"></a><a name="p950282110419"></a>Indicates a subnet ID.</p>
</td>
</tr>
<tr id="row15411523165312"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p2411192310532"><a name="p2411192310532"></a><a name="p2411192310532"></a>os.architecture</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p1741162315319"><a name="p1741162315319"></a><a name="p1741162315319"></a>Indicates the processor architecture of a node.</p>
<p id="p11218831135415"><a name="p11218831135415"></a><a name="p11218831135415"></a>For example, <strong id="b842352706145330"><a name="b842352706145330"></a><a name="b842352706145330"></a>amd64</strong> indicates an AMD64-bit processor.</p>
</td>
</tr>
<tr id="row17411162365318"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p8411102345311"><a name="p8411102345311"></a><a name="p8411102345311"></a>os.name</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p7411112315537"><a name="p7411112315537"></a><a name="p7411112315537"></a>Indicates the operating system name of a node.</p>
<p id="p191918573565"><a name="p191918573565"></a><a name="p191918573565"></a>For example, <strong id="b842352706145337"><a name="b842352706145337"></a><a name="b842352706145337"></a>EulerOS_2.0_SP5</strong> indicates the version of Euler 2.5.</p>
</td>
</tr>
<tr id="row1041115238531"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p2411323135319"><a name="p2411323135319"></a><a name="p2411323135319"></a>os.version</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p641192311530"><a name="p641192311530"></a><a name="p641192311530"></a>Indicates the kernel version of a node.</p>
</td>
</tr>
</tbody>
</table>

## Adding a Node Label<a name="section33951611481"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Nodes**.
2.  In the same row as the node for which you will add labels, choose  **Operation**  \>  **Manage Labels**.
3.  Click  **Add Label**, enter a label key and value, and click  **OK**.

    As shown in the figure, the key is  **deploy\_qa**  and the value is  **true**, indicating that the node is used to deploy the QA \(test\) environment.

4.  After the label is added, click  **Manage Label**. Then, you will see the label that you have added.

## Deleting a Node Label<a name="section947332017485"></a>

Only labels added by users can be deleted. Labels that are fixed on the node cannot be deleted.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Nodes**.
2.  In the same row as the node for which you will delete labels, choose  **Operation**  \>  **Manage Labels**.
3.  Click  **Delete**, and then click  **OK**  to delete the label.

    **Label updated successfully.**  is displayed.


