# Obtaining ECS Console Logs<a name="EN-US_TOPIC_0057711189"></a>

## Scenarios<a name="section1826165816643"></a>

When an ECS cannot start or run properly, you can download and view ECS console logs for troubleshooting, for example, checking whether the kernel and service configuration are correct.

The ECS console logs record ECS operations, such as ECS starting, stopping, restarting, or forcibly restarting. Through the management console, you can obtain the ECS logs within one hour.

## Notes<a name="section2426125161724"></a>

-   The system does not record the logs for forcible ECS stopping.
-   The system supports viewing console logs for the ECSs running the following OSs:
    -   Red Hat Enterprise Linux 6.x series
    -   Red Hat Enterprise Linux 7.x series
    -   CentOS 6.x series
    -   CentOS 7.x series
    -   Ubuntu 14.x series
    -   Ubuntu 16.x series
    -   SUSE 11.x series
    -   SUSE 12.x series
    -   OpenSUSE 13.x series
    -   OpenSUSE 42.x series
    -   Debine 16.x series
    -   Fedora series
    -   Freebsd series
    -   CoreOS series

-   The ECSs running Windows do not support console logs.
-   The system can save up to 100 KB log files.

## Procedure<a name="section24136850162414"></a>

1.  Log in to the ECS.
2.  Check and modify the grub file.

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
            -   If no,  **ttyS0**  has not been configured. Go to  [2.b](#en-us_topic_0057450886_li29451607172853).

        2.  <a name="en-us_topic_0057450886_li29451607172853"></a>Run the following command to open the configuration file to be edited:

            **vi /usr/share/oem/grub.cfg**

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >If the  **/usr/share/oem/grub.cfg**  configuration file does not exist, manually create the file.  

        3.  Add  **set linux\_append="console=ttyS0"**. If  **set linux\_append="console=ttyS0"**  already exists, you do not need to add it. Save the change and exit.

3.  Click  **Restart**  to restart the ECS.
4.  Obtain ECS console logs.
    1.  Log in to the management console.
    2.  Click  ![](figures/icon-region-0.png)  in the upper left corner and select the desired region and project.
    3.  Under  **Computing**, click  **Elastic Cloud Server**.
    4.  On the  **Elastic Cloud Server**  page, click the name of the target ECS.
    5.  On the page providing details about the ECS, click the  **Console Logs**  tab.
    6.  Choose the number of lines to be displayed for a log from the  **Displayed Lines**  drop-down list.
    7.  Click  **Query**.

        View details of the displayed log.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >After you click  **Query**, the system will not automatically update the displayed log. To view the latest log, click  **Query**  again.  

    8.  \(Optional\) Click  **Download**  to download the information of the displayed log.

        Downloaded log files are in .txt format.



## Related Links<a name="section42122526164622"></a>

[Why Does the System Display a Question Mark When I Attempt to Obtain Console Logs?](why-does-the-system-display-a-question-mark-when-i-attempt-to-obtain-console-logs.md)

