# Managing a StatefulSet<a name="cce_01_0158"></a>

After a StatefulSet is created, you can upgrade, scale, monitor, or delete it, as well as edit its YAML file and view its logs.

## Viewing StatefulSet Logs<a name="section1368611276"></a>

You can view logs of StatefulSets.

1.  Log in to the CE console. In the navigation pane, choose  **Workloads**  \>  **StatefulSets**.
2.  In the same row as the StatefulSet you will view, click  **Logs**.

    In the displayed  **Logs**  window, view the logs generated in the last 5 minutes, 30 minutes, or 1 hour.


## Upgrading a StatefulSet<a name="section20612124812473"></a>

CCE enables you to quickly and hitlessly upgrade a StatefulSets by replacing its image or image version.

Before replacing an image or image version, upload the new image to the SWR service. For details, see  [Image Repository](image_repository).

>![](/images/icon-note.gif) **NOTE:**   
>Before performing an in-place StatefulSet upgrade, you must manually delete old pods. Otherwise, the upgrade status is always displayed as  **Upgrading**.  

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **StatefulSets**, and click  **Upgrade**  for the StatefulSet to be upgraded.
2.  Upgrade the StatefulSet.
    -   To replace the StatefulSet image, click  **Replace Image**  and select a new image.
    -   To replace the StatefulSet image version, select a new version from the  **Image Version**  drop-down list.
    -   To change the container name, click  ![](figures/icon-edit.png)  next to  **Container Name**  and enter a new name.
    -   Configure advanced settings.

        **Table  1**  Advanced settings

        <a name="table1476874819155"></a>
        <table><thead align="left"><tr id="row97643486154"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p87643487159"><a name="p87643487159"></a><a name="p87643487159"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p20764164812158"><a name="p20764164812158"></a><a name="p20764164812158"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row8765144819159"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p10764748141514"><a name="p10764748141514"></a><a name="p10764748141514"></a>Lifecycle</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p2764648111514"><a name="p2764648111514"></a><a name="p2764648111514"></a>Commands that are executed in each lifecycle phase of a container.</p>
        <a name="ul1376517481158"></a><a name="ul1376517481158"></a><ul id="ul1376517481158"><li><strong id="b1667873411815"><a name="b1667873411815"></a><a name="b1667873411815"></a>Startup Command</strong>: executed when the container is started. For more information, see <a href="setting-container-startup-commands.md">Setting Container Startup Commands</a>.</li><li><strong id="b19360679196"><a name="b19360679196"></a><a name="b19360679196"></a>Post-Start Processing</strong>: executed after the container is successfully run. For more information, see <a href="setting-container-lifecycle-parameters.md">Setting Container Lifecycle Parameters</a>.</li><li><strong id="b1848181921916"><a name="b1848181921916"></a><a name="b1848181921916"></a>Pre-Stop Processing</strong>: executed to delete logs or temporary files befosre the container stops. For more information, see <a href="setting-container-lifecycle-parameters.md">Setting Container Lifecycle Parameters</a>.</li></ul>
        </td>
        </tr>
        <tr id="row1176517482157"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1476524816158"><a name="p1476524816158"></a><a name="p1476524816158"></a>Health Check</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><div class="p" id="p3765648151514"><a name="p3765648151514"></a><a name="p3765648151514"></a>The system checks whether containers and services are running properly. Two types of probes are set: workload liveness probe and workload service probe. For more information, see <a href="setting-health-check-for-a-container.md">Setting Health Check for a Container</a>.<a name="ul376504811512"></a><a name="ul376504811512"></a><ul id="ul376504811512"><li><strong id="b12894145141912"><a name="b12894145141912"></a><a name="b12894145141912"></a>Workload Liveness Probe</strong>: Restarts the container when detecting that the container instance is unhealthy.</li><li><strong id="b11317512191"><a name="b11317512191"></a><a name="b11317512191"></a>Workload Service Probe</strong>: Sets the workload to the unready state when detecting that the workload's container instance is unhealthy. In this way, the service traffic will not be directed to the container instance.</li></ul>
        </div>
        </td>
        </tr>
        <tr id="row876794814150"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p5765248181514"><a name="p5765248181514"></a><a name="p5765248181514"></a>Environment Variables</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1276694821518"><a name="p1276694821518"></a><a name="p1276694821518"></a>Environment variables are usually to store parameter values. To add environment variables to a container, click <strong id="b2885183152415"><a name="b2885183152415"></a><a name="b2885183152415"></a>Add Environment Variables</strong> on the <strong id="b1588693162411"><a name="b1588693162411"></a><a name="b1588693162411"></a>Environment Variables</strong> tab page. Currently, there are three types of environment variables:</p>
        <a name="ul3766148101511"></a><a name="ul3766148101511"></a><ul id="ul3766148101511"><li><strong id="b63311421145410"><a name="b63311421145410"></a><a name="b63311421145410"></a>Added manually</strong>: Set <strong id="b733222112548"><a name="b733222112548"></a><a name="b733222112548"></a>Variable Name</strong> and <strong id="b1633262111544"><a name="b1633262111544"></a><a name="b1633262111544"></a>Variable Value/Reference</strong>.</li><li><strong id="b19989924125412"><a name="b19989924125412"></a><a name="b19989924125412"></a>Added from Secret</strong>: Set <strong id="b598982455416"><a name="b598982455416"></a><a name="b598982455416"></a>Variable Name</strong> and select the desired secret name and data. A secret must be created in advance. For details, see <a href="creating-a-secret.md">Creating a Secret</a>.</li><li><strong id="b12273388549"><a name="b12273388549"></a><a name="b12273388549"></a>Added from ConfigMap</strong>: Set <strong id="b1822833815414"><a name="b1822833815414"></a><a name="b1822833815414"></a>Variable Name</strong> and select the desired ConfigMap name and data. A ConfigMap must be created in advance. For details, see <a href="creating-a-configmap.md">Creating a ConfigMap</a>.</li></ul>
        <div class="note" id="note1376724881514"><a name="note1376724881514"></a><a name="note1376724881514"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1776616482157"><a name="p1776616482157"></a><a name="p1776616482157"></a>To edit an environment variable that has been set, click <strong id="b106004813540"><a name="b106004813540"></a><a name="b106004813540"></a>Edit</strong>. To delete an environment variable that has been set, click <strong id="b19257143125510"><a name="b19257143125510"></a><a name="b19257143125510"></a>Delete</strong>.</p>
        </div></div>
        </td>
        </tr>
        <tr id="row67677480154"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p5767848191514"><a name="p5767848191514"></a><a name="p5767848191514"></a>Data Storage</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p8767124813155"><a name="p8767124813155"></a><a name="p8767124813155"></a>Local disks can be upgraded. For details, see <a href="using-local-disks-for-storage.md">Using Local Disks for Storage</a>.</p>
        </td>
        </tr>
        <tr id="row37674483152"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p17767164814150"><a name="p17767164814150"></a><a name="p17767164814150"></a>Security Context</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1376710489159"><a name="p1376710489159"></a><a name="p1376710489159"></a>Set container permissions to protect the system and other containers from being affected.</p>
        <p id="p27677487153"><a name="p27677487153"></a><a name="p27677487153"></a>Enter the user ID to set container permissions and prevent systems and other containers from being affected.</p>
        </td>
        </tr>
        <tr id="row276854861518"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p2076712483151"><a name="p2076712483151"></a><a name="p2076712483151"></a>Log Policies</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p889019285217"><a name="p889019285217"></a><a name="p889019285217"></a>Set the container log collection policies and the log directory to collect container logs for unified management and analysis. For details, see <a href="collecting-standard-output-logs-of-containers.md">Collecting Standard Output Logs of Containers</a> and <a href="collecting-container-logs-from-specified-paths.md">Collecting Container Logs from Specified Paths</a>.</p>
        </td>
        </tr>
        </tbody>
        </table>

