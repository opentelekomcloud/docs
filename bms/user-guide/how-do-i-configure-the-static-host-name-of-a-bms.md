# How Do I Configure the Static Host Name of a BMS?<a name="EN-US_TOPIC_0068279730"></a>

## Symptom<a name="section1619013016"></a>

The static host name of a Linux BMS is user-defined and injected on the console during the BMS creation. You can use the console or run the  **hostname**  command to change the host name of a BMS. However, if you restart the BMS, its host name will be automatically changed to the user-defined one injected on the console.

## Automatically Updating the Host Name \(Recommended\)<a name="section154902911814"></a>

Change the host name of the BMS on the console and enable automatic host name synchronization in the BMS OS. In this way, after the BMS is restarted, it automatically synchronizes the host name from the console.

This method has the following restrictions:

-   The host name contains a maximum of 63 characters.
-   Special characters except hyphens \(-\), underscores \(\_\), and periods \(.\) are not supported.
-   Uppercase letters are not supported.
-   This method does not apply to Windows BMSs.

1.  Log in to the management console, click  **Bare Metal Server**  under  **Computing**.
2.  Click the name of the BMS whose host name is to be changed.
3.  On the displayed page, click  ![](figures/edit-icon.png)  next to  **Name**, enter a new host name that meets the preceding requirements, and click  ![](figures/ok-icon.png)  to save the change.
4.  <a name="li1574320984514"></a>Log in to the BMS OS and run the following command to enable automatic host name synchronization:

    **vi /opt/huawei/network\_config/bms-network-config.conf**

    Set the value of  **auto\_synchronize\_hostname**  to  **True**.

    ```
    auto_synchronize_hostname = True
    ```

    Press  **Esc**  and enter  **:wq**  to save and exit the file.

5.  Log in to the management console again, locate the row that contains the BMS, click  **More**  in the  **Operation**  column, and select  **Restart**.

    After about 10 minutes, verify that the BMS is restarted and its host name is automatically updated.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If you set the value of  **auto\_synchronize\_hostname**  in step  [4](#li1574320984514)  to  **False**, the host name configured during BMS creation will be retained.  


## Manually Updating the Host Name<a name="section2033715325415"></a>

To make the changed host name take effect even after the BMS is stopped or restarted, save the changed name into configuration files.

For example, if the changed host name is  _new\_hostname_, perform the following steps:

1.  Modify the  **/etc/hostname**  configuration file.
    1.  Run the following command to edit the  **/etc/hostname**  configuration file:

        **sudo vim /etc/hostname**

    2.  Change the host name to  _new\_hostname_.
    3.  Run the following command to save and exit the configuration file:

        **:wq**

2.  \(Optional\) For Red Hat Enterprise Linux, CentOS, and Fedora 6, modify the configuration file  **/etc/sysconfig/network**.
    1.  Run the following command to edit the  **/etc/sysconfig/network**  configuration file:

        **sudo vim /etc/sysconfig/network**

    2.  Change the  **HOSTNAME**  value to  _new\_hostname_.

        **HOSTNAME=**_new\_hostname_

    3.  Run the following command to save and exit the configuration file:

        **:wq**

3.  Modify the  **/etc/cloud/cloud.cfg**  configuration file.
    1.  Run the following command to edit the  **/etc/cloud/cloud.cfg**  configuration file:

        **sudo vim /etc/cloud/cloud.cfg**

    2.  Use either of the following methods to modify the configuration file:
        -   Method 1: Change the  **preserve\_hostname**  parameter value or add the  **preserve\_hostname**  parameter to the configuration file.

            If  **preserve\_hostname: false**  is already available in the  **/etc/cloud/cloud.cfg**  configuration file, change it to  **preserve\_hostname: true**.

            If  **preserve\_hostname: false**  is unavailable in the  **/etc/cloud/cloud.cfg**  configuration file, add  **preserve\_hostname: true**  before  **cloud\_init\_modules**.

        -   Method 2: Delete or comment out the following content:

            **update\_hostname**

    3.  Run the following command to save and exit the configuration file:

        **:wq**

4.  Change the BMS network configuration script  **bms-network-config.conf**.

    The value of parameter  **enable\_preserve\_hostname**  in the  **bms-network-config.conf**  file is  **False**  by default, indicating that the host name is updated each time the board resets. To disable this function, change its value to  **True**.

    1.  Run the following command to edit the configuration script  **bms-network-config.conf**:

        **sudo vim /opt/huawei/network\_config/bms-network-config.conf**

    2.  Set the value of  **enable\_preserve\_hostname**  to  **True**.

        **enable\_preserve\_hostname: True**

    3.  Run the following command to save and exit the configuration file:

        **:wq!**

5.  \(Optional\) For SUSE, modify the configuration file  **/etc/sysconfig/network/dhcp**.
    1.  Run the following command to edit the  **/etc/sysconfig/network/dhcp**  configuration file:

        **sudo vim /etc/sysconfig/network/dhcp**

    2.  Set the value of  **DHCLIENT\_SET\_HOSTNAME**  to  **no**  to ensure that DHCP does not automatically allocate host names.

        **DHCLIENT\_SET\_HOSTNAME="no"**

    3.  Run the following command to save and exit the configuration file:

        **:wq**

6.  Run the following command to restart the BMS:

    **sudo reboot**

7.  Run the following command to check whether the static host name is changed:

    **sudo hostname**

    If the changed host name  _new\_hostname_  is displayed in the command output, the host name is changed and the new name permanently takes effect.


