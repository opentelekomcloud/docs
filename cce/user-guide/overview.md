# Overview<a name="cce_01_0006"></a>

A  workload  is an abstract model of a group of pods in Kubernetes. Kubernetes classify workloads into  Deployments,  StatefulSets,  DaemonSets,  jobs, and  cron jobs.

CCE provides Kubernetes-native container deployment and management and supports lifecycle management of container workloads, including creation, configuration, monitoring, capacity expansion, upgrade, uninstallation, service discovery, and load balancing.

## Basic Concepts<a name="section9568145263015"></a>

-   **Deployment**: Pods are completely independent of each other and functionally identical. They feature auto scaling and rolling upgrade. Typical examples include Nginx and WordPress. For details on how to create a deployment, see  [Creating a Deployment](creating-a-deployment.md).
-   **StatefulSet**: Pods are not completely independent of each other. They have stable persistent storage, and feature orderly deployment and deletion. Typical examples include MySQL-HA and etcd. For details on how to create a StatefulSet, see  [Creating a StatefulSet](creating-a-statefulset.md).
-   **DaemonSet**:  A DaemonSet ensures that all or some nodes run a pod. It is applicable to pods running on every node. Typical examples include Ceph, Fluentd, and Prometheus Node Exporter. For details about how to create a DaemonSet, see  [Creating a DaemonSet](creating-a-daemonset.md).
-   **Job**: A job is a resource object that Kubernetes uses to control tasks in batches.

    A job is different from a long-term servo workload \(such as Deployment and StatefulSet\). The former is started and terminated at specific times, while the latter runs unceasingly unless being terminated. The pods managed by a job automatically exit after successfully completing the job based on user configurations. The success flag varies according to the spec.completions policy.

    -   One-off jobs: A single pod runs once until successful termination.
    -   Jobs with a fixed success count: N pods run until successful termination.
    -   Queue jobs: Queue jobs are considered successful based on the global success confirmed by the application.

    For details about how to create a job, see  [Creating a Job](creating-a-job.md).

-   **Cron job**: A cron job runs periodically at the specified time. It is similar to Linux crontab. A cron job has the following characteristics:

    -   Runs only once at the specified time.
    -   Runs periodically at the specified time.

    The typical usage of a cron job is as follows:

    -   Schedules jobs at the specified time.
    -   Creates jobs to run periodically, for example, database backup and email sending.

    For details about how to create a cron job, see  [Creating a Cron Job](creating-a-cron-job.md).


## Relationship Between Workloads and Containers<a name="section16194164519394"></a>

As shown in  [Figure 1](#fig1801862479), a workload controls one or more instances \(pods\). A pod consists of one or more containers. Each container is created from a container image. Pods of Deployments are exactly the same.

**Figure  1**  Relationship between workloads and containers<a name="fig1801862479"></a>  
![](figures/relationship-between-workloads-and-containers.png "relationship-between-workloads-and-containers")

## Workload Lifecycle<a name="section3891192610218"></a>

**Table  1**  Status description

<a name="table488465253420"></a>
<table><thead align="left"><tr id="row13888105212343"><th class="cellrowborder" valign="top" width="25%" id="mcps1.2.3.1.1"><p id="p1788975203415"><a name="p1788975203415"></a><a name="p1788975203415"></a>Status</p>
</th>
<th class="cellrowborder" valign="top" width="75%" id="mcps1.2.3.1.2"><p id="p788975211347"><a name="p788975211347"></a><a name="p788975211347"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row14889152173415"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1788905212343"><a name="p1788905212343"></a><a name="p1788905212343"></a>Running</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p188914522345"><a name="p188914522345"></a><a name="p188914522345"></a>All pods are running.</p>
</td>
</tr>
<tr id="row12889195263417"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p1888915253412"><a name="p1888915253412"></a><a name="p1888915253412"></a>Unready</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p12889152113418"><a name="p12889152113418"></a><a name="p12889152113418"></a>All containers are in the pending state.</p>
</td>
</tr>
<tr id="row12889195213419"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p6889135218347"><a name="p6889135218347"></a><a name="p6889135218347"></a>Updating</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p18889052203414"><a name="p18889052203414"></a><a name="p18889052203414"></a>After the upgrade operation is triggered, the workload is being upgraded.</p>
</td>
</tr>
<tr id="row2088975211346"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p788915203415"><a name="p788915203415"></a><a name="p788915203415"></a>Stopped</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p15889152103417"><a name="p15889152103417"></a><a name="p15889152103417"></a>After the stop operation is triggered, the workload is stopped and the number of pods changes to 0.</p>
</td>
</tr>
<tr id="row172011222121114"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p132017221115"><a name="p132017221115"></a><a name="p132017221115"></a>Available</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p16202132212113"><a name="p16202132212113"></a><a name="p16202132212113"></a>For a multi-pod Deployment, some pods are abnormal but at least one pod is available.</p>
</td>
</tr>
<tr id="row1280465420481"><td class="cellrowborder" valign="top" width="25%" headers="mcps1.2.3.1.1 "><p id="p198052054104811"><a name="p198052054104811"></a><a name="p198052054104811"></a>Deleting</p>
</td>
<td class="cellrowborder" valign="top" width="75%" headers="mcps1.2.3.1.2 "><p id="p8805854104812"><a name="p8805854104812"></a><a name="p8805854104812"></a>After the delete operation is triggered, the workload is being deleted.</p>
</td>
</tr>
</tbody>
</table>

