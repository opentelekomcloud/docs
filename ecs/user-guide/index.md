# Elastic Cloud Server User Guide

-   [Service Overview]
    -   [What Is ECS?](what-is-ecs.md)
    -   [Instances]
        -   [Overview](overview.md)
        -   [ECS Lifecycle](ecs-lifecycle.md)
        -   [ECS Types](ecs-types.md)
        -   [ECS Specifications ](ecs-specifications.md)
        -   [General-Purpose ECSs](general-purpose-ecss.md)
        -   [Dedicated General-Purpose ECSs](dedicated-general-purpose-ecss.md)
        -   [Memory-optimized ECSs](memory-optimized-ecss.md)
        -   [Large-Memory ECSs](large-memory-ecss.md)
        -   [Disk-intensive ECSs](disk-intensive-ecss.md)
        -   [High-Performance Computing ECSs](high-performance-computing-ecss.md)
        -   [GPU-accelerated ECSs](gpu-accelerated-ecss.md)

    -   [Images](images-(service-overview).md)
    -   [EVS Disks](evs-disks.md)
    -   [Network](network.md)
    -   [Security]
        -   [User Encryption](user-encryption.md)
        -   [Cloud-Init](cloud-init.md)
        -   [License Type](license-type.md)
        -   [Project](project.md)

    -   [User Permissions](user-permissions.md)
    -   [Region and AZ](region-and-az.md)
    -   [ECS and Other Services](ecs-and-other-services.md)

-   [Getting Started]
    -   [Creating an ECS]
        -   [Overview](overview-(creating-an-ecs).md)
        -   [Step 1: Configure Basic Settings](step-1-configure-basic-settings.md)
        -   [Step 2: Configure Network](step-2-configure-network.md)
        -   [Step 3: Configure Advanced Settings](step-3-configure-advanced-settings.md)
        -   [Step 4: Confirm](step-4-confirm.md)

    -   [Logging In to an ECS](logging-in-to-an-ecs.md)
    -   [Initializing EVS Data Disks]
        -   [Scenarios and Disk Partitions](scenarios-and-disk-partitions.md)
        -   [Initializing a Windows Data Disk \(Windows Server 2008\)](initializing-a-windows-data-disk-(windows-server-2008).md)
        -   [Initializing a Windows Data Disk \(Windows Server 2016\)](initializing-a-windows-data-disk-(windows-server-2016).md)
        -   [Initializing a Linux Data Disk \(fdisk\)](initializing-a-linux-data-disk-(fdisk).md)
        -   [Initializing a Linux Data Disk \(parted\)](initializing-a-linux-data-disk-(parted).md)


-   [Instances]
    -   [Viewing ECS Information]
        -   [Viewing ECS Creation Statuses](viewing-ecs-creation-statuses.md)
        -   [Viewing Failures](viewing-failures.md)
        -   [Viewing Details About an ECS](viewing-details-about-an-ecs.md)
        -   [Exporting ECS Information](exporting-ecs-information.md)

    -   [Logging In to a Windows ECS]
        -   [Login Overview](login-overview-(windows).md)
        -   [Login Using VNC](login-using-vnc-(windows).md)
        -   [Login Using MSTSC](login-using-mstsc.md)

    -   [Logging In to a Linux ECS]
        -   [Login Overview](login-overview-(linux).md)
        -   [Login Using VNC](login-using-vnc-(linux).md)
        -   [Login Using an SSH Key](login-using-an-ssh-key.md)
        -   [Login Using an SSH Password](login-using-an-ssh-password.md)

    -   [Managing ECSs]
        -   [Changing an ECS Name](changing-an-ecs-name.md)
        -   [Reinstalling the OS](reinstalling-the-os.md)
        -   [Changing the OS](changing-the-os.md)
        -   [Managing ECS Groups](managing-ecs-groups.md)
        -   [Backing Up ECS Data](backing-up-ecs-data.md)
        -   [Changing the Time Zone for an ECS](changing-the-time-zone-for-an-ecs.md)
        -   [Obtaining ECS Console Logs](obtaining-ecs-console-logs.md)

    -   [Modifying ECS vCPU and Memory Specifications]
        -   [General Operations for Modifying Specifications](general-operations-for-modifying-specifications.md)
        -   [Changing a General-Purpose ECS to an H1 ECS](changing-a-general-purpose-ecs-to-an-h1-ecs.md)
        -   [Changing a Xen ECS to a KVM ECS \(Windows\)](changing-a-xen-ecs-to-a-kvm-ecs-(windows).md)
        -   [Automatically Changing a Xen ECS to a KVM ECS \(Linux\)](automatically-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md)
        -   [Manually Changing a Xen ECS to a KVM ECS \(Linux\)](manually-changing-a-xen-ecs-to-a-kvm-ecs-(linux).md)

    -   [Migrating an ECS](migrating-an-ecs.md)
    -   [Using User Data and Metadata]
        -   [Obtaining Metadata](obtaining-metadata.md)
        -   [Injecting User Data into ECSs](injecting-user-data-into-ecss.md)
        -   [Injecting Files into ECSs](injecting-files-into-ecss.md)

    -   [\(Optional\) Configuring Mapping Between Hostnames and IP Addresses]((optional)-configuring-mapping-between-hostnames-and-ip-addresses.md)
    -   [\(Optional\) Installing a Driver and Toolkit]
        -   [Installing a GRID/vGPU Driver on a GPU-accelerated ECS](installing-a-grid-vgpu-driver-on-a-gpu-accelerated-ecs.md)
        -   [Obtaining a NVIDIA GPU Driver and CUDA Toolkit](obtaining-a-nvidia-gpu-driver-and-cuda-toolkit.md)
        -   [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2v ECS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p2v-ecs.md)
        -   [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2 ECS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p2-ecs.md)
        -   [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P1 ECS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p1-ecs.md)


