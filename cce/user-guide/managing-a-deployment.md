# Managing a Deployment<a name="cce_01_0007"></a>

After a Deployment is created, you can scale, upgrade, monitor, roll back, or delete the Deployment, as well as edit its YAML file.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>This section uses a Deployment as an example to describe the workload management functions supported by CCE. If any of the following functions is not available on the CCE console, it is not supported yet.

## Viewing Deployment Logs<a name="section51511928173817"></a>

To view logs of a Deployment, do as follows:

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**.
2.  In the same row as the Deployment you will view, click  **Logs**.

    In the displayed  **Logs**  window, view the logs generated in the last 5 minutes, 30 minutes, or 1 hour.


## Upgrading a Deployment<a name="section17604174417381"></a>

CCE enables you to quickly and hitlessly upgrade a Deployment by replacing its image or image version.

Before replacing an image or image version, upload the new image to the SWR service. For details, see  [Image Repository](image-repository.md).

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**, and click  **Upgrade**  for the Deployment to be upgraded.
2.  Upgrade the Deployment.
    -   To replace the Deployment image, click  **Replace Image**  and select a new image.
    -   To replace the Deployment image version, select a new version from the  **Image Version**  drop-down list.
    -   To change the container name, click  ![](figures/icon-edit-0.png)  next to  **Container Name**  and enter a new name.
    -   Configure advanced settings.

        **Table  1**  Advanced settings

        <a name="table415171053012"></a>
        <table><thead align="left"><tr id="row15148810173011"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p3148710123017"><a name="p3148710123017"></a><a name="p3148710123017"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p1148181093015"><a name="p1148181093015"></a><a name="p1148181093015"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row61494108309"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1149121017304"><a name="p1149121017304"></a><a name="p1149121017304"></a>Lifecycle</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p4825183816913"><a name="p4825183816913"></a><a name="p4825183816913"></a>Commands that are executed in each lifecycle phase of a container.</p>
        <a name="ul345010411490"></a><a name="ul345010411490"></a><ul id="ul345010411490"><li><strong id="b13371035379917"><a name="b13371035379917"></a><a name="b13371035379917"></a>Startup Command</strong>: executed when the container is started. For more information, see <a href="setting-container-startup-commands.md">Setting Container Startup Commands</a>.</li><li><strong id="b1189115417503"><a name="b1189115417503"></a><a name="b1189115417503"></a>Post-Start</strong>: executed after the container is successfully run. For details, see <a href="setting-container-lifecycle-parameters.md">Setting Container Lifecycle Parameters</a>.</li><li><strong id="b4515275969939"><a name="b4515275969939"></a><a name="b4515275969939"></a>Pre-Stop</strong>: executed to delete logs or temporary files before the container stops. For more information, see <a href="setting-container-lifecycle-parameters.md">Setting Container Lifecycle Parameters</a>.</li></ul>
        </td>
        </tr>
        <tr id="row014913106304"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p201497101300"><a name="p201497101300"></a><a name="p201497101300"></a>Health Check</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><div class="p" id="p17922112911101"><a name="p17922112911101"></a><a name="p17922112911101"></a>The system checks whether containers and services are running properly. Two types of probes are set: workload liveness probe and workload service probe. For more information, see <a href="setting-health-check-for-a-container.md">Setting Health Check for a Container</a>.<a name="ul13466311391"></a><a name="ul13466311391"></a><ul id="ul13466311391"><li><strong id="b1189217545504"><a name="b1189217545504"></a><a name="b1189217545504"></a>Liveness Probe</strong>: Restarts the container when detecting that the container instance is unhealthy.</li><li><strong id="b3892145465010"><a name="b3892145465010"></a><a name="b3892145465010"></a>Readiness Probe</strong>: Sets the workload to the unready state when detecting that the workload's container instance is unhealthy. In this way, the service traffic will not be directed to the container instance.</li></ul>
        </div>
        </td>
        </tr>
        <tr id="row14150710153016"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p01491310143018"><a name="p01491310143018"></a><a name="p01491310143018"></a>Environment Variables</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p15445520200"><a name="p15445520200"></a><a name="p15445520200"></a>Environment variables are usually to store parameter values. To add environment variables to a container, click <strong id="b1646011219519"><a name="b1646011219519"></a><a name="b1646011219519"></a>Add Environment Variable</strong> on the <strong id="b75958306791110"><a name="b75958306791110"></a><a name="b75958306791110"></a>Environment Variables</strong> tab page. Currently, there are three types of environment variables:</p>
        <a name="ul15192350162919"></a><a name="ul15192350162919"></a><ul id="ul15192350162919"><li><strong id="b1481572491136"><a name="b1481572491136"></a><a name="b1481572491136"></a>Added manually</strong>: Set <strong id="b203463437291136"><a name="b203463437291136"></a><a name="b203463437291136"></a>Variable Name</strong> and <strong id="b186461720691136"><a name="b186461720691136"></a><a name="b186461720691136"></a>Variable Value/Reference</strong>.</li><li><strong id="b157161394891145"><a name="b157161394891145"></a><a name="b157161394891145"></a>Added from Secret</strong>: Set <strong id="b24678617291145"><a name="b24678617291145"></a><a name="b24678617291145"></a>Variable Name</strong> and select the desired secret name and data. A secret must be created in advance. For details, see <a href="creating-a-secret.md">Creating a Secret</a>.</li><li><strong id="b10979397299126"><a name="b10979397299126"></a><a name="b10979397299126"></a>Added from ConfigMap</strong>: Set <strong id="b12119315379126"><a name="b12119315379126"></a><a name="b12119315379126"></a>Variable Name</strong> and select the desired ConfigMap name and data. A ConfigMap must be created in advance. For details, see <a href="creating-a-configmap.md">Creating a ConfigMap</a>.</li></ul>
        <div class="note" id="note470614298582"><a name="note470614298582"></a><a name="note470614298582"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p10707122910587"><a name="p10707122910587"></a><a name="p10707122910587"></a>To edit an environment variable that has been set, click <strong id="b18449343267"><a name="b18449343267"></a><a name="b18449343267"></a>Edit</strong>. To delete an environment variable that has been set, click <strong id="b56923164714"><a name="b56923164714"></a><a name="b56923164714"></a>Delete</strong>.</p>
        </div></div>
        </td>
        </tr>
        <tr id="row1815012101301"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1215031012308"><a name="p1215031012308"></a><a name="p1215031012308"></a>Data Storage</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p20781049143213"><a name="p20781049143213"></a><a name="p20781049143213"></a>Local disks can be upgraded. For details, see <a href="using-local-disks-for-storage.md">Using Local Disks for Storage</a>.</p>
        </td>
        </tr>
        <tr id="row124974911017"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p424918492109"><a name="p424918492109"></a><a name="p424918492109"></a>Security Context</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p12523122111119"><a name="p12523122111119"></a><a name="p12523122111119"></a>Set container permissions to protect the system and other containers from being affected.</p>
        <p id="p202021016182811"><a name="p202021016182811"></a><a name="p202021016182811"></a>Enter the user ID to set container permissions and prevent systems and other containers from being affected.</p>
        </td>
        </tr>
        <tr id="row15151131033012"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1415031033012"><a name="p1415031033012"></a><a name="p1415031033012"></a>Log Policies</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1318317524327"><a name="p1318317524327"></a><a name="p1318317524327"></a>Set the container log collection policies and the log directory to collect container logs for unified management and analysis. For details, see <a href="collecting-standard-output-logs-of-containers.md">Collecting Standard Output Logs of Containers</a> and <a href="collecting-container-logs-from-specified-paths.md">Collecting Container Logs from Specified Paths</a>.</p>
        </td>
        </tr>
        </tbody>
        </table>

