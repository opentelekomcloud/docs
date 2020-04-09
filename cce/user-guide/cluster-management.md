# Cluster Management<a name="cce_01_0027"></a>

-   **[Cluster Overview](cluster-overview.md)**  
The clustering technology improves performance, reliability, and flexibility at an affordable cost. Task scheduling is essential to clusters.
-   **[Cluster Lifecycle](cluster-lifecycle.md)**  
This section describes the status of each cluster lifecycle, helping you understand the running status of the cluster in different phases.
-   **[Creating a VM Cluster](creating-a-vm-cluster.md)**  
On the CCE console, you can easily create Kubernetes clusters. Kubernetes can manage container clusters at scale. A cluster manages a group of node resources.
-   **[Creating a BMS Cluster](creating-a-bms-cluster.md)**  
Bare metal server \(BMS\) clusters  are Kubernetes container clusters with high computing and high network performance. To use a BMS cluster, enable the  BMS service  first.
-   **[Upgrading a Cluster](upgrading-a-cluster.md)**  
Kubernetes versions are expressed as x.y.z, where x is the major version, y is the minor version \(for example, v1.13\), and z is the patch version. Minor releases occur approximately every 3 months to provide new features, design updates, and bug fixes, and each minor release branch is maintained for approximately 9 months. You can use the CCE console to upgrade your cluster to the latest Kubernetes version or a bug fix.
-   **[Changelog for Upgrading Clusters](changelog-for-upgrading-clusters.md)**  

-   **[Cluster Auto Scaling](cluster-auto-scaling.md)**  
The Cluster Auto Scaling feature allows CCE to automatically  scale out  a cluster \(add nodes to a cluster\) according to custom scale-up policies when workloads cannot be scheduled into the cluster due to insufficient cluster resources.
-   **[Deleting, Hibernating, and Waking Up a Cluster](deleting-hibernating-and-waking-up-a-cluster.md)**  
After a cluster is created, you can delete, hibernate, or wake up the cluster.
-   **[Obtaining a Cluster Certificate](obtaining-a-cluster-certificate.md)**  

-   **[Namespace](namespace.md)**  
A  namespace  is a collection of resources and objects. Multiple namespaces can be created in a single cluster, but they are isolated from each other. This enables namespaces to share the services of the same cluster without affecting each other.
-   **[Cluster Management Permission Control](cluster-management-permission-control.md)**  
To perform  permission control  on resources in a cluster \(for example, user A can only read and write applications in a namespace, while user B can only read resources in a cluster\), perform the operations described in this section.

