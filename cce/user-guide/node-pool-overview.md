# Node Pool Overview<a name="cce_01_0081"></a>

This section describes how node pools work in CCE and how to create and manage node pools.

## Introduction<a name="section11993204511284"></a>

A node pool is a group of one or more nodes with identical configuration in a cluster.

In CCE, the nodes configured during cluster creation are grouped into the default node pool. The default node pool is named  **DefaultPool**  and cannot be edited, deleted, or migrated.

On the CCE console, you can create custom node pools in a cluster to organize cluster nodes into different pools so that you can edit or delete a node pool individually without affecting the entire cluster. All nodes in a custom node pool have identical parameters and node type. You cannot configure a single node in a node pool; any configuration changes affect all nodes in the node pool. For details on how to control scheduling of workload pods onto nodes, see  [Scheduling Policy Overview](scheduling-policy-overview.md).

## Deploying a Workload on a Specified Node Pool<a name="section12603142443319"></a>

When creating a workload, you can constrain pods to run in a specified node pool.

**nodeSelector**  is the simplest recommended form of node selection constraint.  **nodeSelector**  is a field in pod YAML files and specifies a map of key-value pairs. For the pod to be eligible to run on a node, the node must have each of the indicated key-value pairs as labels. To specify  **nodeSelector**  for pods of a workload, choose  **Workloads**  in the navigation pane of the CCE console and choose  **More**  \>  **Edit YAML**  in the same row as the workload.

For example, you can use container's resource request as a nodeSelector so that pods will run only on the nodes that meet the resource request. If the pod definition file defines a container that requires four CPUs, the scheduler will not choose the nodes with two CPUs to run pods.

## Nodes in a Multi-AZ Cluster<a name="section17716744163316"></a>

If you create a multi-AZ cluster, all node pools in the cluster will be automatically created in these AZs. Similarly, if you delete a node pool in an AZ, the node pool is also deleted from other AZs.

