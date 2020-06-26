# Locking a User<a name="EN-US_TOPIC_0125375506"></a>

## Scenario<a name="sd55f590aa6754544aea116cdf256b660"></a>

This section describes how to lock users in MRS clusters. A locked user cannot log in to MRS Manager or perform security authentication in the cluster. You have obtained a cluster with Kerberos authentication enabled or a normal cluster with the EIP function enabled.

A locked user can be unlocked by an administrator manually or until the lock duration expires. You can lock a user by using either of the following methods:

-   Automatic lock: Set  **Number of Password Retries** in **Configure Password Policy**. If user login attempts exceed the parameter value, the user is automatically locked. For details, see [Modifying a Password Policy](modifying-a-password-policy.md).
-   Manual lock: The administrator manually locks a user.

The following describes how to manually lock a user.  **Machine-machine**  users cannot be locked.

## Procedure<a name="s91cb4fbb29684126b15bd0519b9df8f2"></a>

1.  On MRS Manager, click  **System**.
2.  In the  **Permission** area, click **Manage User**.
3.  In the row of a user you want to lock,  click **Lock User**.
4.  In the window that is displayed, click  **OK**  to lock the user.

