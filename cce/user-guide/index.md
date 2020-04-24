# User Guide

-   [What Is Cloud Container Engine?](what-is-cloud-container-engine.md)
-   [Product Bulletin]
    -   [Risky Operations on Cluster Nodes](risky-operations-on-cluster-nodes.md)
    -   [CCE Cluster Version Release Notes](cce-cluster-version-release-notes.md)
    -   [OS Patch Notes for Cluster Nodes](os-patch-notes-for-cluster-nodes.md)
    -   [Security Vulnerability Responses]
        -   [Notice on Fixing Linux Kernel SACK Vulnerabilities](notice-on-fixing-linux-kernel-sack-vulnerabilities.md)


-   [Cluster Management]
    -   [Cluster Overview](cluster-overview.md)
    -   [Cluster Lifecycle](cluster-lifecycle.md)
    -   [Creating a VM Cluster](creating-a-vm-cluster.md)
    -   [Creating a BMS Cluster](creating-a-bms-cluster.md)
    -   [Upgrading a Cluster](upgrading-a-cluster.md)
    -   [Changelog for Upgrading Clusters](changelog-for-upgrading-clusters.md)
    -   [Cluster Auto Scaling](cluster-auto-scaling.md)
    -   [Deleting, Hibernating, and Waking Up a Cluster](deleting-hibernating-and-waking-up-a-cluster.md)
    -   [Obtaining a Cluster Certificate](obtaining-a-cluster-certificate.md)
    -   [Namespace](namespace.md)
    -   [Cluster Management Permission Control](cluster-management-permission-control.md)

-   [Node Management]
    -   [Creating a Node](creating-a-node.md)
    -   [Logging In to a Node](logging-in-to-a-node.md)
    -   [Deleting a Node](deleting-a-node.md)
    -   [Stopping a Node](stopping-a-node.md)
    -   [Synchronizing Node Data](synchronizing-node-data.md)
    -   [Managing Node Labels](managing-node-labels.md)
    -   [Monitoring a Node](monitoring-a-node.md)
    -   [Formula for Calculating the Reserved Resources of a Node](formula-for-calculating-the-reserved-resources-of-a-node.md)

-   [Node Pool Management]
    -   [Node Pool Overview](node-pool-overview.md)
    -   [Creating a Node Pool](creating-a-node-pool.md)
    -   [Managing a Node Pool](managing-a-node-pool.md)

-   [Workload]
    -   [Overview](overview.md)
    -   [Creating a Deployment](creating-a-deployment.md)
    -   [Creating a StatefulSet](creating-a-statefulset.md)
    -   [Creating a Job](creating-a-job.md)
    -   [Creating a Cron Job](creating-a-cron-job.md)
    -   [Managing a Deployment](managing-a-deployment.md)
    -   [Managing a StatefulSet](managing-a-statefulset.md)
    -   [Scaling a Workload](scaling-a-workload.md)
    -   [Using a Third-Party Image](using-a-third-party-image.md)

-   [Advanced Container Settings]
    -   [Setting Container Specifications](setting-container-specifications.md)
    -   [Setting Container Lifecycle Parameters](setting-container-lifecycle-parameters.md)
    -   [Setting Container Startup Commands](setting-container-startup-commands.md)
    -   [Setting Health Check for a Container](setting-health-check-for-a-container.md)
    -   [Setting an Environment Variable](setting-an-environment-variable.md)
    -   [Collecting Standard Output Logs of Containers](collecting-standard-output-logs-of-containers.md)
    -   [Collecting Container Logs from Specified Paths](collecting-container-logs-from-specified-paths.md)

-   [Configuring Affinity and Anti-Affinity Scheduling]
    -   [Scheduling Policy Overview](scheduling-policy-overview.md)
    -   [Simple Scheduling Policies]
        -   [Workload-AZ Affinity](workload-az-affinity.md)
        -   [Workload-AZ Anti-Affinity](workload-az-anti-affinity.md)
        -   [Workload-Node Affinity](workload-node-affinity.md)
        -   [Workload-Node Anti-Affinity](workload-node-anti-affinity.md)
        -   [Workload-Workload Affinity](workload-workload-affinity.md)
        -   [Workload-Workload Anti-Affinity](workload-workload-anti-affinity.md)

    -   [Custom Scheduling Policies]
        -   [Node Affinity](node-affinity.md)
        -   [Pod Affinity](pod-affinity.md)
        -   [Pod Anti-Affinity](pod-anti-affinity.md)


-   [Network Management]
    -   [Network Overview](network-overview.md)
    -   [Intra-Cluster Access \(ClusterIP\)](intra-cluster-access-(clusterip).md)
    -   [NodePort](nodeport.md)
    -   [LoadBalancer](loadbalancer.md)
    -   [DNAT](dnat.md)
    -   [Layer 7 Load Balancing \(Ingress\)](layer-7-load-balancing-(ingress).md)
    -   [Network Policy](network-policy.md)

