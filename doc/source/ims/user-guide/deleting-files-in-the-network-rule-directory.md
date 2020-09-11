# Deleting Files in the Network Rule Directory<a name="EN-US_TOPIC_0069904570"></a>

## Scenarios<a name="section12838834226"></a>

To prevent NIC name drift when you use a private image to create ECSs, you need to delete files in the network rule directory of the VM where the ECS or image file is located during the private image creation.

>![](/images/icon-note.gif) **NOTE:**   
>When registering an external image file as a private image, delete files in the network rule directory on the VM where the external image file is located. You are advised to delete the files on the VM and then export the image file.  

## Prerequisites<a name="section15556157"></a>

An OS and the xen-pv and VirtIO drivers have been installed for the ECS.

## Deleting Network Rule Files<a name="section5787686"></a>

1.  Run the following command to query the files in the network rule directory:

    **ls -l /etc/udev/rules.d**

2.  Run the following commands to delete the files whose names contain  **persistent**  and  **net**  from the network rule directory:

    Example:

    **rm** **/etc/udev/rules.d/**_30-_**net\_persistent**_-names_**.rules**

    **rm** **/etc/udev/rules.d/**_70-_**persistent-net.rules**

    The italic content in the commands varies depending on your environment.

    >![](/images/icon-note.gif) **NOTE:**   
    >For CentOS 6 images, to prevent NIC name drift, you need to create an empty rules configuration file.  
    >Example:  
    >**touch /etc/udev/rules.d/**_75_**-persistent-net-generator.rules**  //Replace  _75_  with the actual value in the environment.  

3.  Delete network rules.
    -   If the OS uses the initrd system image, perform the following operations:
        1.  Run the following command to check whether the initrd image file whose name starts with  **initrd**  and ends with  **default**  contains the  **persistent**  and  **net**  network device rule files \(replace the italic content in the following command with the actual OS version\):

            **lsinitrd** **/boot/initrd-**_2.6.32.12-0.7_**-default** **|grep** **persistent|grep** **net**

            -   If no, no further action is required.
            -   If yes, go to  [3.b](#it_58_45_200040_1_mmccppss_bak).

        2.  <a name="it_58_45_200040_1_mmccppss_bak"></a>Run the following command to back up the initrd image file \(replace the italic part in the following command with the actual OS version\):

            **cp** **/boot/initrd-**_2.6.32.12-0.7_**-default** **/boot**_**/**_**initrd-**_2.6.32.12-0.7**-**_**default\_bak**

        3.  Run the following command to generate the initrd file again:

            **mkinitrd**

    -   If the OS uses the initramfs system image \(such as Ubuntu\), perform the following operations:
        1.  Run the following command to check whether the initramfs image files starting with  **initrd**  and ending with  **generic**  contain persistent and net rule files.

            **lsinitramfs** **/boot/initrd.img-3.19.0-25-generic|grep** **persistent|grep** **net**

            -   If no, you do not need to clear the files in the network rule directory.
            -   If yes, go to  [3.b](#li59460586164647).

        2.  <a name="li59460586164647"></a>Run the following command to back up the initrd image file:

            **cp** **/boot/initrd.img-3.19.0-25-generic** **/boot/initrd.img-3.19.0-25-generic\_bak**

        3.  Run the following command to generate the initramfs image files again:

            **update-initramfs -u**




## Disabling NetworkManager<a name="section54488258164255"></a>

There are two methods for installing Linux online:

-   NetworkManager: provides automatic network configuration function.
-   **ifup**  commands

To enable the ECS to obtain an IP address automatically by static injection, use the predefined configuration file to overwrite the network configuration file in the ECS during the ECS creation to configure an IP address for it.

Therefore, the purpose of configuring the Linux OS online installation method is to disable the NetworkManager function. After it is disabled, the network configuration file in the ECS can be overwritten.

You can run one of the following commands to disable NetworkManager depending on the OS:

**service** **NetworkManager stop;** **chkconfig** **NetworkManager** **off**

or

**systemctl** **stop** **NetworkManager.service;** **systemctl** **disable** **NetworkManager.service**

For SUSE Linux, you can also use YaST to disable NetworkManager. The procedure is as follows:

>![](/images/icon-note.gif) **NOTE:**   
>These steps are not required if no NetworkManager is deployed in the ECS OS, for example, SUSE Linux Enterprise 12.  

1.  Run the following command on the ECS to enter the control center:

    **yast**

2.  Choose  **Network Devices**  \>  **Network Settings**.
3.  On the  **Network Settings**  page, press  **Alt+G**.

    The  **Global Options**  page is displayed.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the shortcut keys provided in the steps do not take effect in practice due to OS version or language diversities, use  **Tab**,  **←**, and  **→**  keys to select the required options.  

4.  Press  **Alt+T**  and select  **Traditional Method with ifup**.
5.  Press  **F10**  to save the configuration and exit.
6.  Press  **Alt+Q**  to return to the CLI.

