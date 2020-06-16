# Using the Client on Another Node of a VPC<a name="EN-US_TOPIC_0125375890"></a>

## Scenario<a name="section47062638171526"></a>

After the client is prepared, users can use the client on a node outside the MRS cluster.

>![](/images/icon-note.gif) **NOTE:**   
>If the client has been installed on the node outside the MRS cluster but must be updated, update the client using the same account that is used to install the client, for example, the  **root**  account.  

## Prerequisites<a name="section3219221104310"></a>

-   An ECS has been prepared. For details about the OS and its version of the ECS, see  [Table 1](#table40818788104630).

    **Table  1**  Reference list

    <a name="table40818788104630"></a>
    <table><thead align="left"><tr id="row38578049104630"><th class="cellrowborder" valign="top" width="19.36%" id="mcps1.2.3.1.1"><p id="p37814246104630"><a name="p37814246104630"></a><a name="p37814246104630"></a>OS</p>
    </th>
    <th class="cellrowborder" valign="top" width="80.64%" id="mcps1.2.3.1.2"><p id="p43055100104630"><a name="p43055100104630"></a><a name="p43055100104630"></a>Supported Version</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row64911082104630"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.3.1.1 "><p id="p23306329104630"><a name="p23306329104630"></a><a name="p23306329104630"></a>SuSE</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.64%" headers="mcps1.2.3.1.2 "><a name="ul8764529104630"></a><a name="ul8764529104630"></a><ul id="ul8764529104630"><li>Recommended: SUSE Linux Enterprise Server 11 SP4 (SUSE 11.4)</li><li>Available: SUSE Linux Enterprise Server 11 SP3 (SUSE 11.3)</li><li>Available: SUSE Linux Enterprise Server 11 SP1 (SUSE 11.1)</li><li>Available: SUSE Linux Enterprise Server 11 SP2 (SUSE 11.2)</li></ul>
    </td>
    </tr>
    <tr id="row60240262104630"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.3.1.1 "><p id="p47623054104630"><a name="p47623054104630"></a><a name="p47623054104630"></a>RedHat</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.64%" headers="mcps1.2.3.1.2 "><a name="ul32262179104630"></a><a name="ul32262179104630"></a><ul id="ul32262179104630"><li>Recommended: Red Hat-6.6-x86_64 (Red Hat 6.6)</li><li>Available: Red Hat-6.4-x86_64 (Red Hat 6.4)</li><li>Available: Red Hat-6.5-x86_64 (Red Hat 6.5)</li><li>Available: Red Hat-6.7-x86_64 (Red Hat 6.7)</li></ul>
    </td>
    </tr>
    <tr id="row30103971104630"><td class="cellrowborder" valign="top" width="19.36%" headers="mcps1.2.3.1.1 "><p id="p22502558104630"><a name="p22502558104630"></a><a name="p22502558104630"></a>CentOS</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.64%" headers="mcps1.2.3.1.2 "><a name="ul10767914104630"></a><a name="ul10767914104630"></a><ul id="ul10767914104630"><li>Available: CentOS-6.4 (CentOS 6.4)</li><li>Available: CentOS-6.5 (CentOS 6.5)</li><li>Available: CentOS-6.6 (CentOS 6.6)</li><li>Available: CentOS-6.7 (CentOS 6.7)</li><li>Available: CentOS-7.2 (CentOS 7.2)</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    For example, a user can select the enterprise image  **Enterprise\_SLES11\_SP4\_latest\(4GB\)** or standard image **Standard\_CentOS\_7.2\_latest\(4GB\)**  to prepare the OS for an ECS.

    In addition, sufficient disk space is allocated for the ECS, for example,  **40 GB**.

-   The ECS and the MRS cluster are in the same VPC.
-   The IP address configured for the NIC of the ECS is in the same network segment as the IP address of the MRS cluster.
-   The security group of the ECS is the same as that of the Master node of the MRS cluster.

    If this requirement is not met, modify the ECS security group or configure the inbound and outbound rules of the ECS security group to allow the ECS security group to be accessed by all security groups of MRS cluster nodes.

    For details about how to create an ECS that meets this requirement, see "Creating an ECS" under the "Getting Started" chapter in the  _Elastic Cloud Server User Guide_.

-   To enable users to log in to a Linux ECS using a password \(SSH\), see "Logging In to a Linux ECS Using a Password \(SSH\)" in the  _Elastic Cloud Server User Guide_ \(**Getting Started \> Logging In to an ECS \> Logging In to a Linux ECS Using a Password \(SSH\)**\).

## Procedure<a name="section6090605618256"></a>

1.  Create an ECS that meets the requirements in the prerequisites.
2.  Log in to MRS Manager.
3.  Click  **Service**, and click **Download Client**.
4.  In  **Client Type**, select **All client files**.
5.  In  **Download Path**, select **Remote host**.
6.  Set  **Host IP Address** to the IP address of the ECS, set **Host Port** to **22**, and set **Save Path** to **/home/linux**.
    -   If the default port  **22** for logging in to an ECS using SSH has been changed, set **Host Port**  to the new port.
    -   **Save Path**  contains a maximum of 256 characters.

7.  Set  **Login User** to **linux**.

    If other users are used, ensure that the users have read, write, and execute permission on the save path.

8.  In  **SSH Private Key**, select and upload the private key used for creating the ECS.
9.  Click  **OK**  to start downloading the client to the ECS.

    If the following information is displayed, the client package is successfully saved. Click  **Close**.

    ```
    Client files downloaded to the remote host successfully.
    ```

10. Log in to the ECS using VNC. See "Logging In to a Linux ECS Using VNC" in the  _Elastic Cloud Server User Guide_ \(**Getting Started \> Logging In to an ECS \> Logging In to a Linux ECS Using VNC**\).

    All standard \(Standard\_xxx\) and enterprise \(Enterprise\_xxx\) images support Cloud-Init. The preset username for Cloud-Init is  **linux**. The password is randomly generated and is displayed on the VNC login page by default. If you have changed the password, log in to the ECS using the new password. See "How Do I Log In to an ECS Once All Images Support Cloud-Init?" in the _Elastic Cloud Server User Guide_ \(**FAQs \> Login FAQs \> How Do I Log In to an ECS Once All Images Support Cloud-Init?**\). It is recommended that you change the password upon the first login.

11. On the ECS, switch to user  **root** and copy the installation package to the **/opt**  directory.

    **sudo su - root**

    **cp /home/linux/MRS\_Services\_Client.tar /opt**

12. Run the following command in the  **/opt**  directory to decompress the package and obtain the verification file and the configuration package of the client:

    **tar -xvf MRS\_Services\_Client.tar**

13. Run the following command to verify the configuration package of the client:

    **sha256sum -c MRS\_Services\_ClientConfig.tar.sha256**

    The command output is as follows:

    ```
    MRS_Services_ClientConfig.tar: OK
    ```

14. Run the following command to decompress  **MRS\_Services\_ClientConfig.tar**:

    **tar -xvf MRS\_Services\_ClientConfig.tar**

15. Run the following command to install the client to a new directory, for example,  **/opt/hadoopclient**. A directory is automatically generated during installation.

    **sh /opt/MRS\_Services\_ClientConfig/install.sh /opt/hadoopclient**

    If the following information is displayed, the client is successfully installed:

    ```
    Components client installation is complete.
    ```

16. Check whether the IP address of the ECS node is connected to the IP address of the cluster Master node.

    For example, run the following command:  **ping** _Master node IP address_.

    -   If yes, go to  [17](#li6406429718107).
    -   If no, check whether the VPC and security group are correct and whether the ECS and the MRS cluster are in the same VPC and security group, and go to  [17](#li6406429718107).

17. <a name="li6406429718107"></a>Run the following command to configure the environment variable:

    **source /opt/hadoopclient/bigdata\_env**

18. If the Kerberos authentication is enabled for the current cluster, run the following command to authenticate users. If the Kerberos authentication is disabled for the current cluster, skip this step.

    **kinit** **_MRS cluster user_**

    For example,  **kinit admin**.

19. Run the client command of the component.

    For example, run the following command to query the HDFS directory.

    **hdfs dfs -ls /**


