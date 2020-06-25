# Can MRS Cluster Nodes Be Changed on the MRS Management Console?<a name="EN-US_TOPIC_0125375209"></a>

MRS cluster nodes cannot be changed on the MRS management console. You are not advised to change MRS cluster nodes on the ECS management console either. If you manually stop or delete the ECS, modify or reinstall the ECS OS, or modify the ECS specifications for a cluster node on the ECS management console, the cluster may work improperly.

If you have performed any of the preceding operations, MRS automatically identifies and deletes the involved cluster node. You can substitute the deleted node by expanding the capacity of the cluster on the MRS management console. Do not perform any operation on a node during capacity expansion.

