# User Guide

-   [Service Overview]
    -   [What Is a Bare Metal Server?](what-is-a-bare-metal-server.md)
    -   [BMS Advantages](bms-advantages.md)
    -   [Application Scenarios](application-scenarios.md)
    -   [Instance]
        -   [Instance Family](instance-family.md)
        -   [Lifecycle](lifecycle.md)

    -   [Image](image.md)
    -   [Elastic Volume Service](elastic-volume-service.md)
    -   [Network](network.md)
    -   [Security]
        -   [License Type](license-type.md)
        -   [Security Group](security-group.md)
        -   [Cloud-Init](cloud-init.md)
        -   [Key Pair and Password](key-pair-and-password.md)
        -   [Access Control](access-control.md)

    -   [Region and AZ](region-and-az.md)
    -   [Related Services](related-services.md)

-   [Getting Started]
    -   [Quick Start](quick-start.md)
    -   [Making Preparations](making-preparations.md)
    -   [Step 1: Create a BMS](step-1-create-a-bms.md)
    -   [Step 2: Log In to the BMS](step-2-log-in-to-the-bms.md)
    -   [Step 3: Deploy an Application](step-3-deploy-an-application.md)
    -   [Step 4: Release the BMS](step-4-release-the-bms.md)

-   [Instance]
    -   [Creating a BMS]
        -   [Creating a BMS](creating-a-bms.md)
        -   [Creating a BMS Supporting Quick Provisioning](creating-a-bms-supporting-quick-provisioning.md)
        -   [Creating a BMS Using a Private Image](creating-a-bms-using-a-private-image.md)

    -   [Viewing BMS Information]
        -   [Viewing BMS Creation Statuses](viewing-bms-creation-statuses.md)
        -   [Viewing BMS Details](viewing-bms-details.md)

    -   [Logging In to a Linux BMS]
        -   [Linux BMS Login Methods](linux-bms-login-methods.md)
        -   [Remotely Logging In to a BMS](remotely-logging-in-to-a-bms.md)
        -   [Logging In to a BMS Using an SSH Key Pair](logging-in-to-a-bms-using-an-ssh-key-pair.md)
        -   [Logging In to a BMS Using a Password](logging-in-to-a-bms-using-a-password.md)

    -   [Logging In to a Windows BMS]
        -   [Windows BMS Login Methods](windows-bms-login-methods.md)
        -   [Logging In to a BMS Remotely Using MSTSC](logging-in-to-a-bms-remotely-using-mstsc.md)

    -   [Managing BMSs]
        -   [Changing the Name of a BMS](changing-the-name-of-a-bms.md)
        -   [Stopping BMSs](stopping-bmss.md)
        -   [Restarting BMSs](restarting-bmss.md)
        -   [Rebuilding a BMS](rebuilding-a-bms.md)
        -   [Releasing a BMS](releasing-a-bms.md)

    -   [Using User Data and Metadata]
        -   [Injecting User Data into BMSs](injecting-user-data-into-bmss.md)
        -   [Metadata](metadata.md)

    -   [Installing Drivers and Toolkits]
        -   [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P1 BMS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p1-bms.md)
        -   [Installing the NVIDIA GPU Driver and CUDA Toolkit on a P2 BMS](installing-the-nvidia-gpu-driver-and-cuda-toolkit-on-a-p2-bms.md)


-   [Image]
    -   [Private Image Overview](private-image-overview.md)
    -   [Creating a Private Image from a BMS](creating-a-private-image-from-a-bms.md)
    -   [Creating a Private Image from an External Image File](creating-a-private-image-from-an-external-image-file.md)
    -   [Convert Image File Formats](convert-image-file-formats.md)

-   [Disk]
    -   [Attaching Data Disks](attaching-data-disks.md)
    -   [Initializing Data Disks]
        -   [Introduction to Data Disk Initialization Scenarios and Partition Styles](introduction-to-data-disk-initialization-scenarios-and-partition-styles.md)
        -   [Initializing a Windows Data Disk \(Windows Server 2016\)](initializing-a-windows-data-disk-(windows-server-2016).md)
        -   [Initializing a Linux Data Disk \(fdisk\)](initializing-a-linux-data-disk-(fdisk).md)
        -   [Initializing a Linux Data Disk \(parted\)](initializing-a-linux-data-disk-(parted).md)

    -   [Detaching a Disk](detaching-a-disk.md)
    -   [Expanding Disk Capacity](expanding-disk-capacity.md)

