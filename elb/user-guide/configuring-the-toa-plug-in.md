# Configuring the TOA Plug-in<a name="EN-US_TOPIC_0098947027"></a>

## Scenarios<a name="en-us_topic_0040807238_section38584869111927"></a>

ELB provides customized strategies for managing service access. Before customizing these strategies, ELB needs to obtain the client's IP address contained in the access request. The TOA kernel module installed on backend servers is used to obtain IP addresses \(IPv4 IP addresses\) in the requests.

You can refer to this topic for compiling the TOA kernel module in the OS if you use TCP for traffic distribution.

The configuration operations of the TOA module for Linux OSs with kernel version of 2.6.32 are different from those for Linux OSs with kernel version of 3.0 or later.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   TOA does not support listeners using the UDP protocol.  
>-   The TOA module can work properly in the following OSs and the methods for installing other kernel versions are similar:  
>    -   CentOS 6.8 \(kernel version 2.6.32\)  
>    -   SUSE 11 SP3 \(kernel version 3.0.76\)  
>    -   CentOS 7/7.2 \(kernel version 3.10.0\)  
>    -   Ubuntu 16.04.3 \(kernel version 4.4.0\)  
>    -   Ubuntu 18.04 \(Kernel version 4.15.0\)  
>    -   OpenSUSE 42.2 \(kernel version 4.4.36\)  
>    -   CoreOS 10.10.5 \(kernel version 4.9.16\)  
>    -   Debian 8.2.0 \(Kernel version 3.16.0\)  

## Prerequisites<a name="en-us_topic_0040807238_section29028108105843"></a>

-   The development environment for compiling the kernel module must be the same as that of the current kernel.
-   VMs can access OS repositories.
-   Users other than  **root**  must have sudo permissions.

## Procedure<a name="en-us_topic_0040807238_section32663382105928"></a>

-   In the following operations, the Linux kernel version is 3.0 or later.

