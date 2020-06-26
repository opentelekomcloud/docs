# Cloud-Init<a name="EN-US_TOPIC_0048642616"></a>

Cloud-Init is an open-source cloud initialization program, which initializes specified customized configurations, such as the hostname, key pair, and user data, of a newly created ECS.

All standard \(Standard\_xxx\) and enterprise \(Enterprise\_xxx\) images support Cloud-Init. Only certain community images \(Community\_xxx\) do not support it.

Using Cloud-Init to initialize your ECSs will affect your ECS, IMS, and AS services.

## Impact on IMS<a name="section1150469610136"></a>

To ensure that ECSs created using private images support customized configurations, you must install Cloud-Init or Cloudbase-Init before creating private images.

-   For Windows OSs, download and install Cloudbase-Init.
-   For Linux OSs, download and install Cloud-Init.

After Cloud-Init or Cloudbase-Init is installed in an image, Cloud-Init or Cloudbase-Init automatically configures initial ECS attributes when the ECS is created.

For instructions about the installation, see  _Image Management Service User Guide_.

## Impact on ECS<a name="section2746706105950"></a>

-   When creating an ECS, if the selected image supports Cloud-Init, you can use user data injection to inject customized configuration, such as ECS login password, for initializing. For details, see  [Injecting User Data into ECSs](injecting-user-data-into-ecss.md).
-   After Cloud-Init is supported, ECSs do not support password authentication any more. All newly created ECSs use key pair authentication. This change will influence your ECS logins. For details, see the following sections:
    -   [Login Overview](login-overview-(linux).md)
    -   [What Is the cloudbase-init Account in Windows ECSs?](what-is-the-cloudbase-init-account-in-windows-ecss.md)
    -   [Why Was My Login to a Linux ECS Using a Key File Unsuccessful?](why-was-my-login-to-a-linux-ecs-using-a-key-file-unsuccessful.md)
    -   [Why Does the System Display a Message Indicating that the Password for Logging In to a Windows ECS Cannot Be Viewed?](why-does-the-system-display-a-message-indicating-that-the-password-for-logging-in-to-a-windows-ecs-c.md)

-   After Cloud-Init is supported, you can view and use metadata to configure and manage running ECSs. For more information, see  [Obtaining Metadata](obtaining-metadata.md).

## Impact on AS<a name="section4202207210118"></a>

-   When creating an AS configuration, you can use user data injection to specify ECS configurations for initialization. If the AS configuration has taken effect in an AS group, the ECSs newly created in the AS group will automatically initialize their configurations.
-   For an existing AS configuration, if its private image does not have Cloud-Init or Cloudbase-Init installed, the login mode of the ECSs created in the AS group where the AS configuration takes effect will be affected.

    To resolve this issue, see "How Does Cloud-Init Influence the AS Service?" in  _Auto Scaling User Guide_.


## Notes<a name="section44995720162019"></a>

-   When using Cloud-Init, enable DHCP in the VPC to which the ECS belongs.
-   When using Cloud-Init, ensure that security group rules in the outbound direction meet the following requirements:

    -   **Protocol**:  **TCP**
    -   **Port Range**:  **80**
    -   **Remote End**:  **169.254.0.0/16**

    >![](/images/icon-note.gif) **NOTE:**   
    >If you use the default security group rules in the outbound direction, the preceding requirements are met, and the metadata can be accessed. Default security group rules in the outbound direction are as follows:  
    >-   **Protocol**:  **ANY**  
    >-   **Port Range**:  **ANY**  
    >-   **Remote End**:  **0.0.0.0/0**  


