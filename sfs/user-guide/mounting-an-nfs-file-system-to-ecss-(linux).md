# Mounting an NFS File System to ECSs \(Linux\)<a name="EN-US_TOPIC_0034428728"></a>

After creating a file system, you need to mount the file system to ECSs so that ECSs can share the file system.

## Prerequisites<a name="section27225646153519"></a>

-   You have checked the type of operating system of each ECS. Different operating systems use different commands to install the NFS client.
-   You have created a file system and have obtained the shared path of the file system.
-   The ECSs to which a file system is mounted belong to the same VPC as the file system.
-   The IP address of the DNS server for resolving the domain names of the file systems has been configured on the ECS. 

## Procedure<a name="section62423454145852"></a>

1.  Log in to the ECS as user  **root**.
2.  Install the NFS client.
    1.  Run the following command to check whether the NFS software package is installed.

        -   On CentOS, Red Hat, Oracle Enterprise Linux, SUSE, EulerOS, Fedora, or OpenSUSE:

            **rpm -qa|grep nfs**

        -   On Debian or Ubuntu:

            **dpkg -l nfs-common**

        If a command output similar to the following is displayed, the NFS software package has been installed and you can go to  [3](#li6090605610251). If nothing is displayed, go to  [2.b](#li4299938211109).

        -   On CentOS, Red Hat, EulerOS, Fedora, or Oracle Enterprise Linux:

            ```
            libnfsidmap
            nfs-utils
            ```

        -   On SUSE or OpenSUSE:

            ```
            nfsidmap
            nfs-client
            ```

        -   On Debian or Ubuntu:

            ```
            nfs-common
            ```

    2.  <a name="li4299938211109"></a>Run the following command to install the NFS software package.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >The following commands require that ECSs be connected to the Internet. Otherwise, the installation will fail. Installing NFS clients requires enabling effective software repositories. Installing NFS clients will fail if no software repository is enabled or the ECS does not have any software repository. If installing NFS clients fails, refer to  [Enabling or Adding a Software Repository](enabling-or-adding-a-software-repository.md).  

        -   On CentOS, Red Hat, EulerOS, Fedora, or Oracle Enterprise Linux:

            **sudo yum -y install nfs-utils**

        -   On Debian or Ubuntu:

            **sudo apt-get install nfs-common**

        -   On SUSE or OpenSUSE:

            **zypper install nfs-client**


3.  <a name="li6090605610251"></a>Run the following command to check whether the domain name in the file system shared path can be resolved. 

    **nslookup **_File system domain name_

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   A file system domain name is just a part of the shared path. For example, sfs-nas1._xxxx_.com. You can obtain a file system domain name from the shared path of a file system. In this step, you are not supposed to enter the entire shared path but only the domain name.  
    >-   If the  **nslookup**  command cannot be used, install the  **bind-utils**  software package by running the  **yum install bind-utils**  command.  

    -   If yes, go to  [4](#li4945457518115).
    -   If no, configure the DNS server IP address and then mount the file system. For details, see  [Configuring DNS](configuring-dns.md).

4.  <a name="li4945457518115"></a>Run the following command to create a local path for mounting the file system.

    **mkdir** _Local path_

5.  Run the following command to mount the file system to the ECSs. Currently, the service supports mounting only file systems complying with NFSv3 to ECSs running Linux.  [Table 1](#table199544014035)  describes the variables.

    **mount -t nfs -o vers=3,timeo=600,noresvport,nolock** _Shared path_ _Local path_

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >After an ECS where file systems have been mounted restarts, it loses the file system mount information. You can configure automatic mount in the  **fstab**  file to ensure that an ECS automatically mounts file systems when it restarts. For details, see  [Mounting a File System Automatically](mounting-a-file-system-automatically.md).  

    **Table  1**  Parameter description

    <a name="table199544014035"></a>
    <table><thead align="left"><tr id="row12186162151218"><th class="cellrowborder" valign="top" width="23.119999999999997%" id="mcps1.2.3.1.1"><p id="p151861721201215"><a name="p151861721201215"></a><a name="p151861721201215"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="76.88000000000001%" id="mcps1.2.3.1.2"><p id="p12186102119127"><a name="p12186102119127"></a><a name="p12186102119127"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1087259185"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p1888357181"><a name="p1888357181"></a><a name="p1888357181"></a>vers</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p8882551818"><a name="p8882551818"></a><a name="p8882551818"></a>File system version. Currently, only NFSv3 is supported, so the value is fixed to <strong id="b987819218276"><a name="b987819218276"></a><a name="b987819218276"></a>3</strong>.</p>
    </td>
    </tr>
    <tr id="row1166715112182"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p1566901201816"><a name="p1566901201816"></a><a name="p1566901201816"></a>timeo</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p566914112182"><a name="p566914112182"></a><a name="p566914112182"></a>The waiting time before the NFS client retransmits a request. The unit is 0.1 second. Recommended value: <strong id="b650611862711"><a name="b650611862711"></a><a name="b650611862711"></a>600</strong></p>
    </td>
    </tr>
    <tr id="row18604134217211"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p1348720171934"><a name="p1348720171934"></a><a name="p1348720171934"></a>resvport/noresvport</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p6487111716313"><a name="p6487111716313"></a><a name="p6487111716313"></a>Whether the confidential source port is used for server connection. By default, <strong id="b3816112518328"><a name="b3816112518328"></a><a name="b3816112518328"></a>resvport</strong> indicates that the confidential port is used, and <strong id="b81191248153312"><a name="b81191248153312"></a><a name="b81191248153312"></a>noresvport</strong> indicates that the confidential port is not used. The kernel version is 2.6.28 or later.</p>
    <p id="p164871317236"><a name="p164871317236"></a><a name="p164871317236"></a>You are advised to set this parameter to <strong id="b19481828112214"><a name="b19481828112214"></a><a name="b19481828112214"></a>noresvport</strong> so that a new TCP port can be used when the network is reconnected. This ensures that the connection is not interrupted when the network recovers from a fault.</p>
    </td>
    </tr>
    <tr id="row1611193815390"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p711113843912"><a name="p711113843912"></a><a name="p711113843912"></a>lock/nolock</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p526822214011"><a name="p526822214011"></a><a name="p526822214011"></a>Whether to lock files on the server using the NLM protocol. If <strong id="b18633113319211"><a name="b18633113319211"></a><a name="b18633113319211"></a>nolock</strong> is selected, the lock is valid for applications on one host. For applications on another host, the lock is invalid. Recommended value: <strong id="b16238101472711"><a name="b16238101472711"></a><a name="b16238101472711"></a>nolock</strong> If this parameter is not specified, <strong id="b690794263"><a name="b690794263"></a><a name="b690794263"></a>lock</strong> is selected by default. In this case, other servers cannot write data to the file system.</p>
    </td>
    </tr>
    <tr id="row13186221111215"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p121861521161211"><a name="p121861521161211"></a><a name="p121861521161211"></a>Shared path</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p018672191214"><a name="p018672191214"></a><a name="p018672191214"></a>The format for an SFS file system is <em id="i1991716401405"><a name="i1991716401405"></a><a name="i1991716401405"></a>File system domain name</em>:/<em id="i592094011011"><a name="i592094011011"></a><a name="i592094011011"></a>Path</em>, for example, <strong id="b99231540204"><a name="b99231540204"></a><a name="b99231540204"></a>example.com:/share-</strong><em id="i1992354014012"><a name="i1992354014012"></a><a name="i1992354014012"></a>xxx</em>. See <a href="#fig929579017114">Figure 1</a>.</p>
    <div class="note" id="note1918652110122"><a name="note1918652110122"></a><a name="note1918652110122"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul16921194345613"></a><a name="ul16921194345613"></a><ul id="ul16921194345613"><li><em id="i842352697163853"><a name="i842352697163853"></a><a name="i842352697163853"></a>x</em> is a digit or letter.</li><li>If the shared path is too long to display completely, expand the column to view the full shared path.</li><li>Hover the mouse over the shared path to display the complete <strong id="b9930165141013"><a name="b9930165141013"></a><a name="b9930165141013"></a>mount</strong> command.</li></ul>
    </div></div>
    </td>
    </tr>
    <tr id="row13186122161215"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p1118632112125"><a name="p1118632112125"></a><a name="p1118632112125"></a>Local path</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p10186182112124"><a name="p10186182112124"></a><a name="p10186182112124"></a>Local path on the ECS, used to mount the file system, for example, <span class="filepath" id="filepath52140702094047"><a name="filepath52140702094047"></a><a name="filepath52140702094047"></a><b>/local_path</b></span>.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Figure  1**  Shared Path<a name="fig929579017114"></a>  
    ![](figures/shared-path.png "shared-path")

    For more mounting parameters for performance optimization during file system mounting, see  [Table 2](#table372185017537). Use commas \(,\) to separate parameters. The following command is an example:

    **mount -t nfs -o vers=3,timeo=600,nolock,rsize=1048576,wsize=1048576,hard,retrans=3,noresvport,async,noatime,nodiratime** _Shared path_ _Local path_

    **Table  2**  Parameters for file system mounting

    <a name="table372185017537"></a>
    <table><thead align="left"><tr id="row1872545055319"><th class="cellrowborder" valign="top" width="23.119999999999997%" id="mcps1.2.3.1.1"><p id="p8727850165312"><a name="p8727850165312"></a><a name="p8727850165312"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="76.88000000000001%" id="mcps1.2.3.1.2"><p id="p9729125015313"><a name="p9729125015313"></a><a name="p9729125015313"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12731450195314"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p14732145075316"><a name="p14732145075316"></a><a name="p14732145075316"></a>rsize</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p18978184263717"><a name="p18978184263717"></a><a name="p18978184263717"></a>Maximum number of bytes that can be read from the server each time. The actual data is less than or equal to the value of this parameter. The value of <strong id="b6869125132113"><a name="b6869125132113"></a><a name="b6869125132113"></a>rsize</strong> must be a positive integer that is a multiple of <strong id="b5850141911509"><a name="b5850141911509"></a><a name="b5850141911509"></a>1024</strong>. If the entered value is smaller than <strong id="b85121122205014"><a name="b85121122205014"></a><a name="b85121122205014"></a>1024</strong>, the value is automatically set to <strong id="b267317247508"><a name="b267317247508"></a><a name="b267317247508"></a>4096</strong>. If the entered value is greater than <strong id="b1731412735019"><a name="b1731412735019"></a><a name="b1731412735019"></a>1048576</strong>, the value is automatically set to <strong id="b10446122914508"><a name="b10446122914508"></a><a name="b10446122914508"></a>1048576</strong>. By default, the setting is performed after the negotiation between the server and the client.</p>
    <p id="p71725635411"><a name="p71725635411"></a><a name="p71725635411"></a>You are advised to set this parameter to the maximum value <strong id="b1814819439512"><a name="b1814819439512"></a><a name="b1814819439512"></a>1048576</strong>.</p>
    </td>
    </tr>
    <tr id="row0748165025318"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p87501550205314"><a name="p87501550205314"></a><a name="p87501550205314"></a>wsize</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p996335265410"><a name="p996335265410"></a><a name="p996335265410"></a>Maximum number of bytes that can be written to the server each time. The actual data is less than or equal to the value of this parameter. The value of <strong id="b18685126162610"><a name="b18685126162610"></a><a name="b18685126162610"></a>wsize</strong> must be a positive integer that is a multiple of <strong id="b12716163595015"><a name="b12716163595015"></a><a name="b12716163595015"></a>1024</strong>. If the entered value is smaller than <strong id="b1294011374507"><a name="b1294011374507"></a><a name="b1294011374507"></a>1024</strong>, the value is automatically set to <strong id="b1412984065010"><a name="b1412984065010"></a><a name="b1412984065010"></a>4096</strong>. If the entered value is greater than <strong id="b9554144312508"><a name="b9554144312508"></a><a name="b9554144312508"></a>1048576</strong>, the value is automatically set to <strong id="b376124115504"><a name="b376124115504"></a><a name="b376124115504"></a>1048576</strong>. By default, the setting is performed after the negotiation between the server and the client.</p>
    <p id="p8579149203711"><a name="p8579149203711"></a><a name="p8579149203711"></a>You are advised to set this parameter to the maximum value <strong id="b1578018476514"><a name="b1578018476514"></a><a name="b1578018476514"></a>1048576</strong>.</p>
    </td>
    </tr>
    <tr id="row15831677265"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p2583875267"><a name="p2583875267"></a><a name="p2583875267"></a>soft/hard</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p1230732603814"><a name="p1230732603814"></a><a name="p1230732603814"></a><strong id="b111340380266"><a name="b111340380266"></a><a name="b111340380266"></a>soft</strong> indicates that a file system is mounted in soft mount mode. In this mode, if an NFS request times out, the client returns an error to the invoking program. <strong id="b1954313111279"><a name="b1954313111279"></a><a name="b1954313111279"></a>hard</strong> indicates that a file system is mounted in hard mount mode. In this mode, if the NFS request times out, the client continues to request until the request is successful.</p>
    <p id="p105687113555"><a name="p105687113555"></a><a name="p105687113555"></a>The default value is <strong id="b8530105419447"><a name="b8530105419447"></a><a name="b8530105419447"></a>hard</strong>.</p>
    </td>
    </tr>
    <tr id="row145513217264"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p145611212617"><a name="p145611212617"></a><a name="p145611212617"></a>retrans</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p153123612550"><a name="p153123612550"></a><a name="p153123612550"></a>Number of retransmission times before the client returns an error. The default value is <strong id="b84235270620375"><a name="b84235270620375"></a><a name="b84235270620375"></a>3</strong>.</p>
    </td>
    </tr>
    <tr id="row14791253113117"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p379253133118"><a name="p379253133118"></a><a name="p379253133118"></a>resvport/noresvport</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p4871911185519"><a name="p4871911185519"></a><a name="p4871911185519"></a>Whether the confidential source port is used for server connection. By default, <strong id="b822023932"><a name="b822023932"></a><a name="b822023932"></a>resvport</strong> indicates that the confidential port is used, and <strong id="b680567525"><a name="b680567525"></a><a name="b680567525"></a>noresvport</strong> indicates that the confidential port is not used. The kernel version is 2.6.28 or later.</p>
    <p id="p85214165212"><a name="p85214165212"></a><a name="p85214165212"></a>You are advised to set this parameter to <strong id="b804415169"><a name="b804415169"></a><a name="b804415169"></a>noresvport</strong> so that a new TCP port can be used when the network is reconnected. This ensures that the connection is not interrupted when the network recovers from a fault.</p>
    </td>
    </tr>
    <tr id="row1841014819396"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p09771344017"><a name="p09771344017"></a><a name="p09771344017"></a>sync/async</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p2068210194418"><a name="p2068210194418"></a><a name="p2068210194418"></a><strong id="b1620144254013"><a name="b1620144254013"></a><a name="b1620144254013"></a>sync</strong> indicates that data is written to the server immediately. <strong id="b11896329194220"><a name="b11896329194220"></a><a name="b11896329194220"></a>async</strong> indicates that data is first written to the cache before being written to the server.</p>
    <p id="p1517011424019"><a name="p1517011424019"></a><a name="p1517011424019"></a>Synchronous write requires that an NFS server returns a success message only after all data is written to the server, which brings long latency. The recommended value is <strong id="b1080193514469"><a name="b1080193514469"></a><a name="b1080193514469"></a>async</strong>.</p>
    </td>
    </tr>
    <tr id="row333111388401"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p2484144104013"><a name="p2484144104013"></a><a name="p2484144104013"></a>noatime</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p1928305111402"><a name="p1928305111402"></a><a name="p1928305111402"></a>If you do not need to record the file access time, set this parameter. This prevents overheads caused by access time modification during frequent access.</p>
    </td>
    </tr>
    <tr id="row121441656114020"><td class="cellrowborder" valign="top" width="23.119999999999997%" headers="mcps1.2.3.1.1 "><p id="p115761174114"><a name="p115761174114"></a><a name="p115761174114"></a>nodiratime</p>
    </td>
    <td class="cellrowborder" valign="top" width="76.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p786308184113"><a name="p786308184113"></a><a name="p786308184113"></a>If you do not need to record the directory access time, set this parameter. This prevents overheads caused by access time modification during frequent access.</p>
    </td>
    </tr>
    </tbody>
    </table>

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >You are advised to use the default values for the parameters without use recommendations.  

6.  Run the following command to view the mounted file system.

    **mount -l**

    If the command output contains the following information, the mount is successful.

    ```
    example.com:/share-xxx on /local_path type nfs (rw,vers=3,timeo=600,nolock,addr=)
    ```

7.  After the file system is mounted successfully, you can access the file system on the ECSs to read or write data.

    If the mounting fails or times out, rectify the fault by referring to  [Troubleshooting](troubleshooting.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The supported maximum size of a file to be written is 240 TB.  


