# User Guide

-   [What Is Cloud Container Engine?](what-is-cloud-container-engine.md)
-   [Instruction](instruction.md)
-   [Product Bulletin]
    -   [Risky Operations on Cluster Nodes](risky-operations-on-cluster-nodes.md)
    -   [CCE Cluster Version Release Notes](cce-cluster-version-release-notes.md)
    -   [OS Patch Notes for Cluster Nodes](os-patch-notes-for-cluster-nodes.md)
    -   [Security Vulnerability Responses]
        -   [Notice on Fixing Linux Kernel SACK Vulnerabilities](notice-on-fixing-linux-kernel-sack-vulnerabilities.md)


-   [Cluster Management]
    -   [Cluster Overview](cluster-overview.md)
    -   [Cluster Lifecycle](cluster-lifecycle.md)
    -   [Creating a Hybrid Cluster](creating-a-hybrid-cluster.md)
    -   [Creating a BMS Cluster](creating-a-bms-cluster.md)
    -   [Upgrading a Cluster](upgrading-a-cluster.md)
    -   [Changelog for Upgrading Clusters](changelog-for-upgrading-clusters.md)
    -   [Cluster Auto Scaling](cluster-auto-scaling.md)
    -   [Deleting, Hibernating, and Waking Up a Cluster](deleting-hibernating-and-waking-up-a-cluster.md)
    -   [Configuration Management](configuration-management.md)
    -   [Obtaining a Cluster Certificate](obtaining-a-cluster-certificate.md)
    -   [Namespace](namespace.md)
    -   [Cluster Management Permission Control](cluster-management-permission-control.md)

-   [Node Management]
    -   [Creating a Node](creating-a-node.md)
    -   [Logging In to a Node](logging-in-to-a-node.md)
    -   [Deleting a Node](deleting-a-node.md)
    -   [Stopping a Node](stopping-a-node.md)
    -   [Synchronizing Node Data](synchronizing-node-data.md)
    -   [Resetting a Node](resetting-a-node.md)
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
    -   [Creating a DaemonSet](creating-a-daemonset.md)
    -   [Creating a Job](creating-a-job.md)
    -   [Creating a Cron Job](creating-a-cron-job.md)
    -   [Managing a Deployment](managing-a-deployment.md)
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
    -   [Simple Scheduling Policies](simple-scheduling-policies.md)
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
    -   [Overview](overview-01.md)
    -   [Using Local Disks for Storage](using-local-disks-for-storage.md)
    -   [Using EVS Disks for Storage](using-evs-disks-for-storage.md)
    -   [Using SFS File Systems for Storage](using-sfs-file-systems-for-storage.md)
    -   [Snapshot and backup](snapshot-and-backup.md)

-   [Charts]
    -   [Introduction](introduction.md)
    -   [Preparing a Chart](preparing-a-chart.md)
    -   [Uploading a Chart](uploading-a-chart.md)
    -   [Creating a Workload from a Chart](creating-a-workload-from-a-chart.md)
    -   [Using an EVS Disk](using-an-evs-disk.md)
    -   [Using ELB](using-elb.md)

-   [Add-ons]
    -   [CoreDNS \(System Resource Add-on, Mandatory\)](coredns-(system-resource-add-on-mandatory).md)
    -   [storage-driver \(System Resource Add-on, Mandatory\)](storage-driver-(system-resource-add-on-mandatory).md)
    -   [everest \(System Resource Add-on, Mandatory\)](everest-(system-resource-add-on-mandatory).md)
    -   [autoscaler](autoscaler.md)
    -   [metrics-server](metrics-server.md)
    -   [gpu-beta](gpu-beta.md)

-   [Auto Scaling]
    -   [Scaling a Workload](scaling-a-workload-01.md)
    -   [Scaling a Node](scaling-a-node.md)

-   [Permissions Management]
    -   [Permissions Management by IAM](permissions-management-by-iam.md)
    -   [Policy Syntax](policy-syntax.md)
    -   [Permissions Management for CCE]
        -   [Overview](overview-02.md)
        -   [Cluster-Level Permissions Management \(By Using IAM Fine-Grained Authorization\)](cluster-level-permissions-management-(by-using-iam-fine-grained-authorization).md)
        -   [Namespace-Level Permissions Management \(By Using Kubernetes RBAC Authorization\)](namespace-level-permissions-management-(by-using-kubernetes-rbac-authorization).md)

    -   [Granting IAM Users the Permissions to Access CCE]
        -   [Granting Cluster-Level Permissions \(IAM Fine-Grained Authorization\)](granting-cluster-level-permissions-(iam-fine-grained-authorization).md)
        -   [Granting Namespace-Level Permissions \(Kubernetes RBAC Authorization\)](granting-namespace-level-permissions-(kubernetes-rbac-authorization).md)


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