-   [Storage Management]
    -   [Storage Overview](storage-overview.md)
    -   [Using Local Disks for Storage](using-local-disks-for-storage.md)
    -   [Using EVS Disks for Storage](using-evs-disks-for-storage.md)
    -   [Using SFS File Systems for Storage](using-sfs-file-systems-for-storage.md)

-   [Template Market]
    -   [Introduction](introduction.md)
    -   [Preparing a Chart](preparing-a-chart.md)
    -   [Uploading a Chart](uploading-a-chart.md)
    -   [Creating a Workload from a Chart](creating-a-workload-from-a-chart.md)
    -   [Using an EVS Disk](using-an-evs-disk.md)
    -   [Using ELB](using-elb.md)

-   [Plug-in Management]
    -   [CoreDNS \(System Resource Add-on, Mandatory\)](coredns-(system-resource-add-on-mandatory).md)
    -   [storage-driver \(System Resource Add-on, Mandatory\)](storage-driver-(system-resource-add-on-mandatory).md)
    -   [autoscaler](autoscaler.md)
    -   [gpu-beta](gpu-beta.md)

-   [Permissions Management]
    -   [Permissions Management by IAM](permissions-management-by-iam.md)
    -   [Policy Syntax](policy-syntax.md)
    -   [Permissions Management for CCE]
        -   [Overview](overview-0.md)
        -   [Cluster-Level Permissions Management \(By Using IAM Fine-Grained Authorization\)](cluster-level-permissions-management-(by-using-iam-fine-grained-authorization).md)
        -   [Namespace-Level Permissions Management \(By Using Kubernetes RBAC Authorization\)](namespace-level-permissions-management-(by-using-kubernetes-rbac-authorization).md)

    -   [Granting IAM Users the Permissions to Access CCE]
        -   [Granting Cluster-Level Permissions \(IAM Fine-Grained Authorization\)](granting-cluster-level-permissions-(iam-fine-grained-authorization).md)
        -   [Granting Namespace-Level Permissions \(Kubernetes RBAC Authorization\)](granting-namespace-level-permissions-(kubernetes-rbac-authorization).md)


-   [Configuration Center]
    -   [Creating a ConfigMap](creating-a-configmap.md)
    -   [Using a ConfigMap](using-a-configmap.md)
    -   [Creating a Secret](creating-a-secret.md)
    -   [Using a Secret](using-a-secret.md)

-   [Image Repository]
    -   [Creating an Organization](creating-an-organization.md)
    -   [Creating an Image Repository](creating-an-image-repository.md)
    -   [Connecting to Private Container Registry](connecting-to-private-container-registry.md)
    -   [Pushing a Private Image from the Internet](pushing-a-private-image-from-the-internet.md)
    -   [Pushing a Private Image from an Intranet](pushing-a-private-image-from-an-intranet.md)
    -   [Deleting an Image Repository or Image](deleting-an-image-repository-or-image.md)
    -   [Modifying an Image Repository](modifying-an-image-repository.md)
    -   [Viewing the Address of an Image Repository](viewing-the-address-of-an-image-repository.md)
    -   [Obtaining a Long-Term Valid Docker Login Command](obtaining-a-long-term-valid-docker-login-command.md)

-   [CTS]
    -   [CCE Operations Supported by CTS](cce-operations-supported-by-cts.md)
    -   [Querying CTS Logs](querying-cts-logs.md)

-   [Using kubectl to Perform Operations on the Cluster]
    -   [kubectl Usage Guide](kubectl-usage-guide.md)
    -   [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md)
    -   [Configuring High Availability of kube-dns/CoreDNS Using kubectl](configuring-high-availability-of-kube-dns-coredns-using-kubectl.md)
    -   [Common kubectl Commands](common-kubectl-commands.md)

-   [Reference]
    -   [Creating a Linux LVM Disk Partition for Docker](creating-a-linux-lvm-disk-partition-for-docker.md)
    -   [Using Kubernetes In-Cluster DNS](using-kubernetes-in-cluster-dns.md)
    -   [How Do I Enable ICMP Security Group Rules?](how-do-i-enable-icmp-security-group-rules.md)
    -   [How Do I Add a Second Data Disk to a CCE Node?](how-do-i-add-a-second-data-disk-to-a-cce-node.md)
    -   [How Do I Troubleshoot Insufficient EIPs When a Node Is Added?](how-do-i-troubleshoot-insufficient-eips-when-a-node-is-added.md)
    -   [How Do I Format a Data Disk Using Command Line Injection?](how-do-i-format-a-data-disk-using-command-line-injection.md)
    -   [How Do I Use heapster in Clusters of v1.13.10?](how-do-i-use-heapster-in-clusters-of-v1-13-10.md)

-   [Migrating Data from CCE 1.0 to CCE 2.0]
    -   [Differences Between CCE 1.0 and CCE 2.0](differences-between-cce-1-0-and-cce-2-0.md)
    -   [Migrating Images](migrating-images.md)
    -   [Migrating Clusters](migrating-clusters.md)
    -   [Migrating Applications](migrating-applications.md)


