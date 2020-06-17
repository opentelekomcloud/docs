# Collecting Container Logs from Specified Paths<a name="cce_01_0018"></a>

CCE allows you to configure policies for collecting, managing, and analyzing workload logs periodically to prevent logs from being over-sized.

This section describes how to collect container logs from specified paths. If you want to collect standard output logs of containers, see  [Collecting Standard Output Logs of Containers](collecting-standard-output-logs-of-containers.md).

## Procedure<a name="section1951732710"></a>

1.  When creating a  containerized workload, add a  container. Then, expand  **Log Policies**.

    **Figure  1**  Container logs<a name="fig877312327505"></a>  
    ![](figures/container-logs.png "container-logs")

2.  In the  **Log Policies**  area, click  **Add Log Policy**. Configure parameters in the log policy. The following uses Nginx as an example.

    **Figure  2**  Adding log policies<a name="fig19856172153216"></a>  
    ![](figures/adding-log-policies.png "adding-log-policies")

3.  Set  **Storage Type**. There are two storage types:  **Host Path**  and  **Container Path**.
    -   **Host Path**: You can mount a path on the host to a specified container path. Set the log policy parameters as follows:

        **Table  1**  Parameters for adding log policies \(Host Path\)

        <a name="table115901715550"></a>
        <table><thead align="left"><tr id="row45851074554"><th class="cellrowborder" valign="top" width="22.12%" id="mcps1.2.3.1.1"><p id="p115843785517"><a name="p115843785517"></a><a name="p115843785517"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77.88000000000001%" id="mcps1.2.3.1.2"><p id="p12584573550"><a name="p12584573550"></a><a name="p12584573550"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1458511725510"><td class="cellrowborder" valign="top" width="22.12%" headers="mcps1.2.3.1.1 "><p id="p115855785514"><a name="p115855785514"></a><a name="p115855785514"></a>Storage Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="77.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p058514725519"><a name="p058514725519"></a><a name="p058514725519"></a>Set this parameter to <strong id="b15588848114310"><a name="b15588848114310"></a><a name="b15588848114310"></a>Host Path</strong>.</p>
        </td>
        </tr>
        <tr id="row75867795518"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p75869775515"><a name="p75869775515"></a><a name="p75869775515"></a><strong id="b17502441102718"><a name="b17502441102718"></a><a name="b17502441102718"></a>Add Container Path</strong></p>
        </td>
        </tr>
        <tr id="row19587147165512"><td class="cellrowborder" valign="top" width="22.12%" headers="mcps1.2.3.1.1 "><p id="p1158647155518"><a name="p1158647155518"></a><a name="p1158647155518"></a>Container Path</p>
        </td>
        <td class="cellrowborder" valign="top" width="77.88000000000001%" headers="mcps1.2.3.1.2 "><div class="p" id="p358711715554"><a name="p358711715554"></a><a name="p358711715554"></a>Container path (for example, <strong id="b8656121314711"><a name="b8656121314711"></a><a name="b8656121314711"></a>/tmp</strong>) to which the host path volume will be mounted.<div class="notice" id="note155879745516"><a name="note155879745516"></a><a name="note155879745516"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul14587570556"></a><a name="ul14587570556"></a><ul id="ul14587570556"><li>The container path cannot be a system directory, such as <strong id="b129971541125317"><a name="b129971541125317"></a><a name="b129971541125317"></a>/</strong> or <strong id="b109981941175318"><a name="b109981941175318"></a><a name="b109981941175318"></a>/var/run</strong>. Otherwise, the container may not function properly. You are advised to mount the container to an empty directory. If the directory is not empty, ensure that there are no files affecting container startup in the directory. Otherwise, such files will be replaced, resulting in failures to start the container and create the workload.</li><li>When the container is mounted to a high-risk directory, you are advised to use an account with minimum permissions to start the container; otherwise, high-risk files on the host machine may be damaged.</li></ul>
        </div></div>
        </div>
        </td>
        </tr>
        <tr id="row6588187135510"><td class="cellrowborder" valign="top" width="22.12%" headers="mcps1.2.3.1.1 "><p id="p758720775520"><a name="p758720775520"></a><a name="p758720775520"></a>Extended Host Path</p>
        </td>
        <td class="cellrowborder" valign="top" width="77.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p158737185514"><a name="p158737185514"></a><a name="p158737185514"></a>A level-3 directory is added to the original volume directory/subdirectory. You can easily obtain the files output by a single <span class="keyword" id="keyword1142267981799"><a name="keyword1142267981799"></a><a name="keyword1142267981799"></a>Pod</span>.</p>
        <a name="ul1358877135514"></a><a name="ul1358877135514"></a><ul id="ul1358877135514"><li><strong id="b67128281231"><a name="b67128281231"></a><a name="b67128281231"></a>None</strong>: No extended path is configured.</li><li><strong id="b37109352310"><a name="b37109352310"></a><a name="b37109352310"></a>PodUID</strong>: ID of a pod.</li><li><strong id="b1246417411639"><a name="b1246417411639"></a><a name="b1246417411639"></a>PodName</strong>: name of a pod.</li><li><strong id="b1232314820315"><a name="b1232314820315"></a><a name="b1232314820315"></a>PodUID/ContainerName</strong>: ID of a pod or name of a container.</li><li><strong id="b15921753534"><a name="b15921753534"></a><a name="b15921753534"></a>PodName/ContainerName</strong>: name of a pod or container.</li></ul>
        </td>
        </tr>
        <tr id="row85891275552"><td class="cellrowborder" valign="top" width="22.12%" headers="mcps1.2.3.1.1 "><p id="p258847105513"><a name="p258847105513"></a><a name="p258847105513"></a>Log Dumping</p>
        </td>
        <td class="cellrowborder" valign="top" width="77.88000000000001%" headers="mcps1.2.3.1.2 "><p id="p106131316238"><a name="p106131316238"></a><a name="p106131316238"></a>Log files in <strong id="b1261316312237"><a name="b1261316312237"></a><a name="b1261316312237"></a>.log</strong>, <strong id="b196131313230"><a name="b196131313230"></a><a name="b196131313230"></a>.trace</strong>, and <strong id="b1561316372312"><a name="b1561316372312"></a><a name="b1561316372312"></a>.out</strong> formats can be collected.</p>
        <a name="ul1261353202317"></a><a name="ul1261353202317"></a><ul id="ul1261353202317"><li><strong id="b861310319237"><a name="b861310319237"></a><a name="b861310319237"></a>Enabled</strong>: A log file larger than 50 MB will be dumped and a maximum of 20 dump files will be retained.</li></ul>
        <a name="ul18126151412317"></a><a name="ul18126151412317"></a><ul id="ul18126151412317"><li><strong id="b196131038235"><a name="b196131038235"></a><a name="b196131038235"></a>Disabled</strong>: The default Docker dumping mechanism is used.</li></ul>
        </td>
        </tr>
        </tbody>
        </table>

    -   **Container Path**: Logs are exported only to the container path. You do not need to mount the host path. Set the log policy parameters as follows:

        >![](/images/icon-note.gif) **NOTE:**   
        >This function requires that the ICAgent be upgraded to 5.10.79 or a later version.  

        **Table  2**  Parameters for adding log policies \(Container Path\)

        <a name="table1940632515364"></a>
        <table><thead align="left"><tr id="row1739912520361"><th class="cellrowborder" valign="top" width="22.08%" id="mcps1.2.3.1.1"><p id="p7399142512364"><a name="p7399142512364"></a><a name="p7399142512364"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77.92%" id="mcps1.2.3.1.2"><p id="p1339932553610"><a name="p1339932553610"></a><a name="p1339932553610"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row12882033163811"><td class="cellrowborder" valign="top" width="22.08%" headers="mcps1.2.3.1.1 "><p id="p148836339383"><a name="p148836339383"></a><a name="p148836339383"></a>Storage Type</p>
        </td>
        <td class="cellrowborder" valign="top" width="77.92%" headers="mcps1.2.3.1.2 "><p id="p588363314384"><a name="p588363314384"></a><a name="p588363314384"></a>Set this parameter to <strong id="b341864818552"><a name="b341864818552"></a><a name="b341864818552"></a>Container Path</strong>.</p>
        </td>
        </tr>
        <tr id="row1440272519365"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p164013253366"><a name="p164013253366"></a><a name="p164013253366"></a><strong id="b2116925853"><a name="b2116925853"></a><a name="b2116925853"></a>Add Container Path</strong></p>
        </td>
        </tr>
        <tr id="row19403122523618"><td class="cellrowborder" valign="top" width="22.08%" headers="mcps1.2.3.1.1 "><p id="p44021125103615"><a name="p44021125103615"></a><a name="p44021125103615"></a>Container Path</p>
        </td>
        <td class="cellrowborder" valign="top" width="77.92%" headers="mcps1.2.3.1.2 "><div class="p" id="p840332573617"><a name="p840332573617"></a><a name="p840332573617"></a>Container path (for example, <strong id="b6256372566"><a name="b6256372566"></a><a name="b6256372566"></a>/tmp</strong>) to which the host path volume will be mounted.<div class="notice" id="note124031525163613"><a name="note124031525163613"></a><a name="note124031525163613"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul540382573617"></a><a name="ul540382573617"></a><ul id="ul540382573617"><li>The container path cannot be a system directory, such as <strong id="b16693194125613"><a name="b16693194125613"></a><a name="b16693194125613"></a>/</strong> or <strong id="b116957413565"><a name="b116957413565"></a><a name="b116957413565"></a>/var/run</strong>. Otherwise, the container may not function properly. You are advised to mount the container to an empty directory. If the directory is not empty, ensure that there are no files affecting container startup in the directory. Otherwise, such files will be replaced, resulting in failures to start the container and create the workload.</li><li>If the file system is mounted to a high-risk directory, you are advised to use an account with minimum permissions to start the container; otherwise, high-risk files on the host machine may be damaged.</li></ul>
        </div></div>
        </div>
        </td>
        </tr>
        <tr id="row1840532563617"><td class="cellrowborder" valign="top" width="22.08%" headers="mcps1.2.3.1.1 "><p id="p6404122512367"><a name="p6404122512367"></a><a name="p6404122512367"></a>Log Dumping</p>
        </td>
        <td class="cellrowborder" valign="top" width="77.92%" headers="mcps1.2.3.1.2 "><p id="p34056252367"><a name="p34056252367"></a><a name="p34056252367"></a>Log files in the format of .log, .trace, and .out. are supported. If the size of a log file is greater than 50 MB, a maximum of 20 files are dumped.</p>
        <a name="ul12405325153613"></a><a name="ul12405325153613"></a><ul id="ul12405325153613"><li><strong id="b4724126135720"><a name="b4724126135720"></a><a name="b4724126135720"></a>Enabled</strong>: Log files are dumped.</li><li><strong id="b28101931194413"><a name="b28101931194413"></a><a name="b28101931194413"></a>Disabled</strong>: Log files are not dumped.</li></ul>
        </td>
        </tr>
        </tbody>
        </table>

4.  Click  **OK**.
5.  View logs.

    After the workload is created, access Nginx. Go to the workload details page and click the  **Log**  button in the upper right corner to view the log details.


