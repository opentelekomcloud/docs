# Why is a message displayed indicating that the key pair does not exist and the operation is discontinued when several users under the same account operate AS resources?<a name="EN-US_TOPIC_0207619375"></a>

A key pair cannot be used by multiple users. If the key pair of another user under the same account is configured in the AS configuration, the AS configuration cannot be used to manually provision resources.

If users need to perform operations on others' AS configuration resources without being restricted by the key pair permission, use password authentication for instances.

