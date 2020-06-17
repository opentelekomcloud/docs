# Creating a Job<a name="cce_01_0150"></a>

A  job  is executed only once immediately after being deployed. Before creating a workload, you can execute a job to upload an  image  to the  image repository.

## Prerequisites<a name="s50bf087555b1437aa249c1259138706c"></a>

Nodes have been added. For more information, see  [Creating Nodes](creating-a-node.md). If  clusters  and  node  resources are available, skip this operation.

## Procedure<a name="sb8a02965b2624dbbabab320046ca4973"></a>

1.  \(Optional\) If you use a  private container image  to create your job, upload the container image to the image repository.

    For details, see  [Image Repository](image_repository).

2.  Log in to the CCE console. In the navigation pane, choose  **Workloads \> Jobs**. Then, click  **Create Job**_._
3.  Configure the basic job information listed in  [Table 1](#t70ce3a99637a44ce8f7274857fb245b1). The parameters marked with an asterisk \(\*\) are mandatory.

    **Table  1**  Basic job information

    <a name="t70ce3a99637a44ce8f7274857fb245b1"></a>
    <table><thead align="left"><tr id="r1a0b6bbef01240158b8e679b6165cf76"><th class="cellrowborder" valign="top" width="19.77%" id="mcps1.2.3.1.1"><p id="a51b64f77c7d04e0f9025ed260d38faa3"><a name="a51b64f77c7d04e0f9025ed260d38faa3"></a><a name="a51b64f77c7d04e0f9025ed260d38faa3"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="80.23%" id="mcps1.2.3.1.2"><p id="a639151b15ff74221a51e0b671a591976"><a name="a639151b15ff74221a51e0b671a591976"></a><a name="a639151b15ff74221a51e0b671a591976"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="r92a0394079de48da83876059957c2b78"><td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.3.1.1 "><p id="a989ec542e71a4040a82cbf2931695364"><a name="a989ec542e71a4040a82cbf2931695364"></a><a name="a989ec542e71a4040a82cbf2931695364"></a>* Job Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.23%" headers="mcps1.2.3.1.2 "><p id="a55e0ddd0f9c24b239315111b39913395"><a name="a55e0ddd0f9c24b239315111b39913395"></a><a name="a55e0ddd0f9c24b239315111b39913395"></a>Name of a new job. The name must be unique.</p>
    </td>
    </tr>
    <tr id="r80610bcddd944c02a6e928130b1bc574"><td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.3.1.1 "><p id="a75643f9a614b4180b6b9404f503c5dfd"><a name="a75643f9a614b4180b6b9404f503c5dfd"></a><a name="a75643f9a614b4180b6b9404f503c5dfd"></a>* Cluster</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.23%" headers="mcps1.2.3.1.2 "><p id="a760cf36b9e3b4d168c5ea807b62896d2"><a name="a760cf36b9e3b4d168c5ea807b62896d2"></a><a name="a760cf36b9e3b4d168c5ea807b62896d2"></a>Cluster to which a new job belongs.</p>
    </td>
    </tr>
    <tr id="row43713551547"><td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.3.1.1 "><p id="p1381455125415"><a name="p1381455125415"></a><a name="p1381455125415"></a>* Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.23%" headers="mcps1.2.3.1.2 "><p id="p18383552541"><a name="p18383552541"></a><a name="p18383552541"></a>Namespace to which the new job belongs. By default, this parameter is set to <strong id="b842352706164344"><a name="b842352706164344"></a><a name="b842352706164344"></a>default</strong>.</p>
    </td>
    </tr>
    <tr id="row0507119121413"><td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.3.1.1 "><p id="p19507591149"><a name="p19507591149"></a><a name="p19507591149"></a>* Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.23%" headers="mcps1.2.3.1.2 "><p id="p1042648123717"><a name="p1042648123717"></a><a name="p1042648123717"></a>Number of job instances. A job can have one or more instances. You can specify the number of instances. The default value is <strong id="b842352706104552"><a name="b842352706104552"></a><a name="b842352706104552"></a>1</strong>.</p>
    <p id="p17713926910"><a name="p17713926910"></a><a name="p17713926910"></a>Each job instance consists of the same containers. Configuring multiple job instances can ensure high availability. The job can continue to run even if one of the instances is faulty.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0093532761_row2314820103"><td class="cellrowborder" valign="top" width="19.77%" headers="mcps1.2.3.1.1 "><p id="ab9807e25b58e4d3e88a5fe580e46e093"><a name="ab9807e25b58e4d3e88a5fe580e46e093"></a><a name="ab9807e25b58e4d3e88a5fe580e46e093"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.23%" headers="mcps1.2.3.1.2 "><p id="a8f8f3f458f7c416eb54e58701713294d"><a name="a8f8f3f458f7c416eb54e58701713294d"></a><a name="a8f8f3f458f7c416eb54e58701713294d"></a>Description of a job.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Next**  to add a container.
    1.  Click  **Select Container Image**  to select the image to be deployed.
        -   **My Images**: displays all image repositories you created.
        -   **Third-Party Images**: CCE allows you to create a job from any third-party image repository other than SWR. When you create a job using a third-party image, ensure that the node where the job is running can access public networks. For details about how to use a third-party image, see  [Using a Third-Party Image](using-a-third-party-image.md).
            -   If your image repository does not require authentication, set  **Secret Authentication**  to  **No**, enter an image address in  **Image Address**, and then click  **OK**.
            -   If your image repository must be  authenticated  \(account and password\), you need to create a key and then use a third-party image. For details, see  [Using a Third-Party Image](using-a-third-party-image.md).

        -   **Shared Images**: The images shared by other tenants using the SWR service are displayed here. You can create workloads based on the shared images.

    2.  Set image parameters.

        **Table  2**  Image parameters

        <a name="t2fdf8c3943d948f6873da4b75b46d3f5"></a>
        <table><thead align="left"><tr id="en-us_topic_0107283470_row0282348486"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="en-us_topic_0107283470_p3282147483"><a name="en-us_topic_0107283470_p3282147483"></a><a name="en-us_topic_0107283470_p3282147483"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="en-us_topic_0107283470_p1828244144819"><a name="en-us_topic_0107283470_p1828244144819"></a><a name="en-us_topic_0107283470_p1828244144819"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0107283470_row1844916557597"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p182837474815"><a name="en-us_topic_0107283470_p182837474815"></a><a name="en-us_topic_0107283470_p182837474815"></a>Image</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p3283134134820"><a name="en-us_topic_0107283470_p3283134134820"></a><a name="en-us_topic_0107283470_p3283134134820"></a>Name of the image. You can click <strong id="b84235270617012"><a name="b84235270617012"></a><a name="b84235270617012"></a>Change Image</strong> to update it.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283470_row338117362515"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p1038143616517"><a name="en-us_topic_0107283470_p1038143616517"></a><a name="en-us_topic_0107283470_p1038143616517"></a>* Image Version</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p14236148133915"><a name="p14236148133915"></a><a name="p14236148133915"></a>Version of the image to be deployed.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283470_row32839494813"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p122831140486"><a name="en-us_topic_0107283470_p122831140486"></a><a name="en-us_topic_0107283470_p122831140486"></a>* Container Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p528314415486"><a name="en-us_topic_0107283470_p528314415486"></a><a name="en-us_topic_0107283470_p528314415486"></a>Name of the container. You can modify it.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283470_row152831345485"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p875325925918"><a name="en-us_topic_0107283470_p875325925918"></a><a name="en-us_topic_0107283470_p875325925918"></a>Container Resources</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><div class="p" id="en-us_topic_0107283470_p1825119142351"><a name="en-us_topic_0107283470_p1825119142351"></a><a name="en-us_topic_0107283470_p1825119142351"></a>For more information about <strong id="b1672210449245"><a name="b1672210449245"></a><a name="b1672210449245"></a>Request</strong> and <strong id="b5722194432420"><a name="b5722194432420"></a><a name="b5722194432420"></a>Limit</strong>, see <a href="setting-container-specifications.md">Setting Container Specifications</a>.<a name="en-us_topic_0107283470_ul1674183414114"></a><a name="en-us_topic_0107283470_ul1674183414114"></a><ul id="en-us_topic_0107283470_ul1674183414114"><li><strong id="b1834123719193"><a name="b1834123719193"></a><a name="b1834123719193"></a>Request</strong>: the amount of resources that CCE will guarantee to a container.</li><li><strong id="b842352706161350"><a name="b842352706161350"></a><a name="b842352706161350"></a>Limit</strong>: If a container is overloaded, the system may be faulty. To avoid this situation, set the maximum limits for the container resource quota to ensure that container resources do not exceed the limits.</li><li>GPU settings:<div class="note" id="en-us_topic_0107283470_note118204916050"><a name="en-us_topic_0107283470_note118204916050"></a><a name="en-us_topic_0107283470_note118204916050"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0107283470_p1063844316050"><a name="en-us_topic_0107283470_p1063844316050"></a><a name="en-us_topic_0107283470_p1063844316050"></a>GPU can be configured only when the cluster contains GPU nodes.</p>
        </div></div>
        <a name="en-us_topic_0107283470_ul2409689116041"></a><a name="en-us_topic_0107283470_ul2409689116041"></a><ul id="en-us_topic_0107283470_ul2409689116041"><li>GPU quota: Select <span class="uicontrol" id="uicontrol93352013121413"><a name="uicontrol93352013121413"></a><a name="uicontrol93352013121413"></a><b>Use</b></span> and set the percentage. For example, if this parameter is set to 10%, the container is allowed to use 10% of GPU resources. If you do not select <span class="uicontrol" id="uicontrol16417155441419"><a name="uicontrol16417155441419"></a><a name="uicontrol16417155441419"></a><b>Use</b></span> or set this parameter to 0, no GPU resources can be used.</li><li>GPU/Graphics Card: If <strong id="b11611829191320"><a name="b11611829191320"></a><a name="b11611829191320"></a>Any GPU type</strong> is selected, the container uses a random GPU in the node. If you select a specific GPU, the container uses this GPU.</li></ul>
        </li></ul>
        </div>
        </td>
        </tr>
        </tbody>
        </table>

    3.  \(Optional\) Configure advanced settings.

        **Table  3**  Advanced settings

        <a name="tf56c7b65fd00476dbf686d494609ec01"></a>
        <table><thead align="left"><tr id="rd70607f9bfa74a83a6e424e8abda265c"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="a85705044d3104d34957e244b20e98de2"><a name="a85705044d3104d34957e244b20e98de2"></a><a name="a85705044d3104d34957e244b20e98de2"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="ab80a0aae28b54ab1afe9009e2466b2e6"><a name="ab80a0aae28b54ab1afe9009e2466b2e6"></a><a name="ab80a0aae28b54ab1afe9009e2466b2e6"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="r616e69d5a2004b079888d8a4a2a83762"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="ae1906e2a0f4e48c8a290d2ffdc9e83bf"><a name="ae1906e2a0f4e48c8a290d2ffdc9e83bf"></a><a name="ae1906e2a0f4e48c8a290d2ffdc9e83bf"></a>Lifecycle</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><div class="p" id="a72815832aa2c4ad6953cec368b824346"><a name="a72815832aa2c4ad6953cec368b824346"></a><a name="a72815832aa2c4ad6953cec368b824346"></a>Lifecycle scripts define the actions taken for container-related jobs when a lifecycle event occurs.<a name="u86a34d59537a4e5ebbcd8d62f0fb6fc7"></a><a name="u86a34d59537a4e5ebbcd8d62f0fb6fc7"></a><ul id="u86a34d59537a4e5ebbcd8d62f0fb6fc7"><li><strong id="b1561153219157"><a name="b1561153219157"></a><a name="b1561153219157"></a>Start Command</strong>: If you enter a container startup command, the command is immediately executed after the container starts. For details, see <a href="advanced_container_settings.rst">Advanced Container Settings</a>.</li><li><strong id="b106111232161517"><a name="b106111232161517"></a><a name="b106111232161517"></a>Post-Start</strong> <strong id="b1430804194616"><a name="b1430804194616"></a><a name="b1430804194616"></a>Processing</strong>: The command is triggered after a job starts. For details, see <a href="setting-container-lifecycle-parameters.md">Setting Container Lifecycle Parameters</a>.</li><li><strong id="b461243251510"><a name="b461243251510"></a><a name="b461243251510"></a>Pre-Stop Processing</strong>: The command is triggered before a job is stopped. For details, see <a href="setting-container-lifecycle-parameters.md">Setting Container Lifecycle Parameters</a>.</li></ul>
        </div>
        </td>
        </tr>
        <tr id="r159688429d2c4ad5b55d2b63b5bc6a46"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="acab0841bbf1548e08722d5ec9fb378e9"><a name="acab0841bbf1548e08722d5ec9fb378e9"></a><a name="acab0841bbf1548e08722d5ec9fb378e9"></a>Environment Variables</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><div class="p" id="p1033073311186"><a name="p1033073311186"></a><a name="p1033073311186"></a>Environment variables can be added to a container. In general, environment variables are used to set parameters. On the <strong id="b14284216151619"><a name="b14284216151619"></a><a name="b14284216151619"></a>Environment Variables</strong> tab page, click <strong id="b1928451611610"><a name="b1928451611610"></a><a name="b1928451611610"></a>Add Environment Variables</strong>. Currently, environment variables can be added using any of the following methods:<a name="ul145379401817"></a><a name="ul145379401817"></a><ul id="ul145379401817"><li><strong id="b284992934420"><a name="b284992934420"></a><a name="b284992934420"></a>Added manually</strong>: Set <strong id="b88501129194417"><a name="b88501129194417"></a><a name="b88501129194417"></a>Variable Name</strong> and <strong id="b6850162964413"><a name="b6850162964413"></a><a name="b6850162964413"></a>Variable Value/Reference</strong>.</li><li><strong id="b19672134174410"><a name="b19672134174410"></a><a name="b19672134174410"></a>Added from secret</strong>: Set <strong id="b146731634184410"><a name="b146731634184410"></a><a name="b146731634184410"></a>Variable Name</strong> and select the desired secret name and data. The prerequisite of this method is that a secret has been created. For details, see <a href="creating-a-secret.md">Creating a Secret</a>.</li><li>Importing a ConfigMap: Set <strong id="b629881611615"><a name="b629881611615"></a><a name="b629881611615"></a>Variable Name</strong> and select the desired ConfigMap name and data. The prerequisite of this method is that a ConfigMap has been created. For details, see <a href="creating-a-configmap.md">Creating a ConfigMap</a>.</li></ul>
        </div>
        </td>
        </tr>
        <tr id="r23157569d21e4f1eaca7fddbb384abd8"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="a8540d286ec904152a0ae2a7706f81b13"><a name="a8540d286ec904152a0ae2a7706f81b13"></a><a name="a8540d286ec904152a0ae2a7706f81b13"></a>Data Storage</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="a8b0122d13c334988999081ca36bcd194"><a name="a8b0122d13c334988999081ca36bcd194"></a><a name="a8b0122d13c334988999081ca36bcd194"></a>The local disk or cloud storage can be mounted to a container to implement persistent data file storage.</p>
        <p id="a15513eb91b5c4c3daf720ca0b6365c60"><a name="a15513eb91b5c4c3daf720ca0b6365c60"></a><a name="a15513eb91b5c4c3daf720ca0b6365c60"></a>For details, see <a href="storage_management.rst">Storage Management</a>.</p>
        </td>
        </tr>
        <tr id="r547f9887aa95447fae37c69bf28e8d09"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="a4a93ff2a806b494c8d80b89595802cbe"><a name="a4a93ff2a806b494c8d80b89595802cbe"></a><a name="a4a93ff2a806b494c8d80b89595802cbe"></a>Log Policies</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="ac6fc6fa08da64fdc9d6366f5f9834e11"><a name="ac6fc6fa08da64fdc9d6366f5f9834e11"></a><a name="ac6fc6fa08da64fdc9d6366f5f9834e11"></a>Set a log policy and log path for collecting workload logs and preventing logs from being over-sized. For details, see <a href="collecting-standard-output-logs-of-containers.md">Collecting Standard Output Logs of Containers</a>.</p>
        </td>
        </tr>
        </tbody>
        </table>

    4.  \(Optional\) One job instance contains one or more related containers. If your job contains multiple containers, click  **Add Container**  to add containers.

5.  Click  **Create**.

    If the status of the job is  **Execution completed**, the job has been created successfully.


## Using kubectl<a name="section450152719412"></a>

A job has the following configuration parameters:

-   **spec.template**: has the same schema as a pod.
-   **RestartPolicy**: can only be set to  **Never**  or  **OnFailure**.
-   For a single-pod job, the job ends after the pod runs successfully by default.
-   **.spec.completions**: indicates the number of pods that need to run successfully to end a job. The default value is  **1**.
-   **.spec.parallelism**: indicates the number of pods that run concurrently. The default value is  **1**.
-   **spec.backoffLimit**: indicates the maximum number of retries performed if a pod fails. When the limit is reached, the pod will not try again.
-   **.spec.activeDeadlineSeconds**: indicates the running time of pods. Once the time is reached, all pods of the job are terminated. The priority of .spec.activeDeadlineSeconds is higher than that of .spec.backoffLimit. That is, if a job reaches the .spec.activeDeadlineSeconds, the spec.backoffLimit is ignored.

Based on the  **.spec.completions**  and  **.spec.Parallelism**  settings, jobs are classified into the following types.

**Table  4**  Job types

<a name="table19214202022111"></a>
<table><thead align="left"><tr id="row221419208210"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.4.1.1"><p id="p192146200219"><a name="p192146200219"></a><a name="p192146200219"></a>Job Type</p>
</th>
<th class="cellrowborder" valign="top" width="39%" id="mcps1.2.4.1.2"><p id="p0214720122118"><a name="p0214720122118"></a><a name="p0214720122118"></a>Description</p>
</th>
<th class="cellrowborder" valign="top" width="40%" id="mcps1.2.4.1.3"><p id="p62149208219"><a name="p62149208219"></a><a name="p62149208219"></a>Example</p>
</th>
</tr>
</thead>
<tbody><tr id="row82141620152119"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p2050935122113"><a name="p2050935122113"></a><a name="p2050935122113"></a>One-off jobs</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p124101856162110"><a name="p124101856162110"></a><a name="p124101856162110"></a>A single pod runs once until successful termination.</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p58403110224"><a name="p58403110224"></a><a name="p58403110224"></a>Database migration</p>
</td>
</tr>
<tr id="row1221432052118"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p14512351132120"><a name="p14512351132120"></a><a name="p14512351132120"></a>Jobs with a fixed completion count</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p741405662112"><a name="p741405662112"></a><a name="p741405662112"></a>One pod runs until reaching the specified <strong id="b1815413565343"><a name="b1815413565343"></a><a name="b1815413565343"></a>completions</strong> count.</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p1284481192220"><a name="p1284481192220"></a><a name="p1284481192220"></a>Work queue processing pod</p>
</td>
</tr>
<tr id="row1321432013217"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p195159512216"><a name="p195159512216"></a><a name="p195159512216"></a>Parallel jobs with a fixed completion count</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p134205562218"><a name="p134205562218"></a><a name="p134205562218"></a>Multiple pods run until reaching the specified <strong id="b1215465693419"><a name="b1215465693419"></a><a name="b1215465693419"></a>completions</strong> count.</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p3847512224"><a name="p3847512224"></a><a name="p3847512224"></a>Multiple pods processing from a centralized work queue</p>
</td>
</tr>
<tr id="row8214192020217"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.4.1.1 "><p id="p115209514218"><a name="p115209514218"></a><a name="p115209514218"></a>Parallel jobs</p>
</td>
<td class="cellrowborder" valign="top" width="39%" headers="mcps1.2.4.1.2 "><p id="p12424856142114"><a name="p12424856142114"></a><a name="p12424856142114"></a>One or more pods run until successful termination.</p>
</td>
<td class="cellrowborder" valign="top" width="40%" headers="mcps1.2.4.1.3 "><p id="p285251142217"><a name="p285251142217"></a><a name="p285251142217"></a>Multiple pods processing from a centralized work queue</p>
</td>
</tr>
</tbody>
</table>

The following is an example job, which calculates π till the 2000<sup>th</sup>  digit and prints the output.

```
apiVersion: batch/v1
kind: Job
metadata:
  name: pi-with-timeout
spec:
  completions: 50        # 50 pods need to be run to finish a job. In this example, π is printed for 50 times.
  parallelism: 5        # 5 pods are run parallel.
  backoffLimit: 5        # The maximum number of retry times is 5.
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
```

## Related Operations<a name="s9bef0428158a4935b466ea150ccae961"></a>

After a one-off job is created, you can perform operations listed in  [Table 5](#t84075653e7544394939d13740fad0c20).

**Table  5**  Other operations

<a name="t84075653e7544394939d13740fad0c20"></a>
<table><thead align="left"><tr id="r83819c2bd882441798d949cbee32fa6a"><th class="cellrowborder" valign="top" width="28.999999999999996%" id="mcps1.2.3.1.1"><p id="en-us_topic_0093532761_p92150167611"><a name="en-us_topic_0093532761_p92150167611"></a><a name="en-us_topic_0093532761_p92150167611"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="71%" id="mcps1.2.3.1.2"><p id="a6b27fdd2dcc340f3baa6024edb5b3ae9"><a name="a6b27fdd2dcc340f3baa6024edb5b3ae9"></a><a name="a6b27fdd2dcc340f3baa6024edb5b3ae9"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row17717577287"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.3.1.1 "><p id="p147711757162810"><a name="p147711757162810"></a><a name="p147711757162810"></a>Viewing a YAML</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.3.1.2 "><p id="p15771257142816"><a name="p15771257142816"></a><a name="p15771257142816"></a>Click <strong id="b84235270611425"><a name="b84235270611425"></a><a name="b84235270611425"></a>View YAML</strong> next to the job name to view the YAML file corresponding to the current job.</p>
</td>
</tr>
<tr id="r27a8f438ed1d4cbba2ad07f7a08acb06"><td class="cellrowborder" valign="top" width="28.999999999999996%" headers="mcps1.2.3.1.1 "><p id="a1f9f2bb06252439c82b01c1d4bbb9ab0"><a name="a1f9f2bb06252439c82b01c1d4bbb9ab0"></a><a name="a1f9f2bb06252439c82b01c1d4bbb9ab0"></a>Deleting a one-off job</p>
</td>
<td class="cellrowborder" valign="top" width="71%" headers="mcps1.2.3.1.2 "><a name="od5720c015360452491819af825ce5845"></a><a name="od5720c015360452491819af825ce5845"></a><ol id="od5720c015360452491819af825ce5845"><li>Select the job to be deleted and click <span class="uicontrol" id="uicontrol4855557669443"><a name="uicontrol4855557669443"></a><a name="uicontrol4855557669443"></a><b>Delete</b></span> in the <strong id="b1339219281075"><a name="b1339219281075"></a><a name="b1339219281075"></a>Operation</strong> column.</li><li>Click <strong id="a14b4819ca5b74b27beebaa7cc918e410"><a name="a14b4819ca5b74b27beebaa7cc918e410"></a><a name="a14b4819ca5b74b27beebaa7cc918e410"></a>OK</strong>.<p id="aad27c67674e84e898611af0725bfe1cf"><a name="aad27c67674e84e898611af0725bfe1cf"></a><a name="aad27c67674e84e898611af0725bfe1cf"></a>Deleted jobs cannot be restored. Exercise caution when deleting a job.</p>
</li></ol>
</td>
</tr>
</tbody>
</table>

