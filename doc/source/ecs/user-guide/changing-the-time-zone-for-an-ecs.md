# Changing the Time Zone for an ECS<a name="EN-US_TOPIC_0040630518"></a>

## Scenarios<a name="section2750020410549"></a>

The default time zone for an ECS is the one you selected when creating the image that was used to create the ECS. This section describes how to change the time zone for an ECS to the local one or to another time zone in your network.

After you log in to your ECS, if you find that the time on the ECS is different from the local time, change the time zone for the ECS so that the time on the ECS is the same as the local time.

## For Linux<a name="section1860378410555"></a>

The process of changing the time zone for a Linux ECS depends on the OS. In this section, the CentOS 6.x 64bit OS is used to demonstrate how to change the time zone for a Linux ECS.

1.  Log in to the ECS.
2.  Run the following command to switch to user  **root**:

    **su - root**

3.  Run the following command to obtain the time zones supported by the ECS:

    **ls /usr/share/zoneinfo/**

    In the terminal display, the  **/user/share/zoneinfo**  directory contains a hierarchy of time zone data files. Use the directory structure to obtain your desired time zone file.

    The directory structure shown in  **/user/share/zoneinfo**  includes both time zones and directories. The directories contain time zone files for specific cities. Locate the time zone for the city in which the ECS is located.

    For example:

    -   If you are to use the time zone for Shanghai, China, run the  **ls /usr/share/zoneinfo/Asia**  command to obtain the directory  **/usr/share/zoneinfo/Asia/Shanghai**.
    -   If you are to use the time zone for Paris, France, run the  **ls /usr/share/zoneinfo/Europe**  command to obtain the directory  **/usr/share/zoneinfo/Europe/Paris**.

4.  Set the target time zone.
    1.  Run the following command to open the  **/etc/sysconfig/clock**  file:

        **vim /etc/sysconfig/clock**

    2.  Locate the  **ZONE**  entry and change its value to the name of the desired time zone file.

        For example:

        -   If the target time zone is for Shanghai, China, change the  **ZONE**  entry value as follows:

            ZONE="Asia/Shanghai"

        -   If the target time zone is for Paris, France, change the  **ZONE**  entry value as follows:

            ZONE="Europe/Paris"


5.  Press  **Esc**. Then, run the following command to save and exit the  **/etc/sysconfig/clock**  file:

    **:wq**

6.  Run the following command to check whether the  **/etc/localtime**  file is available on the ECS:

    **ls /etc/localtime**

    -   If the file is available, go to step  [7](#li35115782151653).
    -   If the file is not available, go to step  [8](#li564938451108).

7.  <a name="li35115782151653"></a>Run the following command to delete the existing  **/etc/localtime**  file:

    **rm /etc/localtime**

8.  <a name="li564938451108"></a>Run the following command to create a symbolic link between  **/etc/localtime**  and your time zone file so that the ECS can find this time zone file when it references the local time:

    **ln -sf /usr/share/zoneinfo/**_A__sia/Shanghai_**/etc/localtime**

9.  Run the following command to restart the ECS so that all services and applications running on the ECS use the new time zone:

    **reboot**

10. Log in to the ECS again and run the following command as user  **root**  to check whether the time zone has been changed:

    **ls -lh /etc/localtime**

    The following information is displayed:

    ```
    # ls -lh /etc/localtime
    lrwxrwxrwx 1 root root 33 Nov 27 11:01 /etc/localtime -> /usr/share/zoneinfo/Asia/Shanghai
    ```


## For Windows<a name="section77183612015"></a>

1.  Log in to the ECS.
2.  Click the time display on the far right side of the task bar located at the bottom of your screen. In the dialog box that is displayed, click  **Change date and time settings**.

    The  **Date and Time**  page is displayed.

    **Figure  1**  Date and Time<a name="fig3371712915"></a>  
    ![](figures/date-and-time.png "date-and-time")

3.  Click  **Change time zone**.

    The  **Time Zone Settings**  page is displayed.

4.  In the  **Set the time zone**  pane, choose the target time zone from the  **Time zone**  drop-down list.
5.  Click  **OK**.

