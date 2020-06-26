# Fine-grained Policy<a name="iam_01_019"></a>

A fine-grained policy is a set of permissions defining which operations on which cloud services can be performed. Each policy can define multiple permission sets. After a policy is granted to a user group, users in the user group obtain the permissions of the policy. IAM implements fine-grained permission management based on the permissions defined by policies.

IAM supports two types of policies:

-   Default policies: define the common permissions preset in the system, which are typically read-only or management permission for different cloud services such as ECS. Default policies can be used only for authorization and cannot be edited or modified.
-   Custom policies: define the permissions created and managed by users and are the extension and supplement of default policies.