-   [Configuration Center]
    -   [Creating a ConfigMap](creating-a-configmap.md)
    -   [Using a ConfigMap](using-a-configmap.md)
    -   [Creating a Secret](creating-a-secret.md)
    -   [Using a Secret](using-a-secret.md)

-   [CTS]
    -   [CCE Operations Supported by CTS](cce-operations-supported-by-cts.md)
    -   [Querying CTS Logs](querying-cts-logs.md)

-   [Using kubectl to Perform Operations on the Cluster]
    -   [kubectl Usage Guide](kubectl-usage-guide.md)
    -   [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md)
    -   [Configuring High Availability of kube-dns/CoreDNS Using kubectl](configuring-high-availability-of-kube-dns-coredns-using-kubectl.md)
    -   [Common kubectl Commands](common-kubectl-commands.md)

-   [Reference]
    -   [Checklist for Migrating Containerized Applications to the Cloud](checklist-for-migrating-containerized-applications-to-the-cloud.md)
    -   [Creating a Linux LVM Disk Partition for Docker](creating-a-linux-lvm-disk-partition-for-docker.md)
    -   [Using Kubernetes In-Cluster DNS](using-kubernetes-in-cluster-dns.md)
    -   [How Do I Enable ICMP Security Group Rules?](how-do-i-enable-icmp-security-group-rules.md)
    -   [How Do I Troubleshoot Insufficient EIPs When a Node Is Added?](how-do-i-troubleshoot-insufficient-eips-when-a-node-is-added.md)
    -   [How Do I Format a Data Disk Using Command Line Injection?](how-do-i-format-a-data-disk-using-command-line-injection.md)
    -   [How Do I Use heapster in Clusters of v1.13.10?](how-do-i-use-heapster-in-clusters-of-v1-13-10.md)
    -   [How Do I Change the Mode of the Docker Device Mapper?](how-do-i-change-the-mode-of-the-docker-device-mapper.md)
    -   [How Do I Use kubectl to Set the Workload Access Type to LoadBalancer \(ELB\)?](how-do-i-use-kubectl-to-set-the-workload-access-type-to-loadbalancer-(elb).md)
    -   [How Do I Select a Network Model When Creating a CCE Cluster? What Are the Differences Between These Models?](how-do-i-select-a-network-model-when-creating-a-cce-cluster-what-are-the-differences-between-these-m.md)
    -   [Which CIDR Blocks Does CCE Support?](which-cidr-blocks-does-cce-support.md)
    -   [How Do I Add a Second Data Disk to a Node in a CCE Cluster?](how-do-i-add-a-second-data-disk-to-a-node-in-a-cce-cluster.md)
    -   [Workload Abnormalities]
        -   [Fault Locating and Troubleshooting for Abnormal Workloads](fault-locating-and-troubleshooting-for-abnormal-workloads.md)
        -   [Failed to Schedule an Instance](failed-to-schedule-an-instance.md)
        -   [Failed to Pull an Image](failed-to-pull-an-image.md)
        -   [Failed to Restart a Container](failed-to-restart-a-container.md)
        -   [What Should I Do If An Evicted Pod Exists?](what-should-i-do-if-an-evicted-pod-exists.md)
        -   [Instance Eviction Exception](instance-eviction-exception.md)
        -   [What Should I Do If Pods in the Terminating State Cannot Be Deleted?](what-should-i-do-if-pods-in-the-terminating-state-cannot-be-deleted.md)
        -   [What Should I Do If a Workload Is Stopped Caused by Pod Deletion?](what-should-i-do-if-a-workload-is-stopped-caused-by-pod-deletion.md)
        -   [What Should I Do If Sandbox-Related Errors Are Reported When the Pod Remains in the Creating State?](what-should-i-do-if-sandbox-related-errors-are-reported-when-the-pod-remains-in-the-creating-state.md)
        -   [What Should I Do If a Pod Is in the Evicted State?](what-should-i-do-if-a-pod-is-in-the-evicted-state.md)
        -   [What Should I Do If the OOM Killer Is Triggered When a Container Uses Memory Resources More Than Limited?](what-should-i-do-if-the-oom-killer-is-triggered-when-a-container-uses-memory-resources-more-than-lim.md)

    -   [What Should I Do If a Service Released in a Workload Cannot Be Accessed from Public Networks?](what-should-i-do-if-a-service-released-in-a-workload-cannot-be-accessed-from-public-networks.md)

-   [Migrating Data from CCE 1.0 to CCE 2.0]
    -   [Differences Between CCE 1.0 and CCE 2.0](differences-between-cce-1-0-and-cce-2-0.md)
    -   [Migrating Images](migrating-images.md)
    -   [Migrating Clusters](migrating-clusters.md)
    -   [Migrating Applications](migrating-applications.md)


