# Step 1: Configure Basic Settings<a name="EN-US_TOPIC_0163572589"></a>

## Switching to the Create ECS Page<a name="section636471910536"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Elastic Cloud Server**.
4.  Click  **Create ECS**.

    The page for creating ECSs is displayed.

    >![](/images/icon-note.gif) **NOTE:**   
    >SAP High-Performance Analytic Appliance \(HANA\) is a high-performance real-time data computing platform based on memory computing technologies. The public cloud provides high-performance IaaS services that comply with SAP HANA requirements. These services help users rapidly request for SAP HANA resources \(such as applying for HANA ECSs and public IP addresses\) and install and configure SAP HANA, therefore improving user operation efficiency, reducing operation costs, and enhancing user experience.  
    >HANA ECSs are dedicated for SAP HANA. If you want to deploy SAP HANA on cloud servers, create HANA ECSs.  
    >For more information about HANA ECS application scenarios and creation methods, see  _SAP HANA User Guide_.  


## Performing Basic Configurations<a name="section4570625145413"></a>

1.  Select an AZ.

    An AZ is a physical region where power and networks are physically isolated. AZs in the same region can communicate with each other over an intranet.

    -   To enhance application availability, create ECSs in different AZs.
    -   To shorten network latency, create ECSs in the same AZ.

2.  Set  **DeH**.

    This configuration is optional. This parameter is available only when you click  **Create ECS**  on the  **Dedicated Host**  page. It is unavailable when you click  **Create ECS**  on the  **Elastic Cloud Server**  page.

    DeH refers to physical host resources dedicated for a specified user. You can deploy ECSs on DeHs for better isolation, security, and performance of your ECSs. You can continue using your existing server software licenses of ECSs on DeHs to reduce costs. For more details, see  _Dedicated Host User Guide_.

3.  Set  **Specifications**.

    The public cloud provides various ECS types for different application scenarios. You can view released ECS types and flavors in the list. Alternatively, you can enter a flavor \(such as  **c3**\) or specify vCPUs and memory size to search for the desired flavor.

    **Latest generation**  shows the types and flavors of newly released ECSs, and  **All generations**  show the types and flavors of all ECSs provided by the public cloud.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Before selecting an ECS type, learn the introduction and notes on each type of ECSs. For details, see  [ECS Types](ecs-types.md).  
    >-   **Local Disk**: specifies the local storage of the physical host where the ECS is deployed. Only Hard Disk Driver \(HDD\) disks are supported. If the ECS of the selected type \(such as  **Disk-intensive**\) uses local disks, the system automatically attaches the local disks to the ECS and displays the information of the local disks.  
    >    For example, if  **Local Disk**  is  **3x1,800 GB \(HDD\)**, three HDDs are attached to the ECS and the capacity of each HDD is 1800 GB.  

