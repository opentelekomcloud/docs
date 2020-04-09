# Risky Operations on Cluster Nodes<a name="cce_01_0054"></a>

## Precautions for Using a Cluster<a name="en-us_topic_0203988265_section12415304374"></a>

-   When performing operations such as creating, deleting, and scaling clusters, do not change user permission in the Identity and Access Management \(IAM\) console. Otherwise, these operations may fail.
-   The containerized network canal of CCE nodes uses a CIDR block as the CIDR block of the container network. This CIDR block can be configured during cluster creation and defaults to 172.16.0.0/16. The Docker service creates a docker0 bridge by default. The default docker0 address is 172.17.0.1. When creating a cluster, ensure that the CIDR block of the VPC in the cluster is different from the CIDR blocks of the container network docker0 bridge. If VPC peering connections are used, also ensure that the CIDR block of the peer VPC is different from the CIDR blocks of the container network docker0 bridge.

-   Do not modify the security groups, Elastic Volume Service \(EVS\) disks, and other resources created by CCE. Otherwise, clusters may not function properly. The resources created by CCE are labeled  **cce**, for example,  **cce-evs-jwh9pcl7-\*\*\*\***.

## Precautions for Using a Node<a name="section19751152619340"></a>

Some of the resources on the node need to run some necessary Kubernetes system components and resources to make the node as part of your cluster. Therefore, the total number of node resources and the number of assignable node resources in Kubernetes are different. The larger the node specifications, the more the containers deployed on the node. Therefore, Kubernetes needs to reserve more resources.

To ensure node stability, CCE cluster nodes reserve some resources for Kubernetes components \(such as kubelet, kube-proxy, and docker\) based on node specifications.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>You are advised not to install software or modify the operating system \(OS\) configuration on a cluster node. This may cause exceptions on Kubernetes components installed on the node, and make the node unavailable.  

## Risky Operations on Nodes<a name="en-us_topic_0203988265_section1688214368495"></a>

After logging in to a node created by CCE, do not perform the following operations. Otherwise,  the node will become unready.

**Table  1**  Operations that will cause nodes to become unready

