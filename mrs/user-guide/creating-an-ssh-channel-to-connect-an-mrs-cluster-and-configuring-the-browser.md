# Creating an SSH Channel to Connect an MRS Cluster and Configuring the Browser<a name="EN-US_TOPIC_0125375270"></a>

## Scenario<a name="sa32558ded664441da13efd2c5c2d3cdb"></a>

Users and an MRS cluster are in different networks. As a result, an SSH channel needs to be created to send users' requests for accessing websites to the MRS cluster and dynamically forward them to the target websites.

## Prerequisites<a name="se6e87fe62270467a9c98076d8f87f7ff"></a>

-   You have prepared an SSH client for creating the SSH channel, for example, the Git open source SSH client. You have downloaded and installed the client.
-   You have created a cluster and prepared a key file in the pem format.
-   Users can access the Internet on the local PC.

## Procedure<a name="s006aa048ecfb4a42ad44f6bc73efa903"></a>

1.  Log in to the MRS management console and choose  **Clusters**  \>  **Active Clusters**.
2.  Click the specified MRS cluster name.

    Record  **Default Security Group**  of the Master node.

3.  Add an inbound rule to the security group of the Master node to allow data from the specified sources to access port  **22**.

    For details, see  **Virtual Private Cloud**  \>  **User Guide**  \>  **Security**  \>  **Security Group**  \>  **Adding a Security Group Rule**.

4.  Bind an elastic IP address to the Master2 node.

    See "Assigning an EIP and Binding It to an ECS" in the  _Virtual Private Cloud User Guide_  \(Network Components \> EIP \> Assigning an EIP and Binding It to an ECS\).

5.  Locally start Git Bash and run the following command to log in to the Master2 node:

    **ssh -i** _**Path of the key file**_ **linux@**_**Elastic IP address**_

6.  Run the following commands to view data forwarding configurations:

    **cat /etc/sysctl.conf | grep net.ipv4.ip\_forward**

    If  **net.ipv4.ip\_forward=1** is displayed, the forwarding function has been configured. If it is not displayed, perform [7](#lca440d7abe1c45a99d4e0b4909d6d1f0)

7.  <a name="lca440d7abe1c45a99d4e0b4909d6d1f0"></a>Modify forwarding configurations on the node.
    1.  Run the following command to switch to user  **root**:

        **sudo su - root**

    2.  Run the following commands to modify forwarding configurations:

        **echo 1 \> /proc/sys/net/ipv4/ip\_forward**

        **sed -i "s/net.ipv4.ip\_forward = 0/net.ipv4.ip\_forward = 1/g" /etc/sysctl.conf**

        **sysctl -w net.ipv4.ip\_forward=1**

    3.  Run the following command to modify the  **sshd**  configuration file:

        **vi /etc/ssh/sshd\_config**

        Press  **I** to enter the edit mode. Locate **AllowTcpForwarding** and **GatewayPorts**  and delete comment tags. Modify them as follows. Save the changes and exit.

        ```
        AllowTcpForwarding yes
        GatewayPorts yes
        ```

    4.  Run the following command to restart the sshd service:

        **service sshd restart**

8.  Run the following command to view the floating IP address:

    **ifconfig**

    In the command output,  **eth0:FI\_HUE** indicates the floating IP address of Hue and **eth0:wsom** specifies the floating IP address of MRS Manager. Record the value of **inet**.

    Run the  **exit**  command to exit.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the floating IP address of Hue cannot be queried on the Master2 node, query it on the Master 1 node and record it.  

9.  <a name="l6256e8cc11884f9786bf6fe1419c3013"></a>Run the following command to create an SSH channel supporting dynamic port forwarding:

    **ssh -i  _Path of the key file_  -v -ND** _**Local port**_ **linux@_Elastic IP address_**

    In the command, set  **Local port** to the user's local port that is not occupied. Port **8157**  is recommended.

    After the SSH channel is created, add  **-D**  to the command and run the command to start the dynamic port forwarding function. By default, the dynamic port forwarding function enables a SOCKS proxy process and monitors the user's local port. Port data will be forwarded to the Master2 node using the SSH channel.

10. Run the following command to configure the browser proxy.
    1.  Go to the Google Chrome client installation directory on the local PC.
    2.  Press  **Shift**, right-click the blank area, and choose **Open Command Window Here**  to go to the command line mode. Enter the following command:

        **chrome --proxy-server="socks5://localhost:8157" --host-resolver-rules="MAP \* 0.0.0.0 , EXCLUDE localhost" --user-data-dir=c:/tmppath --proxy-bypass-list="\*google\*com,\*gstatic.com,\*gvt\*.com,\*:80",**

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >In the preceding command,  **8157** is the local proxy port configured in [9](#l6256e8cc11884f9786bf6fe1419c3013).  


11. In the address bar of the browser, enter the address for accessing MRS Manager.

    Address format:  **https://_Floating IP address of_** **_MRS Manager_:28443/web**

    The username and password of the MRS cluster need to be entered for accessing clusters with Kerberos authentication enabled, for example, user  **admin**. They are not required for accessing clusters with Kerberos authentication disabled.

    When accessing the MRS Manager for the first time, you must add the address to the trusted site list.

12. Prepare the website access address.
    1.  Obtain the website address format and the role instance according to  [Websites](web-uis-of-open-source-components.md#s13534867d95748fdbf7322acf0bb34ca).
    2.  Click  **Services**.
    3.  Click the specified service name, for example, HDFS.
    4.  Click  **Instance** and view **Service IP** of **NameNode\(Active\)**.

13. In the address bar of the browser, enter the website address to access it.
14. When logging out of the website, terminate and close the SSH channel.