3.  Click  **Submit**.

## Editing a YAML File<a name="section1412132734911"></a>

To download and edit the YAML file of a StatefulSet, do as follows:

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **StatefulSets**.
2.  In the same row as the StatefulSet you will edit, choose  **Operation**  \>  **More**  \>  **Edit YAML**. In the  **Edit YAML**  window, edit the YAML file of the current StatefulSet.
3.  Click  **Edit**  and then  **OK**  to save the changes.
4.  \(Optional\) In the  **Edit YAML**  window, click  **Download**  to download the YAML file.

## Scaling a StatefulSet<a name="section1360883716272"></a>

A StatefulSet can be automatically resized according to custom scaling policies, freeing you from the efforts to manually adapt the amount of resources to fluctuating traffic load. This saves you big on both resources and labors.

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **StatefulSets**.
2.  In the same row as the StatefulSet for which you will add a scaling policy, choose  **Operation**  \>  **More**  \>  **Scale**.
3.  On the  **Scale**  tab page, add or edit scaling policies. Scaling policies are classified as auto and manual scaling policies. For details, see  [Scaling a Workload](scaling-a-workload.md).

## Deleting a StatefulSet<a name="section14423721191418"></a>

You can delete a StatefulSet that will be no longer in use. Deleted StatefulSets cannot be recovered. Exercise caution when you perform this operation.

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **StatefulSets**.
2.  In the same row as the StatefulSet you will delete, choose  **Operation**  \>  **More**  \>  **Delete**.

    Follow on-screen instructions to delete the StatefulSet.

3.  Click  **OK**.

