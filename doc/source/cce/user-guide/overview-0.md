# Overview<a name="cce_01_0187"></a>

CCE permissions management allows tenants to grant permissions to IAM users and user groups under the tenant accounts. It combines the advantages of Kubernetes Role-based Access Control \(RBAC\) authorization and Identity and Access Management \(IAM\) to provide a variety of authorization methods, including IAM fine-grained authorization, IAM token authorization, cluster-scoped authorization, and namespace-wide authorization.

CCE permissions management is classified as:

-   **Cluster-level permissions management**: On IAM, tenants can configure fine-grained policies to describe which IAM user groups can perform which operations on cluster resources. For example, tenants can grant user group A to create and delete cluster X while granting user group B to view cluster X information. Users created in IAM inherit permissions from the groups to which they belong.
-   **Namespace-level permissions management**: Tenants regulate user or user group access to Kubernetes resources in a single namespace based on their Kubernetes RBAC roles.

