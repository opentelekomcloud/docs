# Step 3: Configure Advanced Settings<a name="EN-US_TOPIC_0163572591"></a>

## Advanced Settings<a name="section127442165919"></a>

1.  Set  **ECS Name**.

    The name can be customized but must comply with the following naming rules: Can contain only letters, digits, underscores \(\_\), hyphens \(-\), and periods \(.\).

    If you want to create multiple ECSs at a time, the system automatically sequences these ECSs.

2.  \(Optional\) Specify the description of the ECS.
3.  Set  **Login Mode**.

    **Key pair**: allows you to use a key pair for login authentication. You can select an existing key pair, or click  **Create Key Pair**  and create a desired one.

    >![](/images/icon-note.gif) **NOTE:**   
    >If you use an existing key pair, make sure that you have saved the key file locally. Otherwise, logging in to the ECS will fail.  

4.  Set  **ECS Group**.

    An ECS group applies the anti-affinity policy to the ECSs in it so that the ECSs are automatically allocated to different hosts. This configuration is optional. For instructions about how to create an ECS group, see  [Managing ECS Groups](managing-ecs-groups.md).

    >![](/images/icon-note.gif) **NOTE:**   
    >An existing ECS attached with a local disk cannot be added to an ECS group. To use ECS group functions, select an ECS group when creating an ECS.  

5.  To use functions listed in  **Advanced Options**, select  **Configure now**. Otherwise, do not select it.
    -   File Injection

        Enables the ECS to automatically inject a script file or other files into a specified directory on an ECS when you create the ECS. This configuration is optional.

        For example, if you activate user  **root**  permission using script file injection, you can log in to the ECS as user  **root**.

        For details about file injection, see  [Injecting Files into ECSs](injecting-files-into-ecss.md).

    -   User Data Injection

        Enables the ECS to automatically inject user data when the ECS starts for the first time. This configuration is optional.

        For example, if you activate user  **root**  permission using script data injection, you can log in to the ECS as user  **root**.

        For detailed operations, see  [Injecting User Data into ECSs](injecting-user-data-into-ecss.md).

    -   Tag

        Tags an ECS, facilitating ECS identification and management. This configuration is optional. You can add up to 10 tags to an ECS.

        >![](/images/icon-note.gif) **NOTE:**   
        >Tags added during ECS creation will also be added to the created EIP and EVS disks \(including the system disk and data disks\) of the ECS. If the ECS uses an existing EIP, the tags will not be added to the EIP.  
        >After creating the ECS, you can view the tags on the pages providing details about the ECS, EIP, and EVS disks.  

        For detailed operations, see  [Overview](tag-management-overview.md).

    -   Agency

        This configuration is optional. When your ECS resources need to be shared with other accounts, or your ECS is delegated to professional personnel or team for management, the tenant administrator creates an agency in IAM and grants the ECS management permissions to the personnel or team. The delegated account can log in to the cloud system and switch to your account to manage resources. You do not need to share security credentials \(such as passwords\) with other accounts, ensuring the security of your account.

        If you have created an agency in IAM, you can select the agency from the drop-down list and obtain specified operation permissions. For instructions about how to create an agency, see  _Identity and Access Management User Guide_.

6.  Click  **Next: Confirm**.