1.  Prepare the compilation environment.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >During the installation, you need to download the required kernel module development package from the Internet if it cannot be found in the source.  

    The following are operations for compiling the kernel module in different Linux OSs. Choose appropriate operations as needed.

    -   CentOS
        1.  Run the following command to install the GCC:

            **sudo yum install gcc**

        2.  Run the following command to install the make tool:

            **sudo yum install make**

        3.  Run the following command to install the kernel module development package \(the development package header and module library must have the same version as the kernel\):

            **sudo yum install kernel-devel-\`uname -r\`**

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >During the installation, you need to download the required kernel module development package from the following address if it cannot be found in the source:  
            >https://mirror.netcologne.de/oracle-linux-repos/ol7\_latest/getPackage/  
            >For example, to install 3.10.0-693.11.1.el7.x86\_64, run the following command:  
            >**rpm -ivh kernel-devel-3.10.0-693.11.1.el7.x86\_64.rpm**  


    -   Ubuntu and Debian
        1.  Run the following command to install the GCC:

            **sudo apt-get install gcc**

        2.  Run the following command to install the make tool:

            **sudo apt-get install make**

        3.  Run the following command to install the kernel module development package \(the development package header and module library must have the same version as the kernel\):

            **sudo apt-get install linux-headers-\`uname -r\`**

    -   SUSE
        1.  Run the following command to install the GCC:

            **sudo zypper install gcc**

        2.  Run the following command to install the make tool:

            **sudo zypper install make**

        3.  Run the following command to install the kernel module development package \(the package header and module library must have the same version as the kernel\):

            **sudo zypper install kenel-default-devel**

    -   CoreOS

        For CoreOS, the kernel module will be compiled in a container, and it must be started before the kernel module is compiled. 

        For detailed operations, see the CoreOS documentation. Obtain the documentation from the following link:

        [https://coreos.com/os/docs/latest/kernel-modules.html](https://coreos.com/os/docs/latest/kernel-modules.html)

2.  Compile the Kernel module.
    1.  Use the git tool and run the following command to download the TOA kernel module source code:

        **git clone **[https://github.com/Huawei/TCP\_option\_address.git](https://github.com/Huawei/TCP_option_address)

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If the git tool is not installed, download the TOA kernel module source code from the following link:  
        >[https://github.com/Huawei/TCP\_option\_address](https://github.com/Huawei/TCP_option_address)  

    2.  Run the following commands to enter the source code directory and compile the module:

        **cd src**

        **make**

        If no warning or error code is prompted, the compilation was successful. Verify that the  **toa.ko**  file was generated in the current directory.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >If error message "config\_retpoline=y but not supported by the compiler, Compiler update recommended" is displayed, the GCC version is too early. Upgrade the GCC to a later version.  


3.  <a name="en-us_topic_0040807238_li64464787101517"></a>Load the kernel module.
    1.  Run the following command to load the kernel module:

        **sudo insmod toa.ko**

    2.  Run the following command to check the module loading and to view the kernel output information:

        **dmesg | grep TOA**

        If  **TOA: toa loaded**  is displayed in the command output, the kernel module has been loaded.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >After compiling the CoreOS kernel module in the container, copy it to the host system and then load it. The container for compiling the kernel module shares the  **/lib/modules**  directory with the host system, so you can copy the kernel module in the container to this directory, allowing the host system to use it.  


4.  Set the script to enable it to automatically load the kernel module.

    To make the TOA kernel module take effect when the system starts, add the command for loading the TOA kernel module to your startup script.

    You can use either of the following methods to automatically load the kernel module:

    -   Add the command for loading the TOA kernel module to a customized startup script as required.
    -   Perform the following operations to configure a startup script:
        1.  Create the  **toa.modules**  file in the  **/etc/sysconfig/modules/**  directory. This file contains the TOA kernel module loading script.

            The following is an example of the content in the  **toa.modules**  file.

            **\#!/bin/sh**

            **/sbin/modinfo -F filename /root/toa/toa.ko \> /dev/null 2\>&1**

            **if \[ $? -eq 0 \]; then**

            **/sbin/insmod /root/toa/toa.ko**

            **fi**

            **/root/toa/toa.ko**  is the path of the TOA kernel module file. You need to replace it with their actual path.

        2.  Run the following command to add execution permissions for the  **toa.modules**  startup script:

            **sudo** **chmod +x /etc/sysconfig/modules/toa.modules**

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >If the kernel is upgraded, the current TOA kernel module will no longer match. Therefore, you need to compile the TOA kernel module again.  


5.  Install the Kernel module on multiple nodes.

    To load the kernel module in the same OSs, copy the  **toa.ko**  file to VMs where the kernel module is to be loaded and then perform the operations in  [3](#en-us_topic_0040807238_li64464787101517).

    After the kernel module is successfully loaded, applications can obtain the real IP address contained in the request.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The OS of the node must have the same version as the kernel.  


-   **In the following operations, the Linux kernel version is 2.6.32.**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The TOA plug-in supports the OSs \(CentOS 6.8 image\) with a kernel of 2.6.32-xx. Perform the following steps to configure the TOA kernel module:  


1.  Obtain the kernel source code package  **Linux-2.6.32-220.23.1.el6.x86\_64.rs.src.tar.gz**  containing the TOA module from the following link:

    [http://kb.linuxvirtualserver.org/images/3/34/Linux-2.6.32-220.23.1.el6.x86\_64.rs.src.tar.gz](http://kb.linuxvirtualserver.org/images/3/34/Linux-2.6.32-220.23.1.el6.x86_64.rs.src.tar.gz)

2.  Decompress the kernel source code package.
3.  Modify compilation parameters.
    1.  Open the  **linux-2.6.32-220.23.1.el6.x86\_64.rs**  folder.
    2.  Edit the  **net/toa/toa.h**  file.

        Change the value of  **\#define TCPOPT\_TOA200**  to  **\#define TCPOPT\_TOA254**.

    3.  On the shell page, run the following commands:

        **sed -i 's/CONFIG\_IPV6=m/CONFIG\_IPV6=y/g' .config**

        **echo -e '\\n\# toa\\nCONFIG\_TOA=m' \>\> .config**

        After the configuration, the IPv6 module is compiled into the kernel. TOA is compiled into a separate kernel module and can be independently started and stopped.

    4.  Edit  **Makefile**.

        You can add a description to the end of  **EXTRAVERSION =**. This description will be displayed in  **uname -r**, for example,  **-toa**.

4.  Run the following command to compile the software package:

    **make -j  _n_**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >_n_  indicates the number of vCPUs. For example, if there are four vCPUs,  _n_  can be set to  _4_.  

5.  Run the following command to install the kernel module:

    **make modules\_install**

    The following information is displayed.

    **Figure  1**  Installing the kernel module<a name="en-us_topic_0040807238_fig22762118104555"></a>  
    ![](figures/installing-the-kernel-module.jpg "installing-the-kernel-module")

6.  Run the following command to install the kernel:

    **make install**

    The following information is displayed.

    **Figure  2**  Installing the kernel<a name="en-us_topic_0040807238_fig58895487104737"></a>  
    ![](figures/installing-the-kernel.jpg "installing-the-kernel")

7.  Open the  **/boot/grub/grub.conf**  file and configure the kernel to start up when the system starts.
    1.  Change the default startup kernel from the first kernel to the zeroth kernel by changing  **default=1**  to  **default=0**.
    2.  Add the  **nohz=off**  parameter to the end of the line containing the  **vmlinuz-2.6.32-toa**  kernel. If  **nohz**  is not disabled, the CPU0 usage may be high, causing uneven stress.

        **Figure  3**  Configuration file<a name="en-us_topic_0040807238_fig28703665105040"></a>  
        ![](figures/configuration-file.jpg "configuration-file")

    3.  Save the modification and exit. Restart the OS.

        During the restart, the system will load the  **vmlinuz-2.6.32-toa**  kernel.

8.  After the restart, run the following command to load the TOA module:

    **modprobe toa**

    You are advised to add the  **modprobe toa**  command to both the startup script and the system scheduled monitoring script.

    **Figure  4**  Adding the  **modprobe toa**  command<a name="en-us_topic_0040807238_fig15588814105614"></a>  
    ![](figures/adding-the-modprobe-toa-command.jpg "adding-the-modprobe-toa-command")

    After the TOA module is loaded, query the kernel information.

    **Figure  5**  Querying the kernel<a name="en-us_topic_0040807238_fig13244290105833"></a>  
    ![](figures/querying-the-kernel.jpg "querying-the-kernel")


