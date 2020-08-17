# Risky Operations on Cluster Nodes<a name="cce_01_0054"></a>

## Precautions for Using a Cluster<a name="section12415304374"></a>

-   When performing operations such as creating, deleting, and scaling clusters, do not change user permission in the Identity and Access Management \(IAM\) console. Otherwise, these operations may fail.
-   The containerized network canal of CCE nodes uses a CIDR block as the CIDR block of the container network. This CIDR block can be configured during cluster creation and defaults to 172.16.0.0/16. The Docker service creates a docker0 bridge by default. The default docker0 address is 172.17.0.1. When creating a cluster, ensure that the CIDR block of the VPC in the cluster is different from the CIDR blocks of the container network docker0 bridge. If VPC peering connections are used, also ensure that the CIDR block of the peer VPC is different from the CIDR blocks of the container network docker0 bridge.
-   For a cluster of Kubernetes v1.15, the DNS server of nodes in the cluster uses the DNS address in the VPC subnet, not the CoreDNS address of Kubernetes. Ensure that the DNS address in the subnet exists and is configurable.
-   Do not modify the security groups, Elastic Volume Service \(EVS\) disks, and other resources created by CCE. Otherwise, clusters may not function properly. The resources created by CCE are labeled  **cce**, for example,  **cce-evs-jwh9pcl7-\*\*\*\***.
-   When adding a node, ensure that the DNS server in the subnet can resolve the domain name of the corresponding service. Otherwise, the node cannot be installed properly.

## Precautions for Using a Node<a name="section19751152619340"></a>

Some of the resources on the node need to run some necessary Kubernetes system components and resources to make the node as part of your cluster. Therefore, the total number of node resources and the number of assignable node resources in Kubernetes are different. The larger the node specifications, the more the containers deployed on the node. Therefore, Kubernetes needs to reserve more resources.

To ensure node stability, CCE cluster nodes reserve some resources for Kubernetes components \(such as kubelet, kube-proxy, and docker\) based on node specifications.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>You are advised not to install software or modify the operating system \(OS\) configuration on a cluster node. This may cause exceptions on Kubernetes components installed on the node, and make the node unavailable.

## Risky Operations on Nodes<a name="section1688214368495"></a>

After logging in to a node created by CCE, do not perform the following operations. Otherwise,  the node will become unready.

**Table  1**  Operations that will cause nodes to become unready

<a name="en-us_topic_0074268051_table275811429288"></a>
<table><thead align="left"><tr id="en-us_topic_0074268051_row112303759288"><th class="cellrowborder" valign="top" width="9.87%" id="mcps1.2.5.1.1"><p id="en-us_topic_0074268051_p667710269288"><a name="en-us_topic_0074268051_p667710269288"></a><a name="en-us_topic_0074268051_p667710269288"></a>SN</p>
</th>
<th class="cellrowborder" valign="top" width="35.75%" id="mcps1.2.5.1.2"><p id="en-us_topic_0074268051_p4794206293155"><a name="en-us_topic_0074268051_p4794206293155"></a><a name="en-us_topic_0074268051_p4794206293155"></a>Risky Operation</p>
</th>
<th class="cellrowborder" valign="top" width="21.6%" id="mcps1.2.5.1.3"><p id="p378914461617"><a name="p378914461617"></a><a name="p378914461617"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="32.78%" id="mcps1.2.5.1.4"><p id="p115912613377"><a name="p115912613377"></a><a name="p115912613377"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0074268051_row26713570113514"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="p13474145214175"><a name="p13474145214175"></a><a name="p13474145214175"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="p18821616143613"><a name="p18821616143613"></a><a name="p18821616143613"></a>Reinstall the operating system using the original image or another image</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="p157891746163"><a name="p157891746163"></a><a name="p157891746163"></a>The node will become unready.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="p1559117663719"><a name="p1559117663719"></a><a name="p1559117663719"></a>Delete the node and buy a new node.</p>
</td>
</tr>
<tr id="row1332010131816"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="p033191020188"><a name="p033191020188"></a><a name="p033191020188"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="p1533121051820"><a name="p1533121051820"></a><a name="p1533121051820"></a>Modify OS configuration</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="p1733171018185"><a name="p1733171018185"></a><a name="p1733171018185"></a>The node will become unready.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="p9592196143718"><a name="p9592196143718"></a><a name="p9592196143718"></a>Restore the original configuration or buy the node again.</p>
</td>
</tr>
<tr id="en-us_topic_0074268051_row459635119288"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="p347418524175"><a name="p347418524175"></a><a name="p347418524175"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="p887841623614"><a name="p887841623614"></a><a name="p887841623614"></a>Delete the <strong id="b2848184815488"><a name="b2848184815488"></a><a name="b2848184815488"></a>opt</strong> directory, <strong id="b784910484480"><a name="b784910484480"></a><a name="b784910484480"></a>/var/paas</strong> directory, or a data disk</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="p14789104111613"><a name="p14789104111613"></a><a name="p14789104111613"></a>The node will become unready.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="p105921623717"><a name="p105921623717"></a><a name="p105921623717"></a>Delete the node and buy a new node.</p>
</td>
</tr>
<tr id="en-us_topic_0074268051_row10353620112057"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="p1847417527172"><a name="p1847417527172"></a><a name="p1847417527172"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="p1187431610365"><a name="p1187431610365"></a><a name="p1187431610365"></a>Format and partition a node disk</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="p1978917461620"><a name="p1978917461620"></a><a name="p1978917461620"></a>The node will become unready.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="p16592768378"><a name="p16592768378"></a><a name="p16592768378"></a>Delete the node and buy a new node.</p>
</td>
</tr>
<tr id="row19857131110174"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="p11474135216170"><a name="p11474135216170"></a><a name="p11474135216170"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="p2085811151718"><a name="p2085811151718"></a><a name="p2085811151718"></a>Modify a security group</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="p118581511181715"><a name="p118581511181715"></a><a name="p118581511181715"></a>The node will become unready or the cluster will exhibit unexpected behavior.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="p126212039121815"><a name="p126212039121815"></a><a name="p126212039121815"></a>Correct the security group settings based on security group settings of normal clusters.</p>
</td>
</tr>
</tbody>
</table>

