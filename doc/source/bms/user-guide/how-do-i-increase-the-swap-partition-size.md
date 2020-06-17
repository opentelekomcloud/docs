# How Do I Increase the Swap Partition Size?<a name="EN-US_TOPIC_0151841137"></a>

## Scenarios<a name="section7803145104911"></a>

When you install the Oracle database for a Linux OS, the swap partition size will be checked. If the swap partition cannot meet requirements, you can perform the operations in this section to increase the swap partition size.

>![](/images/icon-note.gif) **NOTE:**   
>The swap partition is similar to the virtual memory of the Windows OS. When the memory is insufficient, some hard disk space is virtualized into memory to improve the system running efficiency.  

## Procedure<a name="section1190013815614"></a>

1.  Log in to the BMS OS.
2.  Run the  **lsblk**  command to check the size of the swap partition.

    ![](figures/19.png)

    The size of the swap partition is 3 GB.

3.  Run the following command to increase the swap partition size by 5 GB \(example\):

    **dd if=/dev/zero of=/swapfile bs=1M count=5000**

    **chmod 600 /swapfile**

    **mkswap /swapfile swapon /swapfile echo "/swapfile swap swap defaults 0 0" \>\>/etc/fstab**

4.  Run the  **lsblk**  command to check the size of the expanded swap partition.

    ![](figures/20.png)

    The size of the swap partition is 8 GB.