3.  Click  **Submit**.

## Editing a YAML File<a name="section21669213390"></a>

To download and edit the YAML file of a Deployment, do as follows:

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**.
2.  In the same row as the Deployment you will edit, choose  **Operation**  \>  **More**  \>  **Edit YAML**. In the  **Edit YAML**  window, edit the YAML file of the current Deployment.
3.  Click  **Edit**  and then  **OK**  to save the changes.
4.  \(Optional\) In the  **Edit YAML**  window, click  **Download**  to download the YAML file.

## Scaling a Deployment<a name="section11703514131711"></a>

A Deployment can be automatically resized according to custom scaling policies, freeing you from the efforts to manually adapt the amount of resources to fluctuating traffic load. This saves you big on both resources and labors.

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**.
2.  In the same row as the Deployment for which you will add a scaling policy, choose  **Operation**  \>  **More**  \>  **Scaling**.
3.  On the  **Scaling**  tab page, add or edit scaling policies. Scaling policies are classified as auto and manual scaling policies. For details, see  [Scaling a Workload](scaling-a-workload.md).

## Monitoring a Deployment<a name="section15303324141816"></a>

To view CPU and memory usage of a Deployment on the CCE console, do as follows:

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**.
2.  Click the name of the Deployment to be monitored. On the displayed Deployment details page, click the  **Monitoring**  tab to view CPU usage and memory usage of the Deployment.
3.  Click the  **Pods**  tab. Click  ![](figures/icon-monitoring-6.png)  next to a pod to be monitored and click  **Monitoring**.
4.  Check CPU usage and memory usage of the instance.
    -   CPU usage

        The horizontal axis indicates time while the vertical axis indicates the CPU usage. The green line indicates the CPU usage while the red line indicates the CPU usage limit.

        >![](public_sys-resources/icon-note.gif) **NOTE:** 
        >It takes some time to calculate CPU usage. Therefore, when CPU and memory usage are displayed for the first time, CPU usage is displayed about one minute later than memory usage.
        >CPU and memory usage are displayed only for pods in the running state.

    -   Memory usage

        The horizontal axis indicates time while the vertical axis indicates the memory usage. The green line indicates the memory usage while the red line indicates the memory usage limit.

        >![](public_sys-resources/icon-note.gif) **NOTE:** 
        >Memory usage is displayed only for a running pod.



