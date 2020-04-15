# How Can I Set the Validity Period of the Image Password?<a name="EN-US_TOPIC_0079176727"></a>

If an ECS cannot be logged in because of expired image password, you can contact the administrator for handling.

If the ECS can still be logged in, you can perform the following operations to set the password validity period.

## Procedure<a name="section3242177619526"></a>

The following operations use EulerOS 2.2 as an example.

1.  Log in to the ECS.
2.  Run the following command to check the password validity period:

    **vi /etc/login.defs**

    The value of parameter  **PASS\_MAX\_DAYS**  is the password validity period.

3.  Run the following command to change the value of parameter  **PASS\_MAX\_DAYS**:

    **chage -M** _99999 user\_name_

    _99999_  is the password validity period, and  _user\_name_  is the system user, for example, user  **root**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You are advised to configure the password validity period as needed and change it at a regular basis.  

4.  Run command  **vi /etc/login.defs**  to verify that the configuration has taken effect.

    **Figure  1**  Configuration verification<a name="fig36880073194742"></a>  
    ![](figures/configuration-verification.png "configuration-verification")


