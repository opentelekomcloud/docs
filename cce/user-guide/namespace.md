# Namespace<a name="cce_01_0030"></a>

A  namespace  is a collection of resources and objects. Multiple namespaces can be created in a single cluster, but they are isolated from each other. This enables namespaces to share the services of the same cluster without affecting each other.

For example, you can deploy workloads in a development environment into one namespace, and deploy workloads in a test environment into another namespace.

## Prerequisites<a name="section812825881312"></a>

At least one cluster is created. For details, see  [Creating a Hybrid Cluster](creating-a-hybrid-cluster.md).

## Constraints<a name="section21791218165310"></a>

A maximum of 6,000 services can be created in each namespace. The services mentioned here indicate the Kubernetes service resources added for workloads.

## Namespace Types<a name="section15162183815147"></a>

Namespaces can be created automatically or manually.

-   Namespaces created automatically: When a cluster is up, the  **default**,  **kube-public**, and  **kube-system**  namespaces are created by default.
    -   **default**: used if no namespace is specified.
    -   **kube-public**: used for deploying public add-ons and container templates.
    -   **kube-system**: used for deploying Kubernetes system components.

-   Namespaces created manually: You can create namespaces to serve separate purposes. For example, you can create three namespaces, one for a development environment, one for joint debugging environment, and one for test environment. You can also create one namespace for login services and one for game services.

