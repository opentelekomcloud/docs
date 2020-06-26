# Resetting the Administrator Password<a name="en-us_topic_reset_password"></a>

## **Scenarios**<a name="section52938762133842"></a>

You can  reset the administrator password  only through the primary DB instance.

If you forget the password of your database account when using RDS, you can reset the password.

You cannot reset the administrator password under the following circumstances:

-   The database port is being changed.
-   The status of the primary DB instance is  **Creating**,  **Restoring**,  **Rebooting**,  **Storage full**,  **Changing port**, or  **Abnormal**.

## Precautions<a name="section5252821142215"></a>

-   If you have changed the administrator password of the primary DB instance, the administrator passwords of the standby DB instance and read replica \(if any\) will also be changed accordingly.
-   The length of time it takes for the new password to take effect depends on the amount of service data currently being processed by the primary DB instance.
-   To prevent brute force cracking and ensure system security, change your password periodically.

## Method 1<a name="section59807924105129"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, locate the target DB instance and choose  **More**  \>  **Reset Password**  in the  **Operation**  column.
5.  Enter a new password and confirm the password.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >Keep this password secure. The system cannot retrieve it.  

    The new password must consist of 8 to 32 characters and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters \(\~!@\#%^\*-\_+?,\). Enter a strong password and periodically change it to improve security, preventing security risks such as brute force cracking.

    -   To submit the new password, click  **OK**.
    -   To cancel the reset operation, click  **Cancel**.


## Method 2<a name="section4206283114638"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  In the  **DB Information**  area on the  **Basic Information**  page, click  **Reset Password**  in the  **Administrator**  field.
6.  Enter a new password and confirm the password.

    >![](/images/icon-notice.gif) **NOTICE:**   
    >Keep this password secure. The system cannot retrieve it.  

    The new password must consist of 8 to 32 characters and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters \(\~!@\#%^\*-\_+?,\). Enter a strong password and periodically change it to improve security, preventing security risks such as brute force cracking.

    -   To submit the new password, click  **OK**.
    -   To cancel the reset operation, click  **Cancel**.