4.  Select an image.
    -   Public image

        A public image is a standard, widely used image. It contains an OS and preinstalled public applications and is available to all users. You can configure the applications or software in the public image as needed.

        For more information about public images, see  _[Public Images Introduction](https://docs.otc.t-systems.com/en-us/ims/index.html)_.

    -   Private image

        A private image is an image available only to the user who created it. It contains an OS, preinstalled public applications, and the user's private applications. Using a private image to create ECSs removes the need to configure multiple ECSs repeatedly.

        You can also select an encrypted image. For details, see  _Image Management Service User Guide_.

        >![](/images/icon-note.gif) **NOTE:**   
        >-   If you use a full-ECS image to create an ECS, the EVS disks associated with the full-ECS image do not support the function of creating disks using a data disk image.  
        >-   If a full-ECS image is in  **Normal**  state and the system displays message "Available in AZ_x_", the full-ECS image can be used to create ECSs in this AZ only, and the encryption attributes of the system and data disks of the created ECSs are the same as those of the system and data disks specified in the full-ECS image. Additionally, the SCSI, sharing attribute, and data encryption settings of the system and data disks cannot be modified during ECS creation.  
        >-   If a full-ECS image is in  **Normal**  state but the system does not display message "Available in AZ_x_", the full-ECS image can be used to create ECSs in the entire region, and the encryption attributes of the system and data disks of the created ECSs are the same as those of the system and data disks specified in the full-ECS image. Additionally, the SCSI, sharing attribute, and data encryption settings of data disks can be modified during ECS creation.  
        >-   For more details about how to use CSBS backups to create images, see "Using Backups to Create Images" in  _Cloud Server Backup Service User Guide_  and "Creating a Full-ECS Image Using a CSBS Backup" in  _Image Management Service User Guide_.  
        >-   To ensure that NIC multi-queue is enabled on an ECS created using a private image, configure NIC multi-queue when creating such a private image. NIC multi-queue routes NIC interrupt requests among multiple vCPUs for higher network PPS and bandwidth.  
        >    For details, see "How Do I Set NIC Multi-Queue Feature of an Image?"  

    -   Shared image

        A shared image is a private image shared by another user.

    -   Marketplace image

        Marketplace images are high-quality third-party images that have OSs, application environments, and software preinstalled. You can use the images to deploy websites and application development environments with a few clicks, and no additional configuration operation is required. Marketplace images support only yearly/monthly and pay-per-use ECSs.

        If you use a Marketplace image, after you click  **Marketplace image**, the system displays Marketplace images for you to select. For example, if the image product is  **name1 \(test\_001\)**,  **name1**  is the image name, and  **test\_001**  is the product name. You can search for your desired Marketplace image by image name or product name. Alternatively, you can click the image name to view more information about the image. For more information about Marketplace images, see  [Marketplace User Guide \(for Tenants](https://docs.otc.t-systems.com/en-us/marketplace/index.html).

5.  \(Optional\) Set  **License Type**.

    Specifies a license type for using an OS or software. This parameter is displayed only when the selected image is billed.

    -   Using License from the System

        Allows you to use the license provided by the public cloud platform. Obtaining the authorization of such a license is billed.

    -   Bring your own license \(BYOL\)

        Allows you to use your existing OS license. In such a case, you do not need to apply for a license again.

    For more details, see  [License Type](license-type.md).

6.  Set  **System Disk**, and  **Data Disk**  if required.
    -   System disk

        For the disk types supported by an ECS, see  [EVS Disks](evs-disks.md).

        -   If the image based on which an ECS is created is not encrypted, the system disk of the ECS is not encrypted. If the image based on which an ECS is created is encrypted, the system disk of the ECS is automatically encrypted. For details, see  [•  \(Optional\) Encryption-rela...](#en-us_topic_0144542112_li3286101316615).
        -   For a P1 or P2 ECS, the system disk must be greater than or equal to 15 GB. It is recommended that the system disk be greater than 40 GB. A disk size must be an integer multiple of 10, for example, 60 GB or 70 GB. Otherwise, the system automatically rounds the value down, for example, 60 GB for value  **68**.

    -   Data disk

        You can create multiple data disks for an ECS and enable sharing and encryption for each data disk. When creating an ECS, you can add up to 24 disks with customized sizes to it. After the ECS is created, you can add up to 60 disks to such a newly created ECS.

        -   **SCSI**: indicates that the device type of the data disk is SCSI. For more information about SCSI disks and the ECSs that can be attached with SCSI disks, see  [EVS Disks](evs-disks.md).
        -   **Share**: indicates that the EVS disk is sharable. Such an EVS disk can be attached to multiple ECSs.
        -   **Encryption**: indicates that the data disk is encrypted. For details, see  [•  \(Optional\) Encryption-rela...](#en-us_topic_0144542112_li3286101316615).

    -   <a name="en-us_topic_0144542112_li3286101316615"></a>\(Optional\) Encryption-related parameters

        To enable encryption, click  **Create Xrole**  to grant KMS access rights to EVS. If you have rights granting permission, grant the KMS access rights to EVS. If you do not have the permission, contact the user having the security administrator rights to grant the KMS access rights. For more details, see  [Who Can Use the Encryption Feature?](who-can-use-the-encryption-feature.md)

        -   **Encrypted**: indicates that the EVS disk has been encrypted.
        -   **Create Xrole**: grants KMS access rights to EVS to obtain KMS keys. After the rights are granted, follow-up operations do not require granting rights again.
        -   **KMS Key Name**: specifies the name of the key used by the encrypted EVS disk. By default, the name is  **evs/default**.
        -   **Xrole Name: EVSAccessKMS**: specifies that rights have been granted to EVS to obtain KMS keys for encrypting or decrypting EVS disks.
        -   **KMS Key ID**: specifies the ID of the key used by the encrypted data disk.

7.  Click  **Next: Configure Network**.