-   [Key Pair and Password]
    -   [Using an SSH Key Pair](using-an-ssh-key-pair.md)
    -   [Obtaining the Password of a Windows BMS](obtaining-the-password-of-a-windows-bms.md)
    -   [Deleting the Password of a Windows BMS](deleting-the-password-of-a-windows-bms.md)

-   [Network]
    -   [EIP]
        -   [Binding an EIP to a BMS](binding-an-eip-to-a-bms.md)
        -   [Unbinding an EIP from a BMS](unbinding-an-eip-from-a-bms.md)

    -   [VPC]
        -   [Overview](vpc-overview.md)
        -   [Managing Virtual IP Addresses](managing-virtual-ip-addresses.md)
        -   [Setting the Source/Destination Check for a NIC](setting-the-source-destination-check-for-a-nic.md)

    -   [High-Speed Network]
        -   [Overview](high-speed-network-overview.md)
        -   [Managing High-Speed Networks](managing-high-speed-networks.md)

    -   [User-defined VLAN]
        -   [Overview](user-defined-vlan-overview.md)
        -   [Configuring a User-defined VLAN \(SUSE Linux Enterprise Server 12\)](configuring-a-user-defined-vlan-(suse-linux-enterprise-server-12).md)
        -   [Configuring a User-defined VLAN \(SUSE Linux Enterprise Server 11\)](configuring-a-user-defined-vlan-(suse-linux-enterprise-server-11).md)
        -   [Configuring a User-defined VLAN \(Red Hat, CentOS, Oracle Linux, and EulerOS\)](configuring-a-user-defined-vlan-(red-hat-centos-oracle-linux-and-euleros).md)
        -   [Configuring a User-defined VLAN \(Ubuntu\)](configuring-a-user-defined-vlan-(ubuntu).md)
        -   [Configuring a User-defined VLAN \(Windows Server\)](configuring-a-user-defined-vlan-(windows-server).md)

    -   [IB Network]
        -   [Overview](ib-network-overview.md)

    -   [User-defined Network]
        -   [Overview](user-defined-network-overview.md)
        -   [Creating and Managing a User-defined Network](creating-and-managing-a-user-defined-network.md)

    -   [User-defined Network ACL]
        -   [Overview](user-defined-network-acl-overview.md)
        -   [Configuration Examples](configuration-examples.md)
        -   [Creating and Managing a User-defined Network ACL](creating-and-managing-a-user-defined-network-acl.md)


-   [Security]
    -   [Security Group]
        -   [Adding Security Group Rules](adding-security-group-rules.md)
        -   [Security Group Configuration Examples](security-group-configuration-examples.md)
        -   [Changing a Security Group](changing-a-security-group.md)


-   [Virtualization]
    -   [Overview](virtualization-overview.md)
    -   [VMware on BMS]
        -   [Solution Overview](solution-overview.md)
        -   [Environment Preparations](environment-preparations.md)
        -   [Restrictions](restrictions.md)
        -   [Deployment Process](deployment-process.md)
        -   [Creating and Configuring the First ESXi BMS](creating-and-configuring-the-first-esxi-bms.md)
        -   [Creating a Windows Jump VM](creating-a-windows-jump-vm.md)
        -   [Deploying the DNS and NTP Service VMs](deploying-the-dns-and-ntp-service-vms.md)
        -   [Deploying vCenter Server Appliance](deploying-vcenter-server-appliance.md)
        -   [Creating Other ESXi BMSs](creating-other-esxi-bmss.md)
        -   [Deploying VMware vSAN](deploying-vmware-vsan.md)
        -   [Deploying NSX](deploying-nsx.md)
        -   [Deploying Other VMware Components](deploying-other-vmware-components.md)
        -   [FAQs](faqs.md)


-   [Resources]
    -   [Tag]
        -   [Overview](overview.md)
        -   [Adding Tags](adding-tags.md)
        -   [Searching for Resources by Tag](searching-for-resources-by-tag.md)
        -   [Deleting Tags](deleting-tags.md)

    -   [Adjusting Resource Quotas](adjusting-resource-quotas.md)