## Rolling Back a Deployment<a name="section13324541124815"></a>

CCE records the release history of all Deployments. You can roll back a Deployment to a specified version.

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**.
2.  In the same row as the Deployment you will roll back, choose  **Operation**  \>  **More**  \>  **Roll Back**.
3.  In the  **Roll Back to This Version**  drop-down list, select the version to which you will roll back the Deployment. Then, click  **OK**.

## Pausing a Deployment<a name="section10207209154017"></a>

You can pause Deployments. After a Deployment is paused, the upgrade command can be successfully issued but will not be applied to the pods.

If you are performing a rolling upgrade, the rolling upgrade stops after the pause command is issued. In this case, the new and old pods coexist.

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**.
2.  In the same row as the Deployment you will pause, choose  **Operation**  \>  **More**  \>  **Pause**.
3.  In the displayed  **Pause Workload**  dialog box, click  **OK**.
4.  Click  **OK**.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:** 
    >Deployments in the paused state cannot be rolled back.


## Resuming a Deployment<a name="section12087915401"></a>

You can resume paused Deployments. After a Deployment is resumed, it can be upgraded or rolled back. Its pods will inherit the latest updates of the Deployment. If they are inconsistent, the pods are upgraded automatically according to the latest information of the Deployment.

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**.
2.  In the same row as the Deployment you will resume, choose  **Operation**  \>  **More**  \>  **Resume**.
3.  In the displayed  **Resume Workload**  dialog box, click  **OK**.

## Attaching Labels to Deployments<a name="section5931193015488"></a>

Labels are key-value pairs and can be attached to Deployments. Deployments can be easily selected based on labels. Usually, Deployment labels are used during affinity and anti-affinity scheduling. You can add labels to multiple Deployments or a specified Deployment.

In the following figure, three labels \(release, env, and role\) are defined for Deployments APP1, APP2, and APP3. The values of these labels vary with Deployments.

-   Label of APP 1: \[release:alpha;env:development;role:frontend\]
-   Label of APP 2: \[release:beta;env:testing;role:frontend\]
-   Label of APP 3: \[release:alpha;env:production;role:backend\]

If you set  **key**  to  **role**  and  **value**  to  **frontend**  when using Deployment scheduling or another function, the function will apply to APP1 and APP2.

**Figure  1**  Label example<a name="ff50c8d071f4d462bb116f4e3d67c131c"></a>  
![](figures/label-example.png "label-example")

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**.
2.  Click the name of the Deployment whose labels will be managed.
3.  On the Deployment details page, click  **Manage Label**. In the displayed dialog box, click  **Add Label**. Enter the label key and value, and click  **OK**.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >A key-value pair must contain 1 to 63 characters starting and ending with a letter or digit. Only letters, digits, hyphens \(-\), underscores \(\_\), and periods \(.\) are allowed.


## Deleting a Deployment<a name="section14423721191418"></a>

You can delete a Deployment that will be no longer in use. Deleted Deployments cannot be recovered. Exercise caution when you perform this operation.

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**.
2.  In the same row as the Deployment you will delete, choose  **Operation**  \>  **More**  \>  **Delete**. Follow on-screen instructions to delete the Deployment.
3.  Click  **OK**.

