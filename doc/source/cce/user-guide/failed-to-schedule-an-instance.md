# Failed to Schedule an Instance<a name="cce_faq_00098"></a>

## Fault Locating<a name="en-us_topic_0242566250_section1197903153210"></a>

-   [Viewing K8s Event Information](#en-us_topic_0242566250_section1678344818322)
-   [Check Item 1: Checking Whether a Node Is Available in the Cluster](#en-us_topic_0242566250_section133416392418)
-   [Check Item 2: Checking Whether Node Resources \(CPU and Memory\) Are Sufficient](#en-us_topic_0242566250_section29231833141817)
-   [Check Item 3: Checking the Affinity and Anti-Affinity Configuration of the Workload](#en-us_topic_0242566250_section794092214205)
-   [Check Item 4: Checking Whether the Workload's Volume and Node Reside in the Same AZ](#en-us_topic_0242566250_section197421559143010)

## Viewing K8s Event Information<a name="en-us_topic_0242566250_section1678344818322"></a>

If the  workload  is in the Unready state and reports the "**InstanceSchedulingFailed**" event, check the workload's K8S events to identify the cause.

As shown in the following figure, the K8s event is "0/163 nodes are available: 133 Insufficient memory", indicating that the memory is insufficient.

**Complex scheduling failure information:**

-   **no nodes available to schedule pods**: No node resource is available for scheduling workload pods.
-   **0/163 nodes are available: 133 Insufficient memory**: The node is available but the memory is insufficient.
-   **163 Insufficient cpu**: The CPU is insufficient.
-   **49 Insufficient nvidia.com/gpu**: The nvidia.com/gpu resources are insufficient.
-   **49 InsufficientResourceOnSingleGPU**: GPU resources are insufficient.

**Information interpretation:**

-   **0/163 nodes are available**: There are 163 nodes in the cluster, and no node meets the scheduling rules.
-   **133 Insufficient memory**: The memory of 133 nodes is insufficient.
-   **163 Insufficient cpu**: The CPUs of 163 nodes are insufficient.
-   **49 Insufficient nvidia.com/gpu**: The GPUs of 49 nodes are insufficient.

The following is the fault locating procedure:

## Check Item 1: Checking Whether a Node Is Available in the Cluster<a name="en-us_topic_0242566250_section133416392418"></a>

Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Nodes**  to check whether the node where the workload runs is in the available state.

For example, the event "0/1 nodes are available: 1 node\(s\) were not ready, 1 node\(s\) were out of disk space" indicates that the pod fails to be scheduled due to no available node.

**Solution**

-   Add a node and migrate the pods to the new available node to ensure that services are running properly. Then, rectify the fault on the unavailable node. For details about the troubleshooting process, see the methods in the node FAQs.
-   Create a new node or repair the faulty one.

## Check Item 2: Checking Whether Node Resources \(CPU and Memory\) Are Sufficient<a name="en-us_topic_0242566250_section29231833141817"></a>

If the requested workload resources exceed the available resources of the node where the workload runs, the node cannot provide the resources required to run new pods and pod scheduling onto the node will definitely fail.

1.  On the CCE console, choose  **Workloads**  \>  **Deployments**  or  **StatefulSets**  in the navigation pane, click the workload name, and click  **Pods**  and then  **Events**  tabs to view pod events.

    The event "0/1 nodes are available: 1 Insufficient cpu" indicates that the pod fails to be scheduled due to insufficient node resources.

2.  In the navigation pane, choose  **Resource Management**  \>  **Nodes**  to view available CPUs and memory of the node where the workload runs.

    In this example, 0.88 vCPUs and 0.8 GiB memory are available for the node.

3.  In the navigation pane, choose  **Workloads**  and click the workload name to view the workload's CPU request and memory request.

    In this example, the CPU request is 2 vCPUs and the memory request is 0.5 GiB. The CPU request exceeds the available CPU resources, which causes pod scheduling to fail.


**Solution**

On the ECS console, modify node specifications to expand node resources.

## Check Item 3: Checking the Affinity and Anti-Affinity Configuration of the Workload<a name="en-us_topic_0242566250_section794092214205"></a>

Inappropriate affinity policies will cause pod scheduling to fail.

```
0/1 nodes are available: 1 node(s) didn't match pod affinity/anti-affintity, 1 node(s) didn't match pod anti-affinity rules.
```

**Solution**

-   When adding  **workload-workload affinity**  and  **workload-node affinity**  policies, ensure that the two types of policies do not conflict each other. Otherwise, workload deployment will fail. For example, workload deployment will fail if the following conditions are met:

    Assumptions: An anti-affinity relationship is established between workload 1 and workload 2. Workload 1 is deployed on node 1 while workload 2 is deployed on node 2.

    When you try to deploy workload 3 on node 3 and establish an affinity relationship with workload 2, a conflict occurs, resulting in a workload deployment failure.

-   If the workload has a node affinity policy, make sure that  **supportContainer**  in the label of the affinity node is set to  **true**. Otherwise, pods cannot be scheduled onto the affinity node and the following event is generated:

    ```
    No nodes are available that match all of the following predicates: MatchNode Selector, NodeNotSupportsContainer
    ```

    If  **supportContainer**  is set to  **false**, the scheduling fails. The following figure shows the error information.

    ```
    0/1 nodes are available: 1
    ```


## Check Item 4: Checking Whether the Workload's Volume and Node Reside in the Same AZ<a name="en-us_topic_0242566250_section197421559143010"></a>

Pod scheduling fails if the workload's volume and node reside in different AZs.

```
0/1 nodes are available: 1 NoVolumeZoneConflict.
```

**Solution**

In the AZ where the workload's node resides, create a new volume. Alternatively, create an identical workload and select an automatically assigned cloud storage volume.