<a name="en-us_topic_0203988265_en-us_topic_0074268051_table275811429288"></a>
<table><thead align="left"><tr id="en-us_topic_0203988265_en-us_topic_0074268051_row112303759288"><th class="cellrowborder" valign="top" width="9.87%" id="mcps1.2.5.1.1"><p id="en-us_topic_0203988265_en-us_topic_0074268051_p667710269288"><a name="en-us_topic_0203988265_en-us_topic_0074268051_p667710269288"></a><a name="en-us_topic_0203988265_en-us_topic_0074268051_p667710269288"></a>SN</p>
</th>
<th class="cellrowborder" valign="top" width="35.75%" id="mcps1.2.5.1.2"><p id="en-us_topic_0203988265_en-us_topic_0074268051_p4794206293155"><a name="en-us_topic_0203988265_en-us_topic_0074268051_p4794206293155"></a><a name="en-us_topic_0203988265_en-us_topic_0074268051_p4794206293155"></a>Risky Operation</p>
</th>
<th class="cellrowborder" valign="top" width="21.6%" id="mcps1.2.5.1.3"><p id="en-us_topic_0203988265_p378914461617"><a name="en-us_topic_0203988265_p378914461617"></a><a name="en-us_topic_0203988265_p378914461617"></a>Impact</p>
</th>
<th class="cellrowborder" valign="top" width="32.78%" id="mcps1.2.5.1.4"><p id="en-us_topic_0203988265_p115912613377"><a name="en-us_topic_0203988265_p115912613377"></a><a name="en-us_topic_0203988265_p115912613377"></a>Solution</p>
</th>
</tr>
</thead>
<tbody><tr id="en-us_topic_0203988265_en-us_topic_0074268051_row26713570113514"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0203988265_p13474145214175"><a name="en-us_topic_0203988265_p13474145214175"></a><a name="en-us_topic_0203988265_p13474145214175"></a>1</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0203988265_p18821616143613"><a name="en-us_topic_0203988265_p18821616143613"></a><a name="en-us_topic_0203988265_p18821616143613"></a>Reinstall the operating system using the original image or another image</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0203988265_p157891746163"><a name="en-us_topic_0203988265_p157891746163"></a><a name="en-us_topic_0203988265_p157891746163"></a>The node will become unready.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0203988265_p1559117663719"><a name="en-us_topic_0203988265_p1559117663719"></a><a name="en-us_topic_0203988265_p1559117663719"></a>Delete the node and buy a new node.</p>
</td>
</tr>
<tr id="en-us_topic_0203988265_row1332010131816"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0203988265_p033191020188"><a name="en-us_topic_0203988265_p033191020188"></a><a name="en-us_topic_0203988265_p033191020188"></a>2</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0203988265_p1533121051820"><a name="en-us_topic_0203988265_p1533121051820"></a><a name="en-us_topic_0203988265_p1533121051820"></a>Modify OS configuration</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0203988265_p1733171018185"><a name="en-us_topic_0203988265_p1733171018185"></a><a name="en-us_topic_0203988265_p1733171018185"></a>The node will become unready.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0203988265_p9592196143718"><a name="en-us_topic_0203988265_p9592196143718"></a><a name="en-us_topic_0203988265_p9592196143718"></a>Restore the original configuration or buy the node again.</p>
</td>
</tr>
<tr id="en-us_topic_0203988265_en-us_topic_0074268051_row459635119288"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0203988265_p347418524175"><a name="en-us_topic_0203988265_p347418524175"></a><a name="en-us_topic_0203988265_p347418524175"></a>3</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0203988265_p887841623614"><a name="en-us_topic_0203988265_p887841623614"></a><a name="en-us_topic_0203988265_p887841623614"></a>Delete the <strong id="en-us_topic_0203988265_b2848184815488"><a name="en-us_topic_0203988265_b2848184815488"></a><a name="en-us_topic_0203988265_b2848184815488"></a>opt</strong> directory, <strong id="en-us_topic_0203988265_b784910484480"><a name="en-us_topic_0203988265_b784910484480"></a><a name="en-us_topic_0203988265_b784910484480"></a>/var/paas</strong> directory, or a data disk</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0203988265_p14789104111613"><a name="en-us_topic_0203988265_p14789104111613"></a><a name="en-us_topic_0203988265_p14789104111613"></a>The node will become unready.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0203988265_p105921623717"><a name="en-us_topic_0203988265_p105921623717"></a><a name="en-us_topic_0203988265_p105921623717"></a>Delete the node and buy a new node.</p>
</td>
</tr>
<tr id="en-us_topic_0203988265_en-us_topic_0074268051_row10353620112057"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0203988265_p1847417527172"><a name="en-us_topic_0203988265_p1847417527172"></a><a name="en-us_topic_0203988265_p1847417527172"></a>4</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0203988265_p1187431610365"><a name="en-us_topic_0203988265_p1187431610365"></a><a name="en-us_topic_0203988265_p1187431610365"></a>Format and partition a node disk</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0203988265_p1978917461620"><a name="en-us_topic_0203988265_p1978917461620"></a><a name="en-us_topic_0203988265_p1978917461620"></a>The node will become unready.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0203988265_p16592768378"><a name="en-us_topic_0203988265_p16592768378"></a><a name="en-us_topic_0203988265_p16592768378"></a>Delete the node and buy a new node.</p>
</td>
</tr>
<tr id="en-us_topic_0203988265_row19857131110174"><td class="cellrowborder" valign="top" width="9.87%" headers="mcps1.2.5.1.1 "><p id="en-us_topic_0203988265_p11474135216170"><a name="en-us_topic_0203988265_p11474135216170"></a><a name="en-us_topic_0203988265_p11474135216170"></a>5</p>
</td>
<td class="cellrowborder" valign="top" width="35.75%" headers="mcps1.2.5.1.2 "><p id="en-us_topic_0203988265_p2085811151718"><a name="en-us_topic_0203988265_p2085811151718"></a><a name="en-us_topic_0203988265_p2085811151718"></a>Modify a security group</p>
</td>
<td class="cellrowborder" valign="top" width="21.6%" headers="mcps1.2.5.1.3 "><p id="en-us_topic_0203988265_p118581511181715"><a name="en-us_topic_0203988265_p118581511181715"></a><a name="en-us_topic_0203988265_p118581511181715"></a>The node will become unready or the cluster will exhibit unexpected behavior.</p>
</td>
<td class="cellrowborder" valign="top" width="32.78%" headers="mcps1.2.5.1.4 "><p id="en-us_topic_0203988265_p126212039121815"><a name="en-us_topic_0203988265_p126212039121815"></a><a name="en-us_topic_0203988265_p126212039121815"></a>Correct the security group settings based on security group settings of normal clusters.</p>
</td>
</tr>
</tbody>
</table>