-   [Images]
    -   [Overview](images-overview.md)
    -   [Creating an Image](creating-an-image.md)

-   [EVS Disks]
    -   [Attaching an EVS Disk to an ECS](attaching-an-evs-disk-to-an-ecs.md)
    -   [Detaching an EVS Disk from a Running ECS](detaching-an-evs-disk-from-a-running-ecs.md)
    -   [Expanding the Capacity of an EVS Disk](expanding-the-capacity-of-an-evs-disk.md)
    -   [Expanding the Local Disks of a Disk-intensive ECS](expanding-the-local-disks-of-a-disk-intensive-ecs.md)
    -   [Enabling Advanced Disk](enabling-advanced-disk.md)

-   [Passwords and Key Pairs]
    -   [Changing the Login Password on an ECS](changing-the-login-password-on-an-ecs.md)
    -   [Resetting a Login Password]
        -   [Resetting the Password for Logging In to a Windows ECS](resetting-the-password-for-logging-in-to-a-windows-ecs.md)
        -   [Resetting the Password for Logging In to a Linux ECS](resetting-the-password-for-logging-in-to-a-linux-ecs.md)

    -   [Creating a Key Pair](creating-a-key-pair.md)
    -   [Obtaining the Password for Logging In to a Windows ECS](obtaining-the-password-for-logging-in-to-a-windows-ecs.md)
    -   [Deleting the Initial Password for Logging In to a Windows ECS](deleting-the-initial-password-for-logging-in-to-a-windows-ecs.md)

-   [NICs]
    -   [Adding a NIC](adding-a-nic.md)
    -   [Deleting a NIC](deleting-a-nic.md)
    -   [Modifying a Private IP Address](modifying-a-private-ip-address.md)
    -   [Managing Virtual IP Addresses](managing-virtual-ip-addresses.md)
    -   [Enabling NIC Multi-Queue](enabling-nic-multi-queue.md)

-   [Security]
    -   [Security Groups]
        -   [Overview](security-groups-overview.md)
        -   [Default Security Group and Rules](default-security-group-and-rules.md)
        -   [Security Group Configuration Examples](security-group-configuration-examples.md)
        -   [Configuring Security Group Rules](configuring-security-group-rules.md)
        -   [Changing a Security Group](changing-a-security-group.md)


-   [EIPs]
    -   [Binding an EIP](binding-an-eip.md)
    -   [Changing an EIP Bandwidth](changing-an-eip-bandwidth.md)
    -   [Having an ECS Without a Public IP Address Access the Internet](having-an-ecs-without-a-public-ip-address-access-the-internet.md)

-   [Resources and Tags]
    -   [Tag Management]
        -   [Overview](tag-management-overview.md)
        -   [Adding Tags](adding-tags.md)
        -   [Searching for Resources by Tag](searching-for-resources-by-tag.md)
        -   [Deleting a Tag](deleting-a-tag.md)

    -   [Quota Adjustment](quota-adjustment.md)

-   [Monitoring]
    -   [Monitoring ECSs](monitoring-ecss.md)
    -   [Basic ECS Metrics](basic-ecs-metrics.md)
    -   [Setting Alarm Rules](setting-alarm-rules.md)
    -   [Viewing ECS Metrics](viewing-ecs-metrics.md)

