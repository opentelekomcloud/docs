# Introduction<a name="EN-US_TOPIC_0125376089"></a>

## Definition<a name="section65052095201233"></a>

An MRS cluster provides various resources and services for multiple organizations, departments, or applications to share. The cluster provides tenants as a logical entity to use these resources and services. A mode involving different tenants is called multi-tenant mode. Currently, tenants are supported by analysis clusters only.

## Principles<a name="section3120380020134"></a>

The MRS cluster provides the multi-tenant function. It supports a layered tenant model and allows dynamic adding or deleting of tenants to isolate resources. It dynamically manages and configures tenants' computing and storage resources.

The computing resources indicate tenants' Yarn task queue resources. The task queue quota can be modified, and the task queue usage status and statistics can be viewed.

Storage resources support HDFS storage. Tenants' HDFS storage directories can be added or deleted, and the quotas for file quantity and storage space of the directories can be configured.

As the unified tenant management platform of the MRS cluster, MRS Manager provides a mature multi-tenant management model for enterprises, implementing centralized tenant and service management. Users can create and manage tenants in the cluster.

-   Roles, computing resources, and storage resources are automatically created when tenants are created. By default, all rights on the new computing and storage resources are assigned to the tenant roles.
-   By default, the permission to view tenant resources, create sub-tenants, and manage sub-tenant resources is assigned to the tenant roles.
-   After tenants' computing or storage resources are modified, the related role rights are updated automatically.

MRS Manager supports a maximum of 512 tenants. The tenants that are created by default in the system contain  **default**. Tenants that are in the topmost layer with the default tenant are called level-1 tenants.

## Resource Pool<a name="section2620495520142"></a>

Yarn task queues support only the label-based scheduling policy. This policy enables Yarn task queues to associate with NodeManagers that have specific node labels. In this way, Yarn tasks run on specified nodes for scheduling and certain hardware resources are utilized. For example, Yarn tasks requiring a large memory capacity can run on nodes with a large memory capacity by means of label association, preventing poor service performance.

On the MRS cluster, users can logically divide Yarn cluster nodes to combine multiple NodeManagers into a resource pool. Yarn task queues can be associated with specified resource pools by configuring queue capacity policies, ensuring efficient and independent resource utilization in the resource pools.

MRS Manager supports a maximum of 50 resource pools. The system has a  **Default**  resource pool.

