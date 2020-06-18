# Setting Container Specifications<a name="cce_01_0163"></a>

CCE allows you to set resource restrictions for added containers during workload creation. You can apply for and limit the CPU and memory used by each instance of the workload.

>![](/images/icon-note.gif) **NOTE:**   
>-   After the  CPU quota  and  memory quota  are selected, select  **Apply**  to start the configuration. The system schedules the instance to the node that meets the requirements to deploy the workload based on the applied value. If you do not select  **Apply**, the system schedules the instance to a random node to deploy the workload. If you select  **Restrict**, the configuration is started and the resources used by the workload are restricted based on the configured value. If you do not select  **Restrict**, the resources used by the instance are not restricted. If the memory resources used by the instance exceed the memory allocated to the node, the workload or node may be unavailable.  
>-   When creating a workload, you are advised to set the upper and lower limits of CPU and memory resources. If the upper and lower resource limits are not set for a workload, a resource leak of this workload will make resources unavailable for other workloads deployed on the same node. In addition, workloads that do not have upper and lower resource limits cannot be accurately monitored.  

-   CPU quotas:

    **Table  1**  Description of CPU quotas

    <a name="table362417589103"></a>
    <table><thead align="left"><tr id="row186251758111012"><th class="cellrowborder" valign="top" width="17%" id="mcps1.2.3.1.1"><p id="p762595815102"><a name="p762595815102"></a><a name="p762595815102"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="83%" id="mcps1.2.3.1.2"><p id="p8625105813106"><a name="p8625105813106"></a><a name="p8625105813106"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row162511587103"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p2625135851014"><a name="p2625135851014"></a><a name="p2625135851014"></a>CPU request</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p262515818104"><a name="p262515818104"></a><a name="p262515818104"></a>Minimum number of CPU cores required by a container. Resources are scheduled for the container based on this value. The container can be scheduled to this node only when the total available CPU on the node is greater than or equal to the number of containerized CPU applications.</p>
    </td>
    </tr>
    <tr id="row172431422171112"><td class="cellrowborder" valign="top" width="17%" headers="mcps1.2.3.1.1 "><p id="p1424472219115"><a name="p1424472219115"></a><a name="p1424472219115"></a>CPU limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="83%" headers="mcps1.2.3.1.2 "><p id="p524412223119"><a name="p524412223119"></a><a name="p524412223119"></a>Maximum number of CPU cores available for a container.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Recommended configuration method:**  The actual available CPU of a node ≥ The sum of CPU limits of all containers on the current instance ≥ The sum of CPU requests of all containers on the current instance. In the navigation pane, choose  **Resource Management**  \>  **Nodes**. Under the  **Available CPU \(Core\)**  column, view the actual available CPU of the node.


-   Memory quotas:

    **Table  2**  Description of memory quotas

    <a name="table164121625191912"></a>
    <table><thead align="left"><tr id="row64131325111910"><th class="cellrowborder" valign="top" width="18%" id="mcps1.2.3.1.1"><p id="p154131025111914"><a name="p154131025111914"></a><a name="p154131025111914"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="82%" id="mcps1.2.3.1.2"><p id="p16413325111912"><a name="p16413325111912"></a><a name="p16413325111912"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1241310258194"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p15413225131915"><a name="p15413225131915"></a><a name="p15413225131915"></a>Memory request</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p541362541919"><a name="p541362541919"></a><a name="p541362541919"></a>Minimum amount of memory required by a container. Resources are scheduled for the container based on this value. The container can be scheduled to this node only when the total available memory on the node is greater than or equal to the number of containerized memory applications.</p>
    </td>
    </tr>
    <tr id="row1413325101918"><td class="cellrowborder" valign="top" width="18%" headers="mcps1.2.3.1.1 "><p id="p241312517195"><a name="p241312517195"></a><a name="p241312517195"></a>Memory Limit</p>
    </td>
    <td class="cellrowborder" valign="top" width="82%" headers="mcps1.2.3.1.2 "><p id="p1241352520199"><a name="p1241352520199"></a><a name="p1241352520199"></a>Maximum amount of memory available for a container. When the memory usage exceeds the configured memory limit, the instance may be restarted, which affects the normal use of the workload.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Recommended configuration method:**  The actual available memory of a node ≥ The sum of memory limits of all containers on the current node ≥ The sum of memory requests of all containers on the current node. In the navigation pane, choose  **Resource Management**  \>  **Nodes**. Under the  **Available Memory \(GB\)**  column, view the actual available memory of the node.


## Example<a name="section17887209103612"></a>

Assume that a cluster contains a node whose resource is 4 Core 8 GB. A workload containing two instances has been deployed on the cluster. The resources of the two instances \(instances 1 and 2\) are as follows: \{CPU request, CPU limit, memory request, memory limit\} = \{1 Core, 2 Core, 2 GB, 2 GB\}.

The CPU and memory usage of the node are as follows:

-   Allocatable CPU = 4 Core - \(1 Core applied by instance 1 + 1 Core applied by instance 2\) = 2 Core
-   Allocatable memory = 8 GB - \(2 GB applied by instance 1 + 2 GB applied by instance 2\) = 4 GB

Therefore, the remaining 2 Core 4 GB resources can be used by the next new instance.