-   [CTS]
    -   [Viewing Tracing Logs](viewing-tracing-logs.md)

-   [Troubleshooting]
    -   [What Can I Do If Switching from a Non-root User to User root Times Out?](what-can-i-do-if-switching-from-a-non-root-user-to-user-root-times-out.md)
    -   [What Should I Do If Error "command ´gcc´ failed with exit status 1" Occurs During PIP-based Software Installation](what-should-i-do-if-error-command-gcc-failed-with-exit-status-1-occurs-during-pip-based-software-ins.md)
    -   [What Should I Do If Packages Are Downloaded Using PIP or wget at a Low Rate?](what-should-i-do-if-packages-are-downloaded-using-pip-or-wget-at-a-low-rate.md)
    -   [How Can I Handle Slow ECS Startup?](how-can-i-handle-slow-ecs-startup.md)

-   [FAQs]
    -   [Product Consultation]
        -   [What Restrictions Apply to ECSs?](what-restrictions-apply-to-ecss.md)
        -   [What Can I Do with ECSs?](what-can-i-do-with-ecss.md)

    -   [Creation and Deletion]
        -   [Why Does the Failures Area Show an ECS Creation Failure But the ECS List Displays the Created ECS?](why-does-the-failures-area-show-an-ecs-creation-failure-but-the-ecs-list-displays-the-created-ecs.md)
        -   [What Should I Do If It Is Slow to Create ECSs Using a Full-ECS Image?](what-should-i-do-if-it-is-slow-to-create-ecss-using-a-full-ecs-image.md)
        -   [How Long Does It Take to Obtain an ECS?](how-long-does-it-take-to-obtain-an-ecs.md)
        -   [What Functions Does the Delete Button Provide?](what-functions-does-the-delete-button-provide.md)
        -   [Can a Deleted ECS Be Provisioned Again?](can-a-deleted-ecs-be-provisioned-again.md)
        -   [What Should I Do When an ECS Remains in the Restarting or Stopping State for a Long Time?](what-should-i-do-when-an-ecs-remains-in-the-restarting-or-stopping-state-for-a-long-time.md)

    -   [Login and Connection]
        -   [Why Are Characters Entered Through VNC Still Incorrect After the Keyboard Language Is Switched?](why-are-characters-entered-through-vnc-still-incorrect-after-the-keyboard-language-is-switched.md)
        -   [Why Cannot I Use the German Keyboard to Enter Characters After I Log In to an ECS Using VNC?](why-cannot-i-use-the-german-keyboard-to-enter-characters-after-i-log-in-to-an-ecs-using-vnc.md)
        -   [Why Cannot I Use the MAC Keyboard to Enter Lowercase Characters After I Log In to an ECS Using VNC?](why-cannot-i-use-the-mac-keyboard-to-enter-lowercase-characters-after-i-log-in-to-an-ecs-using-vnc.md)
        -   [What Should I Do If the Page Does not Respond After I Log In to an ECS Using VNC and Do Not Perform Any Operation for a Long Period of Time?](what-should-i-do-if-the-page-does-not-respond-after-i-log-in-to-an-ecs-using-vnc-and-do-not-perform.md)
        -   [What Should I Do If I Cannot View Data After Logging In to an ECS Using VNC?](what-should-i-do-if-i-cannot-view-data-after-logging-in-to-an-ecs-using-vnc.md)
        -   [Why Does a Blank Screen Appear While the System Displays a Message Indicating Successful Authentication After I Attempted to Log In to an ECS Using VNC?](why-does-a-blank-screen-appear-while-the-system-displays-a-message-indicating-successful-authenticat.md)
        -   [What Should I Do If I Cannot Log In to an ECS with Cloud-Init Enabled?](what-should-i-do-if-i-cannot-log-in-to-an-ecs-with-cloud-init-enabled.md)
        -   [What Browser Version Is Required to Remotely Log In to an ECS?](what-browser-version-is-required-to-remotely-log-in-to-an-ecs.md)
        -   [How Can I Log In to an ECS After Its System Disk Is Exchanged with That Attached to Another ECS Running the Same OS? ](how-can-i-log-in-to-an-ecs-after-its-system-disk-is-exchanged-with-that-attached-to-another-ecs-runn.md)
        -   [Why Does the System Display a Message Indicating that the Password for Logging In to a Windows ECS Cannot Be Viewed?](why-does-the-system-display-a-message-indicating-that-the-password-for-logging-in-to-a-windows-ecs-c.md)
        -   [What Should I Do If an Authentication Failure Occurs After I Attempt to Remotely Log In to a Windows ECS?](what-should-i-do-if-an-authentication-failure-occurs-after-i-attempt-to-remotely-log-in-to-a-windows.md)
        -   [What Should I Do If the System Displays Error Code 0x112f When I Log In to a Windows ECS?](what-should-i-do-if-the-system-displays-error-code-0x112f-when-i-log-in-to-a-windows-ecs.md)

    -   [ECS Management]
        -   [How Can a Changed Static Hostname Take Effect Permanently?](how-can-a-changed-static-hostname-take-effect-permanently.md)
        -   [Is an ECS Hostname with Suffix .novalocal Normal?](is-an-ecs-hostname-with-suffix-novalocal-normal.md)
        -   [What Should I Do If Executing a Driver Installation Script Failed on an ECS Running CentOS 5?](what-should-i-do-if-executing-a-driver-installation-script-failed-on-an-ecs-running-centos-5.md)
        -   [What Should I Do If Executing a Driver Installation Script Failed When I Attempted to Modify the Specifications of a Linux ECS?](what-should-i-do-if-executing-a-driver-installation-script-failed-when-i-attempted-to-modify-the-spe.md)
        -   [What Should I Do If the Data Disk of a Windows ECS Becomes Offline After the ECS Specifications Are Modified?](what-should-i-do-if-the-data-disk-of-a-windows-ecs-becomes-offline-after-the-ecs-specifications-are.md)
        -   [What Should I Do If the Disk of a Linux ECS Becomes Offline After the ECS Specifications Are Modified?](what-should-i-do-if-the-disk-of-a-linux-ecs-becomes-offline-after-the-ecs-specifications-are-modifie.md)
        -   [How Do I Handle Error Messages Displayed on the Management Console?](how-do-i-handle-error-messages-displayed-on-the-management-console.md)
        -   [Why Does the System Display a Question Mark When I Attempt to Obtain Console Logs?](why-does-the-system-display-a-question-mark-when-i-attempt-to-obtain-console-logs.md)

    -   [OS Management]
        -   [Can I Install or Upgrade the OS by Myself?](can-i-install-or-upgrade-the-os-by-myself.md)
        -   [Can the OS of an ECS Be Changed?](can-the-os-of-an-ecs-be-changed.md)
        -   [Can I Select Another OS During ECS OS Reinstallation?](can-i-select-another-os-during-ecs-os-reinstallation.md)
        -   [Do ECSs Support GUI?](do-ecss-support-gui.md)

    -   [File Uploading]
        -   [Does an ECS Support FTP-based Uploading by Default?](does-an-ecs-support-ftp-based-uploading-by-default.md)

    -   [Application Migration]
        -   [Can I Transfer ECS Ownership Between Accounts?](can-i-transfer-ecs-ownership-between-accounts.md)

    -   [Disk Management]
        -   [How Can I Adjust System Disk Partitions?](how-can-i-adjust-system-disk-partitions.md)
        -   [How Can I Obtain the Mapping Between Disk Partitions and Disk Devices on a Windows ECS?](how-can-i-obtain-the-mapping-between-disk-partitions-and-disk-devices-on-a-windows-ecs.md)
        -   [How Can I Obtain the Mapping Between Disk Partitions and Disk Devices on a Linux ECS?](how-can-i-obtain-the-mapping-between-disk-partitions-and-disk-devices-on-a-linux-ecs.md)
        -   [How Can I Enable Virtual Memory on a Windows ECS?](how-can-i-enable-virtual-memory-on-a-windows-ecs.md)
        -   [Why Is the Memory of an ECS Obtained by Running the free Command Inconsistent with the Actual Memory?](why-is-the-memory-of-an-ecs-obtained-by-running-the-free-command-inconsistent-with-the-actual-memory.md)
        -   [How Can I Add the Empty Partition of an Expanded System Disk to the End Root Partition Online?](how-can-i-add-the-empty-partition-of-an-expanded-system-disk-to-the-end-root-partition-online.md)
        -   [How Can I Add the Empty Partition of an Expanded System Disk to the Non-end Root Partition Online?](how-can-i-add-the-empty-partition-of-an-expanded-system-disk-to-the-non-end-root-partition-online.md)
        -   [Can Multiple Disks Be Attached to an ECS?](can-multiple-disks-be-attached-to-an-ecs.md)
        -   [What Are the Restrictions on Attaching an EVS Disk to an ECS?](what-are-the-restrictions-on-attaching-an-evs-disk-to-an-ecs.md)
        -   [Which ECSs Can Be Attached with SCSI EVS Disks?](which-ecss-can-be-attached-with-scsi-evs-disks.md)
        -   [What Is the Mapping Between Device Names and Disks?](what-is-the-mapping-between-device-names-and-disks.md)
        -   [How Can I Attach a Snapshot-based System Disk to an ECS as Its Data Disk?](how-can-i-attach-a-snapshot-based-system-disk-to-an-ecs-as-its-data-disk.md)
        -   [What Should I Do If a Linux ECS with a SCSI Disk Attached Fails to Restart?](what-should-i-do-if-a-linux-ecs-with-a-scsi-disk-attached-fails-to-restart.md)
        -   [Who Can Use the Encryption Feature?](who-can-use-the-encryption-feature.md)
        -   [What Should I Do If a Disk Is Offline?](what-should-i-do-if-a-disk-is-offline.md)
        -   [How Can I Obtain Data Disk Information If Tools Are Deleted?](how-can-i-obtain-data-disk-information-if-tools-are-deleted.md)
        -   [How Can I Rectify the Fault That May Occur on a Linux ECS with an NVMe SSD Disk Attached?](how-can-i-rectify-the-fault-that-may-occur-on-a-linux-ecs-with-an-nvme-ssd-disk-attached.md)

    -   [Passwords and Key Pairs]
        -   [How Can I Set the Validity Period of the Image Password?](how-can-i-set-the-validity-period-of-the-image-password.md)
        -   [How Can I Obtain the Key Pair Used by an ECS?](how-can-i-obtain-the-key-pair-used-by-an-ecs.md)
        -   [What Should I Do If a Key Pair Cannot Be Imported?](what-should-i-do-if-a-key-pair-cannot-be-imported.md)
        -   [Why Was My Login to a Linux ECS Using a Key File Unsuccessful?](why-was-my-login-to-a-linux-ecs-using-a-key-file-unsuccessful.md)
        -   [What Should I Do If a Key Pair Created Using puttygen.exe Cannot Be Imported to the Management Console?](what-should-i-do-if-a-key-pair-created-using-puttygen-exe-cannot-be-imported-to-the-management-conso.md)
        -   [What Is the cloudbase-init Account in Windows ECSs?](what-is-the-cloudbase-init-account-in-windows-ecss.md)
        -   [What Should I Do If Cloud-Init Does Not Work After Python Is Upgraded?](what-should-i-do-if-cloud-init-does-not-work-after-python-is-upgraded.md)

    -   [Network Configurations]
        -   [Can Multiple EIPs Be Bound to an ECS?](can-multiple-eips-be-bound-to-an-ecs.md)
        -   [Can an ECS Without an EIP Access the Internet?](can-an-ecs-without-an-eip-access-the-internet.md)
        -   [Why Can I Remotely Access an ECS But Cannot Ping It?](why-can-i-remotely-access-an-ecs-but-cannot-ping-it.md)
        -   [Will NICs Added to an ECS Start Automatically?](will-nics-added-to-an-ecs-start-automatically.md)
        -   [How Can I Check Whether the Network Communication Between Two ECSs Equipped with an InfiniBand NIC Driver Is Normal?](how-can-i-check-whether-the-network-communication-between-two-ecss-equipped-with-an-infiniband-nic-d.md)
        -   [How Can I Manually Configure an IP Address for an InfiniBand NIC?](how-can-i-manually-configure-an-ip-address-for-an-infiniband-nic.md)
        -   [What Should I Do If a NIC Fails to Work?](what-should-i-do-if-a-nic-fails-to-work.md)
        -   [How Can I Handle the Issue that a Windows 7 ECS Equipped with an Intel 82599 NIC Reports an Error in SR-IOV Scenarios?](how-can-i-handle-the-issue-that-a-windows-7-ecs-equipped-with-an-intel-82599-nic-reports-an-error-in.md)
        -   [How Can I Test Network Performance?](how-can-i-test-network-performance.md)
        -   [How Can I View and Modify Kernel Parameters of a Linux ECS?](how-can-i-view-and-modify-kernel-parameters-of-a-linux-ecs.md)
        -   [Can the ECSs of Different Accounts Communicate over the Intranet?](can-the-ecss-of-different-accounts-communicate-over-the-intranet.md)

    -   [Database Applications]
        -   [Can a Database Be Deployed on an ECS?](can-a-database-be-deployed-on-an-ecs.md)
        -   [Does an ECS Support Oracle Databases?](does-an-ecs-support-oracle-databases.md)



-   [Glossary](glossary.md)

