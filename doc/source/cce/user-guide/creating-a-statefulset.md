# Creating a StatefulSet<a name="cce_01_0048"></a>

StatefulSets  are a type of workloads whose data or status is stored while they are running. For example, MySQL is a StatefulSet because it needs to store new data.

A container can be migrated between different hosts, but data is not stored on the hosts. To store StatefulSet data persistently, attach HA storage volumes provided by CCE to the container.

## Prerequisites<a name="section1734962819219"></a>

Before creating a containerized workload, you must have an available cluster. For details on how to create a cluster, see  [Creating a Hybrid Cluster](creating-a-hybrid-cluster.md).

>![](/images/icon-note.gif) **NOTE:**   
>When creating multiple containerized workloads, ensure that each container has a unique port. Otherwise, workload creation will fail.  

## Using the CCE Console<a name="section16385130102112"></a>

1.  CCE provides multiple methods for creating a workload. You can use any of the following methods:
    1.  Use a third-party image to create a workload, without the need to upload an image.
    2.  Use an image to create a workload, you need to upload the image to the Software Repository f Container \(SWR\). For details about how to upload an image, see  [Image Repository](image_repository).
    3.  Use a shared image to create a workload. Specifically, other tenants share an image with you by using the SWR service.
    4.  Use a YAML file to create a workload. You can click  **Create YAML**  on the right of the  **Create StatefulSet**  page. For details about YAML, see  [Table 4](#table132326831016). After the YAML file is written, click  **Create**  to create a workload.

        >![](/images/icon-note.gif) **NOTE:**   
        >Settings in the YAML file are synchronized with settings on the console. You can also interact with the YAML to create a workload. For example, if you enter a workload name on the console, the name will automatically appear in the YAML file. Similarly, if you add an image on the console, the image will be automatically added to the YAML file.  


2.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **StatefulSets**. On the displayed page, click  **Create StatefulSet**. Set basic workload parameters as described in  [Table 1](#table12741447488). The parameters marked with an asterisk \(\*\) are mandatory.

    **Table  1**  Basic workload parameters

    <a name="table12741447488"></a>
    <table><thead align="left"><tr id="en-us_topic_0107283470_row52758419481"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="en-us_topic_0107283470_p152759464816"><a name="en-us_topic_0107283470_p152759464816"></a><a name="en-us_topic_0107283470_p152759464816"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="en-us_topic_0107283470_p3275134114811"><a name="en-us_topic_0107283470_p3275134114811"></a><a name="en-us_topic_0107283470_p3275134114811"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0107283470_row18415163712618"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p32763416485"><a name="en-us_topic_0107283470_p32763416485"></a><a name="en-us_topic_0107283470_p32763416485"></a>* Workload Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p5276341485"><a name="en-us_topic_0107283470_p5276341485"></a><a name="en-us_topic_0107283470_p5276341485"></a>Name of the workload to be created. The name must be unique.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0107283470_row81437181202"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p514451811010"><a name="en-us_topic_0107283470_p514451811010"></a><a name="en-us_topic_0107283470_p514451811010"></a>* Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p323714215492"><a name="en-us_topic_0107283470_p323714215492"></a><a name="en-us_topic_0107283470_p323714215492"></a>Cluster in which the workload resides.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0107283470_row169810201307"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p19698152011011"><a name="en-us_topic_0107283470_p19698152011011"></a><a name="en-us_topic_0107283470_p19698152011011"></a>* Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p12447336131710"><a name="en-us_topic_0107283470_p12447336131710"></a><a name="en-us_topic_0107283470_p12447336131710"></a>In a single cluster, data in different namespaces is isolated from each other. This enables applications to share the services of the same cluster without interfering each other. If no namespace is set, the default namespace is used.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0107283470_row165805182316"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p45913512317"><a name="en-us_topic_0107283470_p45913512317"></a><a name="en-us_topic_0107283470_p45913512317"></a>* Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p1042648123717"><a name="en-us_topic_0107283470_p1042648123717"></a><a name="en-us_topic_0107283470_p1042648123717"></a>Number of instances in the workload. A workload can have one or more instances. You can set the number of instances. The default value is <strong id="en-us_topic_0107283470_b842352706154640"><a name="en-us_topic_0107283470_b842352706154640"></a><a name="en-us_topic_0107283470_b842352706154640"></a>2</strong> and can be set to <strong id="en-us_topic_0107283470_b842352706154646"><a name="en-us_topic_0107283470_b842352706154646"></a><a name="en-us_topic_0107283470_b842352706154646"></a>1</strong>.</p>
    <p id="en-us_topic_0107283470_p17713926910"><a name="en-us_topic_0107283470_p17713926910"></a><a name="en-us_topic_0107283470_p17713926910"></a>Each workload instance consists of the same containers. Configuring multiple instances for a workload ensures that the workload can still run properly even if an instance is faulty. If only one instance is used, a node or instance exception may cause service exceptions.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0107283470_row18442191224514"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p244261214513"><a name="en-us_topic_0107283470_p244261214513"></a><a name="en-us_topic_0107283470_p244261214513"></a>Time Zone Synchronization</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p644215125454"><a name="en-us_topic_0107283470_p644215125454"></a><a name="en-us_topic_0107283470_p644215125454"></a>If <strong id="en-us_topic_0107283470_b842352706164155"><a name="en-us_topic_0107283470_b842352706164155"></a><a name="en-us_topic_0107283470_b842352706164155"></a>ON</strong> is selected, the container and the node use the same time zone.</p>
    <div class="notice" id="en-us_topic_0107283470_note5422953172616"><a name="en-us_topic_0107283470_note5422953172616"></a><a name="en-us_topic_0107283470_note5422953172616"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="en-us_topic_0107283470_p11422145392614"><a name="en-us_topic_0107283470_p11422145392614"></a><a name="en-us_topic_0107283470_p11422145392614"></a>After time zone synchronization is enabled, disks of the HostPath type will be automatically added and listed in the <strong id="en-us_topic_0107283470_b84235270616465"><a name="en-us_topic_0107283470_b84235270616465"></a><a name="en-us_topic_0107283470_b84235270616465"></a>Data Storage</strong> &gt; <strong id="en-us_topic_0107283470_b84235270616468"><a name="en-us_topic_0107283470_b84235270616468"></a><a name="en-us_topic_0107283470_b84235270616468"></a>Local Disk</strong> area. Do not modify or delete the disks.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0107283470_row1027719414818"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p1527715418485"><a name="en-us_topic_0107283470_p1527715418485"></a><a name="en-us_topic_0107283470_p1527715418485"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p827734134817"><a name="en-us_topic_0107283470_p827734134817"></a><a name="en-us_topic_0107283470_p827734134817"></a>Description of the workload.</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **Next**  to add a container.
    1.  Click  **Add Container**  and select the image to be deployed.
        -   **My Images**: Create a workload using an image in the image repository you created.
        -   **Third-Party Images**: Create a workload using an image from any third-party image repository \(image repositories other than SWR and Docker Hub\). When you create a workload using a third-party image, ensure that the node where the workload is running can access public networks. For details on how to create a workload using a third-party image, see  [Using a Third-Party Image](using-a-third-party-image.md).
            -   If your image repository does not require authentication, set  **Authenticate Secret**  to  **No**, enter an image address, and then click  **OK**.
            -   If your image repository must be authenticated \(account and password\), you need to create a key and then use a third-party image. For details, see  [Using a Third-Party Image](using-a-third-party-image.md).

        -   **Shared Images**: Create a workload using an image shared by another tenant through the SWR service.

    2.  Configure basic image information.

        **Table  2**  Image parameters

        <a name="t9abbfd9e05484cc1a0e9332711bdd756"></a>
        <table><thead align="left"><tr id="en-us_topic_0107283470_row0282348486"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="en-us_topic_0107283470_p3282147483"><a name="en-us_topic_0107283470_p3282147483"></a><a name="en-us_topic_0107283470_p3282147483"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="en-us_topic_0107283470_p1828244144819"><a name="en-us_topic_0107283470_p1828244144819"></a><a name="en-us_topic_0107283470_p1828244144819"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0107283470_row1844916557597"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p182837474815"><a name="en-us_topic_0107283470_p182837474815"></a><a name="en-us_topic_0107283470_p182837474815"></a>Image Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p3283134134820"><a name="en-us_topic_0107283470_p3283134134820"></a><a name="en-us_topic_0107283470_p3283134134820"></a>Name of the image. You can click <strong id="en-us_topic_0107283470_b84235270617012"><a name="en-us_topic_0107283470_b84235270617012"></a><a name="en-us_topic_0107283470_b84235270617012"></a>Change Image</strong> to update it.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283470_row338117362515"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p1038143616517"><a name="en-us_topic_0107283470_p1038143616517"></a><a name="en-us_topic_0107283470_p1038143616517"></a>* Image Version</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p1338110368519"><a name="en-us_topic_0107283470_p1338110368519"></a><a name="en-us_topic_0107283470_p1338110368519"></a>Version of the image to be deployed.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283470_row32839494813"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p122831140486"><a name="en-us_topic_0107283470_p122831140486"></a><a name="en-us_topic_0107283470_p122831140486"></a>* Container Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p528314415486"><a name="en-us_topic_0107283470_p528314415486"></a><a name="en-us_topic_0107283470_p528314415486"></a>Name of the container. You can modify it.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283470_row1449911299503"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p53374336504"><a name="en-us_topic_0107283470_p53374336504"></a><a name="en-us_topic_0107283470_p53374336504"></a>Privileged Container</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p49887211526"><a name="en-us_topic_0107283470_p49887211526"></a><a name="en-us_topic_0107283470_p49887211526"></a>Programs in a privileged container have certain privileges.</p>
        <p id="en-us_topic_0107283470_p65001729105011"><a name="en-us_topic_0107283470_p65001729105011"></a><a name="en-us_topic_0107283470_p65001729105011"></a>If <strong id="en-us_topic_0107283470_b13252222105114"><a name="en-us_topic_0107283470_b13252222105114"></a><a name="en-us_topic_0107283470_b13252222105114"></a>Privileged Container</strong> is <strong id="en-us_topic_0107283470_b11849182725112"><a name="en-us_topic_0107283470_b11849182725112"></a><a name="en-us_topic_0107283470_b11849182725112"></a>On</strong>, the container is granted superuser permissions. For example, privileged containers can manipulate network devices on the host machine and modify kernel parameters.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0107283470_row152831345485"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0107283470_p875325925918"><a name="en-us_topic_0107283470_p875325925918"></a><a name="en-us_topic_0107283470_p875325925918"></a>Container Resources</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0107283470_p5379182494610"><a name="en-us_topic_0107283470_p5379182494610"></a><a name="en-us_topic_0107283470_p5379182494610"></a>CPU quotas:</p>
        <a name="en-us_topic_0107283470_ul67283495467"></a><a name="en-us_topic_0107283470_ul67283495467"></a><ul id="en-us_topic_0107283470_ul67283495467"><li><strong id="en-us_topic_0107283470_b837912315811"><a name="en-us_topic_0107283470_b837912315811"></a><a name="en-us_topic_0107283470_b837912315811"></a>Request</strong>: the minimum number of CPU cores required by a container. The default value is 0.25 core.</li><li><strong id="en-us_topic_0107283470_b1728781088"><a name="en-us_topic_0107283470_b1728781088"></a><a name="en-us_topic_0107283470_b1728781088"></a>Limit</strong>: the maximum number of CPU cores available for a container. Do not leave <strong id="en-us_topic_0107283470_b71778281894"><a name="en-us_topic_0107283470_b71778281894"></a><a name="en-us_topic_0107283470_b71778281894"></a>Limit</strong> unspecified. Otherwise, intensive use of container resources will occur and your workload may exhibit unexpected behavior.</li></ul>
        <p id="en-us_topic_0107283470_p633394210502"><a name="en-us_topic_0107283470_p633394210502"></a><a name="en-us_topic_0107283470_p633394210502"></a>Memory quotas:</p>
        <a name="en-us_topic_0107283470_ul14326165915010"></a><a name="en-us_topic_0107283470_ul14326165915010"></a><ul id="en-us_topic_0107283470_ul14326165915010"><li><strong id="en-us_topic_0107283470_b2325104041116"><a name="en-us_topic_0107283470_b2325104041116"></a><a name="en-us_topic_0107283470_b2325104041116"></a>Request</strong>: the minimum amount of memory required by a container. The default value is 512 MiB.</li><li><strong id="en-us_topic_0107283470_b4467144318115"><a name="en-us_topic_0107283470_b4467144318115"></a><a name="en-us_topic_0107283470_b4467144318115"></a>Limit</strong>: the maximum amount of memory available for a container. When memory usage exceeds the specified memory limit, the container will be terminated.</li></ul>
        <p id="en-us_topic_0107283470_p1825119142351"><a name="en-us_topic_0107283470_p1825119142351"></a><a name="en-us_topic_0107283470_p1825119142351"></a>For more information about <strong id="en-us_topic_0107283470_b1672210449245"><a name="en-us_topic_0107283470_b1672210449245"></a><a name="en-us_topic_0107283470_b1672210449245"></a>Request</strong> and <strong id="en-us_topic_0107283470_b5722194432420"><a name="en-us_topic_0107283470_b5722194432420"></a><a name="en-us_topic_0107283470_b5722194432420"></a>Limit</strong>, see <a href="setting-container-specifications.md">Setting Container Specifications</a>.</p>
        <div class="p" id="en-us_topic_0107283470_p1684921311567"><a name="en-us_topic_0107283470_p1684921311567"></a><a name="en-us_topic_0107283470_p1684921311567"></a>GPU quotas: configurable only when the cluster contains GPU nodes.<a name="en-us_topic_0107283470_ul1634514911568"></a><a name="en-us_topic_0107283470_ul1634514911568"></a><ul id="en-us_topic_0107283470_ul1634514911568"><li><strong id="en-us_topic_0107283470_b42101842349"><a name="en-us_topic_0107283470_b42101842349"></a><a name="en-us_topic_0107283470_b42101842349"></a>GPU</strong>: the percentage of GPU resources reserved for a container. Select <span class="uicontrol" id="en-us_topic_0107283470_uicontrol19942102410563"><a name="en-us_topic_0107283470_uicontrol19942102410563"></a><a name="en-us_topic_0107283470_uicontrol19942102410563"></a><b>Use</b></span> and set the percentage. For example, if this parameter is set to 10%, the container is allowed to use 10% of GPU resources. If you do not select <span class="uicontrol" id="en-us_topic_0107283470_uicontrol13191233125719"><a name="en-us_topic_0107283470_uicontrol13191233125719"></a><a name="en-us_topic_0107283470_uicontrol13191233125719"></a><b>Use</b></span> or set this parameter to 0, no GPU resources can be used.</li><li><strong id="en-us_topic_0107283470_b20489865364"><a name="en-us_topic_0107283470_b20489865364"></a><a name="en-us_topic_0107283470_b20489865364"></a>GPU/Graphics Card</strong>: The workload's pods will be scheduled to the node with the specified GPU. If <strong id="en-us_topic_0107283470_b376171219323"><a name="en-us_topic_0107283470_b376171219323"></a><a name="en-us_topic_0107283470_b376171219323"></a>Any GPU type</strong> is selected, the container uses a random GPU in the node. If you select a specific GPU, the container uses this GPU.</li></ul>
        </div>
        </td>
        </tr>
        </tbody>
        </table>

    3.  Configure the container lifecycle: Set the commands for starting and running containers.
        -   **Startup Command**: executed when the workload is started. For details, see  [Setting Container Startup Commands](setting-container-startup-commands.md).
        -   **Post-Start Processing**: executed after the workload runs successfully. For more information, see  [Setting Container Lifecycle Parameters](setting-container-lifecycle-parameters.md).
        -   **Pre-Stop Processing**: executed to delete logs or temporary files before the workload ends. For more information, see  [Setting Container Lifecycle Parameters](setting-container-lifecycle-parameters.md).

    4.  Configure the health check function to check whether containers and services are running properly. CCE provides two types of probes: liveness probes and readiness probes. For more information, see  [Setting Health Check for a Container](setting-health-check-for-a-container.md).
        -   **Workload Liveness Probe**: restarts the unhealthy container.
        -   **Workload Service Probe**: changes the container to the unready state when detecting that the container is unhealthy. In this way, service traffic will not be directed to the container.

    5.  Configure environment variables. Environment variables can be added to a container. In general, environment variables are used to set parameters.

        On the  **Environment Variables**  tab page, click  **Add Environment Variables**. Add an environment variable in one of the following ways:

        -   **Added manually**: Set  **Variable Name**  and  **Variable Value/Reference**.
        -   **Added from Secret**: Set  **Variable Name**  and select the desired secret name and data. A secret must be created in advance. For details, see  [Creating a Secret](creating-a-secret.md).
        -   **Added from ConfigMap**: Set  **Variable Name**  and select the desired ConfigMap name and data. A ConfigMap must be created in advance. For details, see  [Creating a ConfigMap](creating-a-configmap.md).

    6.  Mount data storage to containers for persistent storage and high disk I/O. For details, see  [Storage Management](storage_management).
    7.  Configure container permissions to protect CCE and other containers from being affected.

        Enter the user ID to set container permissions and prevent systems and other containers from being affected.

    8.  Configure the log collection policies and log directory to collect container logs for unified management and analysis. For details, see  [Collecting Standard Output Logs of Containers](collecting-standard-output-logs-of-containers.md)  and  [Collecting Container Logs from Specified Paths](collecting-container-logs-from-specified-paths.md).

4.  Click  **Next**  and set headless service parameters, as shown in  [Table 3](#table9558885552).

    **Table  3**  Headless service parameters

    <a name="table9558885552"></a>
    <table><thead align="left"><tr id="row656715819558"><th class="cellrowborder" valign="top" width="18.01%" id="mcps1.2.3.1.1"><p id="p14572108155517"><a name="p14572108155517"></a><a name="p14572108155517"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="81.99%" id="mcps1.2.3.1.2"><p id="p2057528175518"><a name="p2057528175518"></a><a name="p2057528175518"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19578881559"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.3.1.1 "><p id="p05829820555"><a name="p05829820555"></a><a name="p05829820555"></a>Service Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.99%" headers="mcps1.2.3.1.2 "><p id="p1958612895516"><a name="p1958612895516"></a><a name="p1958612895516"></a>Name of the service corresponding to the workload for mutual access between instances. This service is used for internal discovery of instances, and does not require an independent IP address or load balancing.</p>
    </td>
    </tr>
    <tr id="row259512817559"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.3.1.1 "><p id="p560098185519"><a name="p560098185519"></a><a name="p560098185519"></a>Port Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.99%" headers="mcps1.2.3.1.2 "><p id="p8604184555"><a name="p8604184555"></a><a name="p8604184555"></a>Name of the container port. You are advised to enter a name that indicates the function of the port.</p>
    </td>
    </tr>
    <tr id="row1060528115514"><td class="cellrowborder" valign="top" width="18.01%" headers="mcps1.2.3.1.1 "><p id="p260917817552"><a name="p260917817552"></a><a name="p260917817552"></a>Container Port</p>
    </td>
    <td class="cellrowborder" valign="top" width="81.99%" headers="mcps1.2.3.1.2 "><p id="p26129811555"><a name="p26129811555"></a><a name="p26129811555"></a>Listening port inside the container.</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **Add Service**  and set the workload access type.

    If your workload will be reachable to other workloads or public networks, add a service to define the workload access type.

    The workload access type determines the network attributes of the workload. Workloads with different access types can provide different network capabilities. For details, see  [Network Overview](network-overview.md).

6.  Click  **Next**  and configure advanced settings.
    -   **Upgrade Policy**: Only  **Rolling Upgrade**  is supported.
    -   **Pod Management Policy**: There are two types of policies: ordered and parallel.
        -   **Ordered**: The StatefulSet will deploy, delete, or scale pods in order and one by one \(The StatefulSet waits until each pod is ready before continuing\).
        -   **Parallel**: The StatefulSet will create pods in parallel to match the desired scale without waiting, and will delete all pods at once.

    -   **Graceful Deletion**: On the  **Graceful Time Window \(s\)**  page, set a time window \(0–9999s\) for pre-stop commands to finish execution before a workload is deleted. The default value is 30s. The graceful scale-in policy provides a time window for workload deletion and is reserved for executing commands in the PreStop phase in the lifecycle. If workload processes are not terminated after the time window elapses, the workload will be forcibly deleted.
    -   **Scheduling Policies**: You can combine static global scheduling policies or dynamic runtime scheduling policies as required. For more information, see  [Scheduling Policy Overview](scheduling-policy-overview.md).
    -   **Advanced Pod Settings**  \>  **User-Defined Label**: Built-in app labels are specified during workload creation and cannot be modified. You can click  **Add Label**  to add labels.
    -   **Client DNS Configuration**: A CCE cluster has a built-in DNS add-on \(CoreDNS\) to provide domain name resolution for workloads in the cluster. For details, see  [Using Kubernetes In-Cluster DNS](using-kubernetes-in-cluster-dns.md).
        -   **DNS Policy**:
            -   **ClusterFirst**: The default DNS configuration overrides the  **Nameserver**  and  **DNS Search Domain**  configurations of the client.
            -   **None**: The pod uses the following configurations of the client.
            -   **Default**: The pod inherits the DNS configuration from the node on which the pods run.

        -   **Nameserver**: You can configure a domain name server for a user-defined domain name. The value is one or a group of DNS IP addresses, for example, 1.2.3.4.
        -   **DNS Search Domain**: a search list for host-name lookup. When a domain name cannot be resolved, DNS queries will be attempted combining the domain name with each domain in the search list in turn until a match is found or all domains in the search list are tried.
        -   **Timeout \(s\)**: the amount of time the resolver will wait for a response from a remote name server before retrying the query on a different name server. Set it based on the site requirements.
        -   **ndots**: threshold for the number of dots that must appear in a domain name before an initial absolute query will be made. If a domain name has  **ndots**  or more than  **ndots**  dots, the name is a fully qualified domain name \(FQDN\) and will be tried first as an absolute name. If a domain name has less than  **ndots**  dots, the operating system will look up the name in a list of search domain names.

7.  Click  **Create**  and then  **Back to StatefulSet List**.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   If the workload is in the  **Running**  state, it has been successfully created.  
    >-   Workload status is not updated in real time. Click  ![](figures/icon-upgrade.png)  in the upper right corner or press  **F5**  to refresh the page.  
    >-   If the workload list contains more than 500 records, the Kubernetes pagination mechanism will be used. Specifically, you can only go to the first page or the next page, but cannot go to the previous page. In addition, if resources are divided into discrete pages, the total number of resources displayed is the maximum number of resources that can be queried at a time, not the actual total number of resources.  


## Using kubectl<a name="section113441881214"></a>

The following procedure uses an etcd workload as an example to describe how to create a workload using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

1.  Log in to the ECS on which kubectl has been configured. For details, see  [Logging In to a Linux ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0013771089.html).
2.  Create and edit the  **etcd-statefulset.yaml**  file.

    **etcd-statefulset.yaml**  is an example file name, and you can change it as required.

    **vi etcd-statefulset.yaml**

    The following provides an example of the file contents.

    ```
    apiVersion: apps/v1beta1
    kind: StatefulSet
    metadata:
      name: etcd
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: etcd
      serviceName: etcd-svc
      template:
        metadata:
          labels:
            app: etcd
        spec:
          containers:
          - env:
            - name: PAAS_APP_NAME
              value: tesyhhj
            - name: PAAS_NAMESPACE
              value: default
            - name: PAAS_PROJECT_ID
              value: 9632fae707ce4416a0ab1e3e121fe555
            image: etcd
            imagePullPolicy: IfNotPresent
            name: container-0
      updateStrategy:
        type: RollingUpdate
    ```

    For details about deployment.yaml parameters, see  [Table 4](#table132326831016). For more information on StatefulSet, see the  [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/).

    **Table  4**  etcd-statefulset.yaml parameters

    <a name="table132326831016"></a>
    <table><thead align="left"><tr id="row523318817104"><th class="cellrowborder" valign="top" width="37%" id="mcps1.2.4.1.1"><p id="p162344817100"><a name="p162344817100"></a><a name="p162344817100"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="47%" id="mcps1.2.4.1.2"><p id="p16234138161012"><a name="p16234138161012"></a><a name="p16234138161012"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="16%" id="mcps1.2.4.1.3"><p id="p102881159151016"><a name="p102881159151016"></a><a name="p102881159151016"></a>Mandatory/Optional</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row112346841018"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p182345811107"><a name="p182345811107"></a><a name="p182345811107"></a>apiVersion</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p2023458141014"><a name="p2023458141014"></a><a name="p2023458141014"></a>API version.</p>
    <div class="note" id="note143305521379"><a name="note143305521379"></a><a name="note143305521379"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19331452133715"><a name="p19331452133715"></a><a name="p19331452133715"></a>For clusters earlier than 1.9, the apiVersion format of StatefulSets is extensions/v1beta1. For clusters later than 1.9, the apiVersion format can be extensions/v1beta1 or apps/v1. Set this parameter based on the cluster version.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p6234158101019"><a name="p6234158101019"></a><a name="p6234158101019"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row202347814100"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p172342815109"><a name="p172342815109"></a><a name="p172342815109"></a>kind</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p142346871019"><a name="p142346871019"></a><a name="p142346871019"></a>Type of a created object.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p2023416841019"><a name="p2023416841019"></a><a name="p2023416841019"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row1459172931315"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p1659232941311"><a name="p1659232941311"></a><a name="p1659232941311"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p165932298137"><a name="p165932298137"></a><a name="p165932298137"></a>Metadata of a resource object.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p16593112941310"><a name="p16593112941310"></a><a name="p16593112941310"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row33638545115"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p036575412114"><a name="p036575412114"></a><a name="p036575412114"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p1036510541116"><a name="p1036510541116"></a><a name="p1036510541116"></a>Name of a statefulset.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p1936585415110"><a name="p1936585415110"></a><a name="p1936585415110"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row52341382109"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p2234188171017"><a name="p2234188171017"></a><a name="p2234188171017"></a>Spec</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p1023414811012"><a name="p1023414811012"></a><a name="p1023414811012"></a>Detailed description of the statefulset.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p92341186101"><a name="p92341186101"></a><a name="p92341186101"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row490820516139"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p99089513134"><a name="p99089513134"></a><a name="p99089513134"></a>replicas</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p1890815551313"><a name="p1890815551313"></a><a name="p1890815551313"></a>Number of instances.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p1390895141312"><a name="p1390895141312"></a><a name="p1390895141312"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row29372135139"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p1493821315132"><a name="p1493821315132"></a><a name="p1493821315132"></a>selector</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p10938171341312"><a name="p10938171341312"></a><a name="p10938171341312"></a>Container instance that can be managed by the statefulset.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p5939181320135"><a name="p5939181320135"></a><a name="p5939181320135"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row1862113722419"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p20622163762419"><a name="p20622163762419"></a><a name="p20622163762419"></a>serviceName</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p1662293742419"><a name="p1662293742419"></a><a name="p1662293742419"></a>Service Name.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p106221537172410"><a name="p106221537172410"></a><a name="p106221537172410"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row793916134135"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p14939131391317"><a name="p14939131391317"></a><a name="p14939131391317"></a>template</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p993921331312"><a name="p993921331312"></a><a name="p993921331312"></a>Detailed description of a created container instance.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p1193919138132"><a name="p1193919138132"></a><a name="p1193919138132"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row69398139139"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p132126496218"><a name="p132126496218"></a><a name="p132126496218"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p10939121391317"><a name="p10939121391317"></a><a name="p10939121391317"></a>Metadata.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p4939161321314"><a name="p4939161321314"></a><a name="p4939161321314"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row1479918372441"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p67994378445"><a name="p67994378445"></a><a name="p67994378445"></a>labels</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p1680012377440"><a name="p1680012377440"></a><a name="p1680012377440"></a><strong id="b842352706115258"><a name="b842352706115258"></a><a name="b842352706115258"></a>metadata.labels</strong>: Container labels.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p180033714449"><a name="p180033714449"></a><a name="p180033714449"></a>Optional</p>
    </td>
    </tr>
    <tr id="row6939151316138"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p793911361316"><a name="p793911361316"></a><a name="p793911361316"></a>spec:</p>
    <p id="p17330235102212"><a name="p17330235102212"></a><a name="p17330235102212"></a>containers</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><a name="ul48282256265"></a><a name="ul48282256265"></a><ul id="ul48282256265"><li><strong id="b112303267291"><a name="b112303267291"></a><a name="b112303267291"></a>env</strong>: List of environment variables to set in the container.</li><li><strong id="b021334265015"><a name="b021334265015"></a><a name="b021334265015"></a>image</strong> (mandatory): Name of a container image.</li><li><strong id="b04931854185511"><a name="b04931854185511"></a><a name="b04931854185511"></a>imagePullPolicy</strong> (optional): Policy for obtaining an image. The options include <strong id="b47004369113256"><a name="b47004369113256"></a><a name="b47004369113256"></a>Always</strong> (attempting to download images each time), <strong id="b1385119962113256"><a name="b1385119962113256"></a><a name="b1385119962113256"></a>Never</strong> (only using local images), and <strong id="b1264351417113256"><a name="b1264351417113256"></a><a name="b1264351417113256"></a>IfNotPresent</strong> (using local images if they are available; downloading images if local images are unavailable). The default value is <strong id="b184934519113256"><a name="b184934519113256"></a><a name="b184934519113256"></a>Always</strong>.</li><li><strong id="b710815216563"><a name="b710815216563"></a><a name="b710815216563"></a>name</strong> (mandatory): Container name.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p1193991381318"><a name="p1193991381318"></a><a name="p1193991381318"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row1748132412341"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p8483152412349"><a name="p8483152412349"></a><a name="p8483152412349"></a>updateStrategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p122191850171118"><a name="p122191850171118"></a><a name="p122191850171118"></a>Upgrade mode. Only <strong id="b1067492619123"><a name="b1067492619123"></a><a name="b1067492619123"></a>Rolling Upgrade</strong> is supported.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p348372443419"><a name="p348372443419"></a><a name="p348372443419"></a>Optional</p>
    </td>
    </tr>
    </tbody>
    </table>

    **vi etcd-headless.yaml**

    ```
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: etcd
      name: etcd-svc
    spec:
      clusterIP: None
      ports:
      - name: etcd-svc
        port: 3120
        protocol: TCP
        targetPort: 3120
      selector:
        app: etcd
      sessionAffinity: None
      type: ClusterIP
    ```

    For details about etcd-headless.yaml parameters, see  [Table 5](#table19812058154417).

    **Table  5**  etcd-headless.yaml parameters

    <a name="table19812058154417"></a>
    <table><thead align="left"><tr id="row1598185814449"><th class="cellrowborder" valign="top" width="28.29%" id="mcps1.2.4.1.1"><p id="p49811258174414"><a name="p49811258174414"></a><a name="p49811258174414"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="52.59%" id="mcps1.2.4.1.2"><p id="p17981125854418"><a name="p17981125854418"></a><a name="p17981125854418"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="19.12%" id="mcps1.2.4.1.3"><p id="p198120582445"><a name="p198120582445"></a><a name="p198120582445"></a>Mandatory/Optional</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1982175811449"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p18982155834413"><a name="p18982155834413"></a><a name="p18982155834413"></a>apiVersion</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="p79821658184416"><a name="p79821658184416"></a><a name="p79821658184416"></a>API version.</p>
    <div class="note" id="note5982165884411"><a name="note5982165884411"></a><a name="note5982165884411"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p20982758114411"><a name="p20982758114411"></a><a name="p20982758114411"></a>For clusters earlier than 1.9, the apiVersion format of StatefulSets is extensions/v1beta1. For clusters later than 1.9, the apiVersion format can be extensions/v1beta1 or apps/v1. Set this parameter based on the cluster version.</p>
    </div></div>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p1498215844414"><a name="p1498215844414"></a><a name="p1498215844414"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row69821258204415"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p19982145834411"><a name="p19982145834411"></a><a name="p19982145834411"></a>kind</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="p3983155844411"><a name="p3983155844411"></a><a name="p3983155844411"></a>Type of a created object.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p17983858194417"><a name="p17983858194417"></a><a name="p17983858194417"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row2983115816445"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p798318588449"><a name="p798318588449"></a><a name="p798318588449"></a>metadata</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="p4983195814415"><a name="p4983195814415"></a><a name="p4983195814415"></a>Metadata of a resource object.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p69833588446"><a name="p69833588446"></a><a name="p69833588446"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row1841232325412"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p10412182319545"><a name="p10412182319545"></a><a name="p10412182319545"></a>labels</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="p12609333316"><a name="p12609333316"></a><a name="p12609333316"></a><strong id="b16104338117"><a name="b16104338117"></a><a name="b16104338117"></a>metadata.labels</strong>: Container labels.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p241362318544"><a name="p241362318544"></a><a name="p241362318544"></a>Optional</p>
    </td>
    </tr>
    <tr id="row398395834412"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p49830588444"><a name="p49830588444"></a><a name="p49830588444"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="p6983175819448"><a name="p6983175819448"></a><a name="p6983175819448"></a>Name of a service.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p79832058144416"><a name="p79832058144416"></a><a name="p79832058144416"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row119831958144413"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p19834588445"><a name="p19834588445"></a><a name="p19834588445"></a>spec</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="p16983458164412"><a name="p16983458164412"></a><a name="p16983458164412"></a>Detailed description of the service.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p7984145810442"><a name="p7984145810442"></a><a name="p7984145810442"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row7780329175518"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p478092919554"><a name="p478092919554"></a><a name="p478092919554"></a>clusterIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0079615000_p9091997"><a name="zh-cn_topic_0079615000_p9091997"></a><a name="zh-cn_topic_0079615000_p9091997"></a>ClusterIP is usually assigned by the master and is the IP address of the service.</p>
    <p id="zh-cn_topic_0079615000_p14719114"><a name="zh-cn_topic_0079615000_p14719114"></a><a name="zh-cn_topic_0079615000_p14719114"></a>The value of this parameter is <strong id="zh-cn_topic_0079615000_b65363170"><a name="zh-cn_topic_0079615000_b65363170"></a><a name="zh-cn_topic_0079615000_b65363170"></a>NONE</strong> or a valid IP address.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p17780142913555"><a name="p17780142913555"></a><a name="p17780142913555"></a>Optional</p>
    </td>
    </tr>
    <tr id="row166904265554"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p9691102645511"><a name="p9691102645511"></a><a name="p9691102645511"></a>ports</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><a name="ul46731616208"></a><a name="ul46731616208"></a><ul id="ul46731616208"><li><strong id="b15251122710013"><a name="b15251122710013"></a><a name="b15251122710013"></a>name</strong>: The name of this port within the service.</li><li><strong id="b08461724508"><a name="b08461724508"></a><a name="b08461724508"></a>port</strong>: The port that will be exposed by this service.</li><li><strong id="b452318225012"><a name="b452318225012"></a><a name="b452318225012"></a>protocol</strong>: The IP protocol for this port.</li><li><strong id="b1824652015012"><a name="b1824652015012"></a><a name="b1824652015012"></a>targetPort</strong>: Number or name of the port to access on the pods targeted by the service.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p106911226125516"><a name="p106911226125516"></a><a name="p106911226125516"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row174141123165517"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p841419236553"><a name="p841419236553"></a><a name="p841419236553"></a>selector</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="p14141423165510"><a name="p14141423165510"></a><a name="p14141423165510"></a>This service will route traffic to pods having labels matching this selector.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p1841420237553"><a name="p1841420237553"></a><a name="p1841420237553"></a>Optional</p>
    </td>
    </tr>
    <tr id="row42632490014"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p172639492017"><a name="p172639492017"></a><a name="p172639492017"></a>sessionAffinity</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="zh-cn_topic_0079615000_p60715427"><a name="zh-cn_topic_0079615000_p60715427"></a><a name="zh-cn_topic_0079615000_p60715427"></a>Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p92631649107"><a name="p92631649107"></a><a name="p92631649107"></a>Optional</p>
    </td>
    </tr>
    <tr id="row32274598013"><td class="cellrowborder" valign="top" width="28.29%" headers="mcps1.2.4.1.1 "><p id="p62278591107"><a name="p62278591107"></a><a name="p62278591107"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="52.59%" headers="mcps1.2.4.1.2 "><p id="p192271859000"><a name="p192271859000"></a><a name="p192271859000"></a>Type of exposed service.</p>
    </td>
    <td class="cellrowborder" valign="top" width="19.12%" headers="mcps1.2.4.1.3 "><p id="p112279598019"><a name="p112279598019"></a><a name="p112279598019"></a>Optional</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Create a workload and the corresponding headless service.

    **kubectl create -f etcd-statefulset.yaml**

    If the following information is displayed, the StatefulSet has been successfully created.

    ```
    statefulset "etcd" created
    ```

    **kubectl create -f  **etcd-headless**.yaml**

    If the following information is displayed, the headless service has been successfully created.

    ```
    service "etcd-svc" created
    ```

4.  If the workload will be accessed through a ClusterIP or NodePort service, set the corresponding workload access type. For details, see  [Network Management](network_management).

