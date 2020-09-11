# Uninstalling the PV Driver from a Linux ECS<a name="EN-US_TOPIC_0037352186"></a>

## Scenarios<a name="section8801182220417"></a>

When optimizing a Linux private image, you need to change the UUID in the fstab and GRUB configuration files, and install native Xen and KVM drivers on the ECS. To ensure that you can successfully install native Xen and KVM drivers, you must uninstall the PV driver from the ECS.

## Procedure<a name="section1381148120949"></a>

1.  Log in to the ECS as user  **root**  using VNC.
2.  Run the following command to check whether the PV driver is installed in the OS:

    **ps -ef | grep uvp-monitor**

    The PV driver is installed in the OS if the following information is displayed:

    ```
    root     4561        1    0   Jun29 ?           00:00:00   /usr/bin/uvp-monitor
    root     4567     4561    0   Jun29 ?           00:00:00   /usr/bin/uvp-monitor
    root     6185     6085    0   03:04  pts/2      00:00:00   grep uvp-monitor
    ```

    -   If the PV driver is installed, go to  [3](#li4726695220949).
    -   If the PV driver is not installed, perform the operations in  [Changing the Disk Identifier in the fstab File to UUID](changing-the-disk-identifier-in-the-fstab-file-to-uuid.md),  [Installing Native Xen and KVM Drivers](installing-native-xen-and-kvm-drivers.md), and  [Changing the Disk Identifier in the GRUB Configuration File to UUID](changing-the-disk-identifier-in-the-grub-configuration-file-to-uuid.md).

3.  <a name="li4726695220949"></a>In the VNC login window, open the CLI.

    For how to open the CLI, see the OS manual.

4.  Run the following command to uninstall the PV driver:

    **/etc/.uvp-monitor/uninstall**

    -   The PV driver is uninstalled successfully if the following command output is displayed:

        ```
        The PV driver is uninstalled successfully. Reboot the system for the uninstallation to take effect.
        ```

    -   If  **uvp-monitor**  is not contained in the command output, go to  [5](#li45681026173616).

        ```
        -bash: /etc/.uvp-monitor/uninstall: No such file or directory
        ```

5.  <a name="li45681026173616"></a>Perform the following operations to delete  uvp-monitor  that fails to take effect to prevent log overflow:
    1.  Run the following command to check whether UVP user-mode programs are installed in the OS:

        **rpm -qa | grep uvp**

        Information similar to the following is displayed:

        ```
        libxenstore_uvp3_0-3.00-36.1.x86_64
        uvp-monitor-2.2.0.315-3.1.x86_64
        kmod-uvpmod-2.2.0.315-3.1.x86_64
        ```

    2.  Run the following commands to delete the installation packages:

        **rpm -e kmod-uvpmod**

        **rpm -e uvp-monitor**

        **rpm -e libxenstore\_uvp**



