# Namespace-Level Permissions Management \(By Using Kubernetes RBAC Authorization\)<a name="cce_01_0167"></a>

At its core, RBAC is a way of granting users granular access to computer or network resources based on the roles of individual users within an enterprise. The connection between user and resources is defined in RBAC using the following four objects:

-   **Role**  and  **ClusterRole**: In the RBAC API, a role contains rules that represent a set of permissions. A role can be defined within a namespace with a Role, or cluster-wide with a ClusterRole.
-   **RoleBinding**  and  **ClusterRoleBinding**: A role binding grants the permissions defined in a role to a user or set of users. It holds a list of subjects \(users, groups, or service accounts\), and a reference to the role being granted. Permissions can be granted within a namespace with a RoleBinding, or cluster-wide with a ClusterRoleBinding.

**Table  1**  Four objects declared by the RBAC API

<a name="table7143142111614"></a>
<table><thead align="left"><tr id="row1914410211164"><th class="cellrowborder" valign="top" width="30.620000000000005%" id="mcps1.2.3.1.1"><p id="p614452101611"><a name="p614452101611"></a><a name="p614452101611"></a>Type</p>
</th>
<th class="cellrowborder" valign="top" width="69.38%" id="mcps1.2.3.1.2"><p id="p12144622163"><a name="p12144622163"></a><a name="p12144622163"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1014417217164"><td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.3.1.1 "><p id="p153732040131712"><a name="p153732040131712"></a><a name="p153732040131712"></a>Role</p>
</td>
<td class="cellrowborder" valign="top" width="69.38%" headers="mcps1.2.3.1.2 "><p id="p714414221614"><a name="p714414221614"></a><a name="p714414221614"></a>A Role can only be used to grant access to resources within a single namespace.</p>
</td>
</tr>
<tr id="row2014418219161"><td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.3.1.1 "><p id="p4498748131713"><a name="p4498748131713"></a><a name="p4498748131713"></a>ClusterRole</p>
</td>
<td class="cellrowborder" valign="top" width="69.38%" headers="mcps1.2.3.1.2 "><p id="p176330155212"><a name="p176330155212"></a><a name="p176330155212"></a>A ClusterRole can be used to grant the same permissions as a Role, but because they are cluster-scoped, they can also be used to grant access to:</p>
<a name="ul11279114152116"></a><a name="ul11279114152116"></a><ul id="ul11279114152116"><li>Cluster-scoped resources (like nodes)</li><li>Non-resource endpoints (like "/healthz")</li><li>Namespaced resources (like pods) across all namespaces (needed to run <strong id="b1533423182410"><a name="b1533423182410"></a><a name="b1533423182410"></a>kubectl get pods --all-namespaces</strong>, for example)</li></ul>
</td>
</tr>
<tr id="row16145329168"><td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.3.1.1 "><p id="p13145527161"><a name="p13145527161"></a><a name="p13145527161"></a>RoleBinding</p>
</td>
<td class="cellrowborder" valign="top" width="69.38%" headers="mcps1.2.3.1.2 "><p id="p1214572201610"><a name="p1214572201610"></a><a name="p1214572201610"></a>A RoleBinding maps a Role to a subject (a user or set of users), granting that Role's permissions to those users for resources in that namespace.</p>
</td>
</tr>
<tr id="row121452211165"><td class="cellrowborder" valign="top" width="30.620000000000005%" headers="mcps1.2.3.1.1 "><p id="p81450211617"><a name="p81450211617"></a><a name="p81450211617"></a>ClusterRoleBinding</p>
</td>
<td class="cellrowborder" valign="top" width="69.38%" headers="mcps1.2.3.1.2 "><p id="p10145525168"><a name="p10145525168"></a><a name="p10145525168"></a>A ClusterRoleBinding allows users to be granted a ClusterRole for authorization across the entire cluster.</p>
</td>
</tr>
</tbody>
</table>

For more information about Kubernetes RBAC authorization, see  [Using RBAC Authorization](https://kubernetes.io/docs/admin/authorization/rbac/).

## CCE Namespace Permissions<a name="section562824112461"></a>

Tenants regulate users' or user groups' access to Kubernetes resources in a single namespace based on their Kubernetes RBAC roles.

Currently, there are three roles:  **admin**,  **edit**, and  **view**. For details, see  [Table 2](#table174765455252).

**Table  2**  User/user group roles

<a name="table174765455252"></a>
<table><thead align="left"><tr id="row19540194512257"><th class="cellrowborder" valign="top" width="34.27%" id="mcps1.2.3.1.1"><p id="p1654017455258"><a name="p1654017455258"></a><a name="p1654017455258"></a>Default ClusterRole</p>
</th>
<th class="cellrowborder" valign="top" width="65.73%" id="mcps1.2.3.1.2"><p id="p0540144517258"><a name="p0540144517258"></a><a name="p0540144517258"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row195412454251"><td class="cellrowborder" valign="top" width="34.27%" headers="mcps1.2.3.1.1 "><p id="p4541104518251"><a name="p4541104518251"></a><a name="p4541104518251"></a>admin</p>
</td>
<td class="cellrowborder" valign="top" width="65.73%" headers="mcps1.2.3.1.2 "><p id="p154117452251"><a name="p154117452251"></a><a name="p154117452251"></a>Allows admin access, intended to be granted within a namespace using a RoleBinding. If used in a RoleBinding, allows read/write access to most resources in a namespace, including the ability to create roles and role bindings within the namespace. It does not allow write access to resource quota or to the namespace itself.</p>
</td>
</tr>
<tr id="row12541445182514"><td class="cellrowborder" valign="top" width="34.27%" headers="mcps1.2.3.1.1 "><p id="p55415459252"><a name="p55415459252"></a><a name="p55415459252"></a>edit</p>
</td>
<td class="cellrowborder" valign="top" width="65.73%" headers="mcps1.2.3.1.2 "><p id="p20541545152519"><a name="p20541545152519"></a><a name="p20541545152519"></a>Allows read/write access to most objects in a namespace. It does not allow viewing or modifying roles or role bindings.</p>
</td>
</tr>
<tr id="row15541154516259"><td class="cellrowborder" valign="top" width="34.27%" headers="mcps1.2.3.1.1 "><p id="p20541194582515"><a name="p20541194582515"></a><a name="p20541194582515"></a>view</p>
</td>
<td class="cellrowborder" valign="top" width="65.73%" headers="mcps1.2.3.1.2 "><p id="p65420455258"><a name="p65420455258"></a><a name="p65420455258"></a>Allows read-only access to see most objects in a namespace. It does not allow viewing roles, role bindings, or secrets.</p>
</td>
</tr>
</tbody>
</table>

