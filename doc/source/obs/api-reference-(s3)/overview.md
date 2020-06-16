# Overview<a name="EN-US_TOPIC_0125560328"></a>

Buckets or objects that are created by a user belong to the user's domain. By default, only users in the domain can access the buckets or objects. In this policy you can control permission access to requested resources \(buckets or objects\). OBS uses the access control list \(ACL\) and bucket policy to manage permission.

-   ACL: specifies an account's permission to access resources. Each entry in an ACL grants specific permission to a specific account. ACLs apply to accounts but not accounts' users. You can use an ACL to grant but not to deny permission.
-   Bucket policy: controls one or multiple users' or accounts' permission to access buckets or bucket objects. You can use a bucket policy to grant or deny permission. A bucket policy applies to both accounts and users. If a user receives the returned code  **200**  when configuring a bucket policy, it indicates that the user is authorized with the permission for bucket policy configuration. If the code  **405**  is returned, it indicates that the user does not have the permission to configure the bucket policy.