## Creating a Namespace<a name="section452221655718"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Namespaces**, and click  **Create Namespace**.
2.  Set the parameters listed in  [Table 1](#table5523151617575). The parameters marked with an asterisk \(\*\) are mandatory.

    **Table  1**  Parameters for creating a namespace

    <a name="table5523151617575"></a>
    <table><thead align="left"><tr id="row145240162572"><th class="cellrowborder" valign="top" width="27.99%" id="mcps1.2.3.1.1"><p id="p105244162578"><a name="p105244162578"></a><a name="p105244162578"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="72.00999999999999%" id="mcps1.2.3.1.2"><p id="p14525016155719"><a name="p14525016155719"></a><a name="p14525016155719"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row835519426223"><td class="cellrowborder" valign="top" width="27.99%" headers="mcps1.2.3.1.1 "><p id="p1964374702211"><a name="p1964374702211"></a><a name="p1964374702211"></a>* Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p14644047132219"><a name="p14644047132219"></a><a name="p14644047132219"></a>Name of the namespace, which must be unique in a cluster.</p>
    </td>
    </tr>
    <tr id="row1326175714265"><td class="cellrowborder" valign="top" width="27.99%" headers="mcps1.2.3.1.1 "><p id="p102613574265"><a name="p102613574265"></a><a name="p102613574265"></a>* Cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p1226957152615"><a name="p1226957152615"></a><a name="p1226957152615"></a>Cluster to which the namespace belongs.</p>
    </td>
    </tr>
    <tr id="row62811035135114"><td class="cellrowborder" valign="top" width="27.99%" headers="mcps1.2.3.1.1 "><p id="p828263519510"><a name="p828263519510"></a><a name="p828263519510"></a>Node Affinity</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p6726725115313"><a name="p6726725115313"></a><a name="p6726725115313"></a>If this parameter is set to on, workloads in the current namespace will be scheduled only to nodes with specified labels. To add labels to a node, choose <strong id="b37268259533"><a name="b37268259533"></a><a name="b37268259533"></a>Resource Management</strong> &gt; <strong id="b172612595316"><a name="b172612595316"></a><a name="b172612595316"></a>Nodes</strong> &gt; <strong id="b0726225185311"><a name="b0726225185311"></a><a name="b0726225185311"></a>Manage Labels</strong>.</p>
    </td>
    </tr>
    <tr id="row75251516185711"><td class="cellrowborder" valign="top" width="27.99%" headers="mcps1.2.3.1.1 "><p id="p19525016125713"><a name="p19525016125713"></a><a name="p19525016125713"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p1452519163573"><a name="p1452519163573"></a><a name="p1452519163573"></a>Description of the namespace.</p>
    </td>
    </tr>
    <tr id="row18506114684111"><td class="cellrowborder" valign="top" width="27.99%" headers="mcps1.2.3.1.1 "><p id="p7506164613417"><a name="p7506164613417"></a><a name="p7506164613417"></a>Set Resource Quotas</p>
    </td>
    <td class="cellrowborder" valign="top" width="72.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p10506204644111"><a name="p10506204644111"></a><a name="p10506204644111"></a>Set resource quotas to limit resource usage in the namespace, thereby organizing resources into different namespaces.</p>
    <div class="notice" id="note9166152113399"><a name="note9166152113399"></a><a name="note9166152113399"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p2167521123914"><a name="p2167521123914"></a><a name="p2167521123914"></a>It is recommended to assign a pod quota to each namespace. Without a pod quota, clusters or nodes may soon run out of system resources and exhibit unexpected behavior when too many pods are created. The pod quotas of all namespaces in a cluster must not exceed 110 (maximum pods per node) multiplied by the quantity of nodes in a cluster. For example, in a cluster of 50 nodes, a maximum of 5,500 (110 * 50) pods can be created. This means that pod quotas of all namespaces in the cluster should not exceed 5,500.</p>
    </div></div>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **OK**.

## Using Namespaces<a name="section5992104316274"></a>

1.  When you create a workload, select a namespace for it.
2.  When you query workloads, select a namespace to view all workloads in the namespace.

## Namespace Application Scenarios<a name="section10225104442820"></a>

-   **Dividing workloads into namespaces by environment type**

    Before being released, a workload generally goes through the phases of development, joint debugging, testing, and production. In this process, the workloads of different environments are logically defined but are basically the same. There are two methods:

    -   Creating clusters for different environments:

        Resources cannot be shared among different clusters. A load balancer is required in order to enable mutual access between services in different environments.

    -   Creating namespaces in the same cluster for different environments:

        Workloads in the same namespace access each other using service names, while workloads in different namespaces access each other using service names and namespace names.

        [Figure 1](#fig741584216524)  shows namespaces respectively created for the development, joint debugging, and testing environments.

        **Figure  1**  Dividing workloads into namespaces by environment types<a name="fig741584216524"></a>  
        ![](figures/dividing-workloads-into-namespaces-by-environment-types.png "dividing-workloads-into-namespaces-by-environment-types")


-   **Dividing workloads into namespaces by application**

    You are advised to use this method if a large number of workloads are deployed in the same environment. As shown in the following figure, different namespaces are created for App 1 and App 2. Workloads in a namespace are managed as a workload group. Workloads in the same namespace access each other using service names, while workloads in different namespaces access each other using service names and namespace names.

    **Figure  2**  Dividing workloads into namespaces by workload type<a name="fig11187114614422"></a>  
    ![](figures/dividing-workloads-into-namespaces-by-workload-type.png "dividing-workloads-into-namespaces-by-workload-type")


## Configuring a Namespace-level Network Policy<a name="section1462011111016"></a>

You can configure a namespace-level network policy by enabling network isolation.

By default,  **Network Isolation**  is disabled for  namespaces. For example, if network isolation is off for namespace  **default**,  **all pods in the current cluster**  can access the  **pods** **in** **namespace** **default**.

To prevent other pods from accessing the pods in namespace  **default**, perform the following steps:

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Namespaces**.
2.  In the same row as the namespace \(for example,  **default**\) for which you will create a network policy, enable network isolation

    After network isolation is enabled, pods in namespace  **default**  can access each other but they cannot be accessed by pods in other namespaces.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >After a network isolated namespace is whitelisted \(see  [Creating a Network Policy](network-policy.md#section19894131402011)\) network isolation may be broken down.

    **Figure  3**  Namespace-level network policy<a name="en-us_topic_0113320781_fig13427151918417"></a>  
    ![](figures/namespace-level-network-policy.png "namespace-level-network-policy")


## Configuring Namespace-level Resource Quotas<a name="section73511074518"></a>

Namespace-level resource quotas limit the total numbers of resources that can be used when multiple teams or users share cluster resources. The quotas include the total number of a type of objects and the total amount of compute resources \(CPU and memory\) consumed by the objects.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>This function is supported only when the cluster version is 1.9 or later.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Namespaces**.
2.  In the  **Operation**  column of a namespace, click  **Manage Quota**.

    This operation cannot be performed on system namespaces  **kube-system**  and  **kube-public**.

3.  Set the following resource quotas and click  **OK**:

    -   **CPU \(cores\)**: maximum number of CPU cores that can be allocated to workload pods in the namespace.
    -   **Memory \(MiB\)**: maximum amount of memory that can be allocated to workload pods in the namespace.
    -   **StatefulSet**: maximum number of StatefuSets that can be created in the namespace.
    -   **Deployment**: maximum number of deployments that can be created under the namespace.
    -   **Job**: maximum number of one-off jobs that can be created under the namespace.
    -   **CronJob**: maximum number of Cron jobs that can be created under the namespace.
    -   **Pod**: maximum number of instances that can be created under the namespace.
    -   **Service**: maximum number of services that can be created under the namespace.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:** 
    >-   After setting CPU and memory quotas for a namespace, you must specify the request and limit values of CPU and memory resources when creating a workload. Otherwise, the workload cannot be created. If the quota of a resource is set to  **0**, no limit is posed on the resource.
    >-   Accumulated quota usage includes the default resources created by CCE, such as the kubernetes service \(view this service using the kubectl tool\) created under the  **default**  namespace. Therefore, you are advised to set a resource quota greater than what you expect.


## Deleting Namespaces<a name="section175251816125710"></a>

If a namespace is deleted, all resources \(such as workloads, jobs, and ConfigMaps\) in this namespace will be also deleted. Exercise caution when deleting a namespace.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Namespaces**.
2.  In the  **Clusters**  drop-down list, select the cluster where the namespace to be deleted is located.
3.  Select the namespace to be deleted and click  **Delete**.

    Follow the prompts to delete it. The built-in namespaces of the system cannot be deleted.


