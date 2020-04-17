# Logging In to an ECS Using VNC<a name="EN-US_TOPIC_0125376075"></a>

This section describes how to log in to an ECS using VNC on the ECS management console. This login method is mainly used for emergent O&M. In other scenarios, it is recommended that you log in to the ECS using SSH.

## Login Notes<a name="section3378547181032"></a>

If no default image password is set when Cloud-Init is installed, you must log in to the ECS by following the instructions provided in section  [Logging In to a Linux ECS Using a Key Pair \(SSH\)](logging-in-to-a-linux-ecs-using-a-key-pair-(ssh).md). After logging in using SSH, you can set the ECS login password. For details about other login notes, see "Logging In to an ECS Using VNC" in the _ECS User Guide_ \(**Getting Started \> Logging In to an ECS \> Logging In to an ECS Using VNC**\).

## Logging In to an ECS<a name="section26776515111928"></a>

1.  Log in to the MRS management console.
2.  Click  ![](figures/dt_mrs_project_region_image01.png)  in the upper-left corner on the management console and select **Region** and **Project**.
3.  Choose  **Clusters \> Active Clusters**, select a running cluster, and click its name to switch to the cluster details page.
4.  On the basic information page, query the IP addresses of Master1 and Master2 nodes.
5.  Log in to the ECS management console. Choose  **IP Address**  from the drop-down list of the search box on the right.
6.  Enter the IP address of Master1 or Master2 and click  ![](figures/icon_mrs_search_r.jpg).
7.  In the searched ECS, click  **Remote Login**  in  **Operation**.

    For details about remote login to an ECS, see "Logging In to an ECS Using VNC" in the  _ECS User Guide_ \(**Getting Started \> Logging In to an ECS \> Logging In to an ECS Using VNC**\).


## Changing the OS Keyboard Language<a name="section8454625114537"></a>

All nodes in the MRS cluster use the Linux OS. For details about changing the OS keyboard language, see "Logging In to an ECS Using VNC" in the  _ECS User Guide_  \(Getting Started \> Logging In to an ECS \> Logging In to an ECS Using VNC\).

