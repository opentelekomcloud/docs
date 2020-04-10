# Configuring Console Logging<a name="EN-US_TOPIC_0057450886"></a>

## Scenarios<a name="section159104822314"></a>

If you want to use the ECS console logging function, you need to configure related parameters on the ECS.

Currently, ECSs running the following OSs are supported: CentOS 6 series, Red Hat 6 series, CentOS 7 series, Red Hat 7 series, Ubuntu 14 series, SUSE 11 series, SUSE 12 series, Debian, Ubuntu 16 series, Fedora, FreeBSD, and CoreOS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>To use the Console Log function on the ECS console, perform this operation. Otherwise, skip this section.  

## Prerequisites<a name="section45948871103043"></a>

You have logged in to the ECS.

## Procedure<a name="section9404234103043"></a>

The configuration method varies depending on the OS.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>To prevent impact on the start of the recovery mode, you are advised to modify only the item used for the default start.  

-   For CentOS and Red Hat 6, perform the following steps:
    1.  Run the following command to open the configuration file:

        **vi /boot/grub/menu.lst**

    2.  Locate the row that contains  **linux**,  **linux16**, or  **kernel**  \(depending on the system\), add  **console=ttyS0**  to its end, and delete parameter  **rhgb quiet**. If  **console=ttyS0**  already exists, you do not need to add it. Save the change and exit.

-   For CentOS 7, Red Hat 7, and Ubuntu 14, perform the following steps:
    1.  Run the following command to open the configuration file:

        **vi /boot/grub2/grub.cfg**

    2.  Locate the row that contains  **linux**,  **linux16**, or  **kernel**  \(depending on the system\), add  **console=ttyS0**  to its end, and delete parameter  **rhgb quiet**. If  **console=ttyS0**  already exists, you do not need to add it. Save the change and exit.

-   For SUSE Linux 11, perform the following steps:
    1.  Run the following command to open the configuration file:

        **vi /boot/grub/menu.1st**

    2.  Locate the row that contains  **linux**,  **linux16**, or  **kernel**  \(depending on the system\) and add  **console=ttyS0**  to its end. If  **console=ttyS0**  already exists, you do not need to add it. Save the change and exit.

-   For SUSE Linux 12, openSUSE 13, and openSUSE 42, perform the following steps:
    1.  Run the following command to open the configuration file:

        **vi /boot/grub2/grub.cfg**

    2.  Locate the row that contains  **linux**,  **linux16**, or  **kernel**  \(depending on the system\) and add  **console=ttyS0**  to its end. If  **console=ttyS0**  already exists, you do not need to add it. Save the change and exit.

-   For Debian and Ubuntu 16, perform the following steps:
    1.  Run the following command to open the configuration file:

        **vi /boot/grub/grub.cfg**

    2.  Locate the row that contains  **linux**,  **linux16**, or  **kernel**  \(depending on the system\) and add  **console=ttyS0**  to its end. If  **console=ttyS0**  already exists, you do not need to add it. Save the change and exit.

-   For Fedora, perform the following steps:
    1.  Run the following command to open the configuration file:

        **vi /boot/grub2/grub.cfg**

    2.  Locate the row that contains  **linux**,  **linux16**, or  **kernel**  \(depending on the system\) and add  **console=ttyS0**  to its end. If  **console=ttyS0**  already exists, you do not need to add it. Save the change and exit.

-   For FreeBSD, perform the following steps:
    1.  Run the following command to open the configuration file:

        **vi /boot/loader.conf**

    2.  Add  **console="comconsole"**. If  **console="comconsole"**  already exists, you do not need to add it. Save the change and exit.

-   For CoreOS, perform the following steps:
    1.  Run the following command to check whether  **ttyS0**  has been configured:

        **cat /proc/cmdline | grep ttyS0**

        -   If yes,  **ttyS0**  has been configured.
        -   If no,  **ttyS0**  has not been configured. Go to  [2](#li29451607172853).

    2.  <a name="li29451607172853"></a>Run the following command to open the configuration file to be edited:

        **vi /usr/share/oem/grub.cfg**

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If the  **/usr/share/oem/grub.cfg**  configuration file does not exist, manually create the file.  

    3.  Add  **set linux\_append="console=ttyS0"**. If  **set linux\_append="console=ttyS0"**  already exists, you do not need to add it. Save the change and exit.


