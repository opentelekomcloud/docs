# Optimization Process<a name="EN-US_TOPIC_0047501133"></a>

A Linux ECS can be switched from Xen to KVM if xen-pv and VirtIO drivers run on the ECS. Before changing a Xen-based ECS to a KVM-based ECS, ensure that the required drivers have been installed and the UUID has been configured for the Linux private image. In addition, optimizing the private image can improve network performance of the ECS.

1.  Create an ECS using the Linux private image to be optimized and log in to the ECS.
2.  Uninstall the PV Driver installed on the ECS.

    For details, see  [Uninstalling the PV Driver from a Linux ECS](uninstalling-the-pv-driver-from-a-linux-ecs.md).

3.  Change the disk ID in the GRUB configuration file to UUID.

    For details, see  [Changing the Disk Identifier in the GRUB Configuration File to UUID](changing-the-disk-identifier-in-the-grub-configuration-file-to-uuid.md).

4.  Change the disk ID in the fstab file to UUID.

    For details, see  [Changing the Disk Identifier in the fstab File to UUID](changing-the-disk-identifier-in-the-fstab-file-to-uuid.md).

5.  Install native Xen and KVM drivers.

    For details, see  [Installing Native Xen and KVM Drivers](installing-native-xen-and-kvm-drivers.md).

6.  Delete log files and historical records, and stop the ECS.

    For details, see  [Clearing System Logs](clearing-system-logs-(linux).md).

7.  Create a Linux private image using the ECS.

