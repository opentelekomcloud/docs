# Differences Between CCE 1.0 and CCE 2.0<a name="cce_01_9998"></a>

CCE 2.0 inherits and modifies the features of CCE 1.0, and release new features.

-   Modified features:
    -   Clusters in CCE 1.0 are equivalent to VM clusters in CCE 2.0.
    -   CCE 2.0 does not have the concept of component template. In CCE 1.0, you can set parameters in the component template when creating an application.
    -   Applications in CCE 1.0 are equivalent to Deployments in CCE 2.0. In addition, the concept of StatefulSet is added in CCE 2.0.

-   New Features:
    -   EVS disks and file storage can be created and directly mounted during workload creation on the CCE console.
    -   Auto scaling for cluster nodes.
    -   Docker upgraded to the 1706 version.
    -   Customized helm charts for orchestrating workloads.

-   In CCE 2.0, before uploading an image, you must create an image repository.

The following table compares the two versions.

**Table  1**  Comparison between CCE 1.0 and CCE 2.0

<a name="table1542418017574"></a>
<table><thead align="left"><tr id="row1842620018575"><th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.1"><p id="p1521569576"><a name="p1521569576"></a><a name="p1521569576"></a>CCE 1.0</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.2.3.1.2"><p id="p12166175715"><a name="p12166175715"></a><a name="p12166175715"></a>CCE 2.0</p>
</th>
</tr>
</thead>
<tbody><tr id="row174262045719"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p16417613575"><a name="p16417613575"></a><a name="p16417613575"></a>Container registry</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p44967578"><a name="p44967578"></a><a name="p44967578"></a>Image repository</p>
</td>
</tr>
<tr id="row5426804576"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p2613635719"><a name="p2613635719"></a><a name="p2613635719"></a>Cluster</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p46196205715"><a name="p46196205715"></a><a name="p46196205715"></a>Resource Management &gt; VM Cluster</p>
</td>
</tr>
<tr id="row144261102575"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p581635711"><a name="p581635711"></a><a name="p581635711"></a>Component template</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p59462576"><a name="p59462576"></a><a name="p59462576"></a>-</p>
</td>
</tr>
<tr id="row154264016570"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p201096175713"><a name="p201096175713"></a><a name="p201096175713"></a>App Designer</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p91213635713"><a name="p91213635713"></a><a name="p91213635713"></a>-</p>
</td>
</tr>
<tr id="row13426100205719"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.1 "><p id="p4129610570"><a name="p4129610570"></a><a name="p4129610570"></a>App Manager</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.2.3.1.2 "><p id="p11313615576"><a name="p11313615576"></a><a name="p11313615576"></a>Deployment</p>
</td>
</tr>
</tbody>
</table>