-   [Server Monitoring]
    -   [Installing and Configuring Agent](installing-and-configuring-agent.md)

-   [Auditing of Key Operations]
    -   [Viewing Traces](viewing-traces.md)
    -   [BMS Operations Recorded by CTS](bms-operations-recorded-by-cts.md)

-   [Troubleshooting]
    -   [What Can I Do If I Cannot Log In to My BMS or the BMS EVS Disk Is Lost After the BMS Is Started or Restarted?](what-can-i-do-if-i-cannot-log-in-to-my-bms-or-the-bms-evs-disk-is-lost-after-the-bms-is-started-or-r.md)
    -   [What Should I Do If a Key Pair Created Using PuTTYgen Cannot Be Imported to the Management Console?](what-should-i-do-if-a-key-pair-created-using-puttygen-cannot-be-imported-to-the-management-console.md)
    -   [What Can I Do If Disks Cannot Be Attached to a BMS That Restarts Abnormally?](what-can-i-do-if-disks-cannot-be-attached-to-a-bms-that-restarts-abnormally.md)
    -   [What Can I Do If an EVS Disk Attached to a Windows BMS Is in Offline State?](what-can-i-do-if-an-evs-disk-attached-to-a-windows-bms-is-in-offline-state.md)

-   [FAQs]
    -   [General FAQs]
        -   [What Are the Restrictions on Using BMSs?](what-are-the-restrictions-on-using-bmss.md)
        -   [How Are BMSs Different from ECSs?](how-are-bmss-different-from-ecss.md)
        -   [What Are the Differences Between BMSs and Traditional Physical Servers?](what-are-the-differences-between-bmss-and-traditional-physical-servers.md)

    -   [Instance FAQs]
        -   [How Long Does It Take to Create a BMS?](how-long-does-it-take-to-create-a-bms.md)
        -   [Why Is Failed Displayed for a BMS Application Task But the BMS List Shows the Obtained BMS?](why-is-failed-displayed-for-a-bms-application-task-but-the-bms-list-shows-the-obtained-bms.md)
        -   [How Can I Quickly Provision BMSs Using EVS Disks?](how-can-i-quickly-provision-bmss-using-evs-disks.md)
        -   [What Are the Advanced Features of BMSs Using EVS Disks?](what-are-the-advanced-features-of-bmss-using-evs-disks.md)
        -   [Is the BMS Host Name with Suffix novalocal Normal?](is-the-bms-host-name-with-suffix-novalocal-normal.md)
        -   [How Can I Check the BMS Monitoring Status?](how-can-i-check-the-bms-monitoring-status.md)
        -   [How Do I Create an Agency for Server Monitoring of the BMS?](how-do-i-create-an-agency-for-server-monitoring-of-the-bms.md)

    -   [Login FAQs]
        -   [What Browser Versions Can Be Used to Remotely Log In to a BMS?](what-browser-versions-can-be-used-to-remotely-log-in-to-a-bms.md)
        -   [What Can I Do If the Login Page Does Not Respond?](what-can-i-do-if-the-login-page-does-not-respond.md)
        -   [What Can I Do If the BMS Console Is Displayed Improperly After I Remotely Log In to a BMS?](what-can-i-do-if-the-bms-console-is-displayed-improperly-after-i-remotely-log-in-to-a-bms.md)

    -   [Network and Security FAQs]
        -   [Can BMSs of Different Accounts Communicate with Each Other over an Internal Network?](can-bmss-of-different-accounts-communicate-with-each-other-over-an-internal-network.md)
        -   [How Do Two BMSs in the Same Region But Different AZs Communicate with Each Other?](how-do-two-bmss-in-the-same-region-but-different-azs-communicate-with-each-other.md)
        -   [Are My BMSs in the Same Subnet?](are-my-bmss-in-the-same-subnet.md)
        -   [Can BMSs Communicate with ECSs in the Same VPC?](can-bmss-communicate-with-ecss-in-the-same-vpc.md)
        -   [Can Multiple EIPs Be Bound to a BMS?](can-multiple-eips-be-bound-to-a-bms.md)
        -   [Can I Configure the EIP?](can-i-configure-the-eip.md)
        -   [How Can I Modify the Network Configuration or Restart the Network If I Can Log In to a BMS Using Only SSH?](how-can-i-modify-the-network-configuration-or-restart-the-network-if-i-can-log-in-to-a-bms-using-onl.md)
        -   [What Can I Do If the Communication Between the Primary NIC and Extension NIC of the BMS is Abnormal?](what-can-i-do-if-the-communication-between-the-primary-nic-and-extension-nic-of-the-bms-is-abnormal.md)
        -   [How Can I Configure a Static IP Address for a BMS?](how-can-i-configure-a-static-ip-address-for-a-bms.md)
        -   [How Do I Configure the DNS Server?](how-do-i-configure-the-dns-server.md)

    -   [Disk FAQs]
        -   [Can EVS Disks Be Attached to BMSs? ](can-evs-disks-be-attached-to-bmss.md)
        -   [How Do I Change the Disk Identifier in the fstab file to UUID?](how-do-i-change-the-disk-identifier-in-the-fstab-file-to-uuid.md)
        -   [What Are the Restrictions for Attaching a Disk to a BMS?](what-are-the-restrictions-for-attaching-a-disk-to-a-bms.md)
        -   [How Do I Obtain the Drive Letter of an EVS Disk?](how-do-i-obtain-the-drive-letter-of-an-evs-disk.md)
        -   [Are the EVS Disk Device Names on the Console and the Device Names in BMS OSs Consistent?](are-the-evs-disk-device-names-on-the-console-and-the-device-names-in-bms-oss-consistent.md)
        -   [Why Is the EVS Disk Size Not Updated in the BMS OS After the EVS Disk Capacity Has Been Expanded?](why-is-the-evs-disk-size-not-updated-in-the-bms-os-after-the-evs-disk-capacity-has-been-expanded.md)
        -   [How Can I Restore System Disk Data Using the Snapshot?](how-can-i-restore-system-disk-data-using-the-snapshot.md)
        -   [What Can I Do to Prevent Risks of Attaching or Detaching the System Disk?](what-can-i-do-to-prevent-risks-of-attaching-or-detaching-the-system-disk.md)
        -   [How Should I Select Storage?](how-should-i-select-storage.md)
        -   [Why Is the Disk Capacity Displayed in the BMS OS Less Than That Displayed on the Official Website?](why-is-the-disk-capacity-displayed-in-the-bms-os-less-than-that-displayed-on-the-official-website.md)

    -   [OS FAQs]
        -   [Can I Install or Upgrade BMS OSs by Myself?](can-i-install-or-upgrade-bms-oss-by-myself.md)
        -   [Can the BMS OS Be Replaced?](can-the-bms-os-be-replaced.md)
        -   [Is a GUI Provided for BMS OSs?](is-a-gui-provided-for-bms-oss.md)
        -   [Is an Upload Tool Delivered with BMS OSs?](is-an-upload-tool-delivered-with-bms-oss.md)
        -   [How Do I Configure the Static Host Name of a BMS?](how-do-i-configure-the-static-host-name-of-a-bms.md)
        -   [How Do I Set the Password Validity Period?](how-do-i-set-the-password-validity-period.md)
        -   [How Do I Set SSH Configuration Items?](how-do-i-set-ssh-configuration-items.md)
        -   [How Can I Handle the Eight-Hour Difference Between the Windows BMS and Local Time](how-can-i-handle-the-eight-hour-difference-between-the-windows-bms-and-local-time.md)
        -   [How Can I Activate a Windows BMS?](how-can-i-activate-a-windows-bms.md)
        -   [How Do I Change the SID of a Windows Server 2012 BMS?](how-do-i-change-the-sid-of-a-windows-server-2012-bms.md)
        -   [How Do I Reserve Log Space If the Root Partition Automatically Expands Disks?](how-do-i-reserve-log-space-if-the-root-partition-automatically-expands-disks.md)
        -   [How Do I Roll Back the Kernel Version If I Mistakenly Upgrade the Kernel?](how-do-i-roll-back-the-kernel-version-if-i-mistakenly-upgrade-the-kernel.md)
        -   [How Do I Increase the Swap Partition Size?](how-do-i-increase-the-swap-partition-size.md)

    -   [Virtualization]
        -   [How Do I Access VMs on a BMS with KVM Deployed from the Internet?](how-do-i-access-vms-on-a-bms-with-kvm-deployed-from-the-internet.md)


-   [Glossary](glossary.md)

