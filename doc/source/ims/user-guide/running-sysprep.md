# Running Sysprep<a name="EN-US_TOPIC_0093887081"></a>

## Scenarios<a name="section12143031154614"></a>

Running Sysprep ensures that an ECS has a unique SID after it is added to a domain.

After installing Cloudbase-Init on an ECS, you need to decide whether the ECS needs to be added to a domain or whether it must have a unique SID. If yes, run  Sysprep  as instructed in this section.

## Prerequisites<a name="section1180712252202"></a>

-   Run Sysprep as the administrator.
-   For a newly activated Windows ECS, you can run Sysprep only once at a time.
-   If an ECS is created from an image file, only Sysprep provided by the image file can be used. In addition, Sysprep must always reside in the  **%WINDIR%\\system32\\sysprep**  directory.
-   Windows must be in the activated state, and the remaining Windows rearm count must be greater than or equal to 1. Otherwise, the Sysprep encapsulation cannot be executed.

    Run the following command in the Windows command line and check how many times you can run Sysprep in the displayed  **Windows Script Host**  dialog box:

    **slmgr.vbs /dlv**

    If the value of  **Remaining Windows rearm count**  is  **0**, you cannot run Sysprep.

    **Figure  1**  Windows Script Host<a name="fig6211922154010"></a>  
    ![](figures/windows-script-host.png "windows-script-host")


## Procedure<a name="section52239395104045"></a>

1.  Enter the Cloudbase-Init installation directory.

    **C:\\Program Files\\Cloudbase Solutions\\**  is used as an example of the Cloudbase-Init installation directory. Switch to the root directory of drive C and run the following command to enter the installation directory:

    **cd C:\\Program Files\\Cloudbase Solutions\\Cloudbase-Init\\conf**

2.  Run the following command to encapsulate Windows:

    **C:\\Windows\\System32\\sysprep\\sysprep.exe /generalize /oobe /unattend:Unattend.xml**

    >![](/images/icon-notice.gif) **NOTICE:**   
    >-   Ensure that  **/unattend:Unattend.xml**  is contained in the preceding command. Otherwise, the username, password, and other important configuration information of the ECS will be reset, and you must configure the OS manually when you use ECSs created using the Windows private image.  
    >-   After this command is executed, the ECS will be automatically stopped. After the ECS is stopped, use the ECS to create an image. ECSs created using the image have unique SIDs. If you restart a Windows ECS on which Sysprep has been executed, Sysprep takes effect only for the current ECS. Before creating an image using the ECS, you must run Sysprep again.  
    >-   For Windows Server 2012 and Windows Server 2012 R2, the administrator password of the ECS will be deleted after Sysprep is executed on the ECS. You need to log in to the ECS and reset the administrator password. In this case, the administrator password set on the management console will be invalid. Keep the password you set secure.  
    >-   If a domain account is required for logins, run Sysprep on the ECS before using it to create a private image. For details about the impact of running Sysprep, see  [Why Is Sysprep Required for Creating a Private Image from a Windows ECS?](why-is-sysprep-required-for-creating-a-private-image-from-a-windows-ecs.md).  
    >-   The Cloudbase-Init account of a Windows ECS is an internal account of the Cloudbase-Init agent. This account is used for obtaining metadata and completing relevant configuration when the Windows ECS starts. If you modify or delete this account, or uninstall the Cloudbase-Init agent, you will be unable to inject initial custom information into an ECS created from a Windows private image. Therefore, you are not advised to modify or delete the Cloudbase-Init account.  

    **Figure  2**  Running Sysprep<a name="fig6590344163610"></a>  
    ![](figures/running-sysprep.png "running-sysprep")


## Follow-up Operations<a name="section539192915492"></a>

1.  Create a private image from the ECS on which Sysprep is executed. For details, see  [Creating a System Disk Image from a Windows ECS](creating-a-system-disk-image-from-a-windows-ecs.md).
2.  You can use the image to create ECSs. Each ECS has a unique SID.

    Run the following command to query the ECS SID:

    **whoami /user**

    **Figure  3**  ECS SID before Sysprep is executed<a name="fig1442820462495"></a>  
    ![](figures/ecs-sid-before-sysprep-is-executed.png "ecs-sid-before-sysprep-is-executed")

    **Figure  4**  ECS SID after Sysprep is executed<a name="fig1428124614493"></a>  
    ![](figures/ecs-sid-after-sysprep-is-executed.png "ecs-sid-after-sysprep-is-executed")


