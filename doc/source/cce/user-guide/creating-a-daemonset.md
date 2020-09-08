# Creating a DaemonSet<a name="cce_01_0216"></a>

CCE provides deployment and management capabilities for multiple types of containers and supports features of container workloads, including creation, configuration, monitoring, scaling, upgrade, uninstallation, service discovery, and load balancing.

DaemonSet ensures that only one pod runs on all or some nodes. When a node is added to a cluster, a new pod is also added for the node. When a node is removed from a cluster, the pod is also reclaimed. If a DaemonSet is deleted, all pods created by it will be deleted.

The typical application scenarios of a DaemonSet are as follows:

-   Run the cluster storage daemon, such as glusterd or ceph, on each node.
-   Run the log collection daemon, such as Flunentd or Logstash, on each node.
-   Run the monitoring daemon, such as Prometheus Node Exporter, collectd, Datadog agent, New Relic agent, or Ganglia gmond, on each node.

In a simple case, one DaemonSet, covering all nodes, will be used for each type of daemon. A more complex setup may use multiple DaemonSets for a single type of daemon, but with different flags and/or different memory and CPU requests for different hardware types.

## Preparations<a name="section7271245481"></a>

You must have one cluster available before creating a DaemonSet. For details on how to create a cluster, see  [Creating a Hybrid Cluster](creating-a-hybrid-cluster.md).

## Procedure<a name="section1578617172401"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **DaemonSets**. On the displayed page, click  **Create** **DaemonSet**.
2.  Set basic workload parameters as described in  [Table 1](#table12741447488). The parameters marked with an asterisk \(\*\) are mandatory.

    **Table  1**  Basic workload parameters

    <a name="table12741447488"></a>
    <table><thead align="left"><tr id="row52758419481"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p152759464816"><a name="p152759464816"></a><a name="p152759464816"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p3275134114811"><a name="p3275134114811"></a><a name="p3275134114811"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row18415163712618"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p32763416485"><a name="p32763416485"></a><a name="p32763416485"></a>* Workload Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p5276341485"><a name="p5276341485"></a><a name="p5276341485"></a>Name of the workload to be created. The name must be unique.</p>
    </td>
    </tr>
    <tr id="row81437181202"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p514451811010"><a name="p514451811010"></a><a name="p514451811010"></a>* Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p323714215492"><a name="p323714215492"></a><a name="p323714215492"></a>Cluster in which the workload resides.</p>
    </td>
    </tr>
    <tr id="row169810201307"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p19698152011011"><a name="p19698152011011"></a><a name="p19698152011011"></a>* Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p12447336131710"><a name="p12447336131710"></a><a name="p12447336131710"></a>In a single cluster, data in different namespaces is isolated from each other. This enables applications to share the services of the same cluster without interfering each other. If no namespace is set, the default namespace is used.</p>
    </td>
    </tr>
    <tr id="row18442191224514"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p244261214513"><a name="p244261214513"></a><a name="p244261214513"></a>Time Zone Synchronization</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p644215125454"><a name="p644215125454"></a><a name="p644215125454"></a>If <strong id="b842352706164155"><a name="b842352706164155"></a><a name="b842352706164155"></a>ON</strong> is selected, the container and the node use the same time zone.</p>
    <div class="notice" id="note5422953172616"><a name="note5422953172616"></a><a name="note5422953172616"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p11422145392614"><a name="p11422145392614"></a><a name="p11422145392614"></a>After time zone synchronization is enabled, disks of the HostPath type will be automatically added and listed in the <strong id="b84235270616465"><a name="b84235270616465"></a><a name="b84235270616465"></a>Data Storage</strong> &gt; <strong id="b84235270616468"><a name="b84235270616468"></a><a name="b84235270616468"></a>Local Disk</strong> area. Do not modify or delete the disks.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1027719414818"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1527715418485"><a name="p1527715418485"></a><a name="p1527715418485"></a>Description</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p827734134817"><a name="p827734134817"></a><a name="p827734134817"></a>Description of the workload.</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **Next: Add Container**  to add a container.
    1.  Click  **Add Container**  and select the image to be deployed.
        -   **My Images**: Create a workload using an image in the image repository you created.
        -   **Third-Party Images**: Create a workload using an image from any third-party image repository \(image repositories other than SWR\). When you create a workload using a third-party image, ensure that the node where the workload is running can access public networks. For details on how to create a workload using a third-party image, see  [Using a Third-Party Image](using-a-third-party-image.md).
            -   If your image repository does not require authentication, set  **Authenticate Secret**  to  **No**, enter an image address, and then click  **OK**.
            -   If your image repository must be authenticated \(account and password\), you need to create a key and then use a third-party image. For details, see  [Using a Third-Party Image](using-a-third-party-image.md).

        -   **Shared Images**: Create a workload using an image shared by another tenant through the SWR service.

    2.  Configure basic image information.

        **Table  2**  Image parameters

        <a name="en-us_topic_0203988109_table128216444815"></a>
        <table><thead align="left"><tr id="en-us_topic_0203988109_row0282348486"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="en-us_topic_0203988109_p3282147483"><a name="en-us_topic_0203988109_p3282147483"></a><a name="en-us_topic_0203988109_p3282147483"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="en-us_topic_0203988109_p1828244144819"><a name="en-us_topic_0203988109_p1828244144819"></a><a name="en-us_topic_0203988109_p1828244144819"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="en-us_topic_0203988109_row1844916557597"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0203988109_p182837474815"><a name="en-us_topic_0203988109_p182837474815"></a><a name="en-us_topic_0203988109_p182837474815"></a>Image Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0203988109_p3283134134820"><a name="en-us_topic_0203988109_p3283134134820"></a><a name="en-us_topic_0203988109_p3283134134820"></a>Name of the image. You can click <strong id="en-us_topic_0203988109_b84235270617012"><a name="en-us_topic_0203988109_b84235270617012"></a><a name="en-us_topic_0203988109_b84235270617012"></a>Change Image</strong> to update it.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0203988109_row338117362515"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0203988109_p1038143616517"><a name="en-us_topic_0203988109_p1038143616517"></a><a name="en-us_topic_0203988109_p1038143616517"></a>* Image Version</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0203988109_p1338110368519"><a name="en-us_topic_0203988109_p1338110368519"></a><a name="en-us_topic_0203988109_p1338110368519"></a>Version of the image to be deployed.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0203988109_row32839494813"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0203988109_p122831140486"><a name="en-us_topic_0203988109_p122831140486"></a><a name="en-us_topic_0203988109_p122831140486"></a>* Container Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0203988109_p528314415486"><a name="en-us_topic_0203988109_p528314415486"></a><a name="en-us_topic_0203988109_p528314415486"></a>Name of the container. You can modify it.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0203988109_row1449911299503"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0203988109_p53374336504"><a name="en-us_topic_0203988109_p53374336504"></a><a name="en-us_topic_0203988109_p53374336504"></a>Privileged Container</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0203988109_p49887211526"><a name="en-us_topic_0203988109_p49887211526"></a><a name="en-us_topic_0203988109_p49887211526"></a>Programs in a privileged container have certain privileges.</p>
        <p id="en-us_topic_0203988109_p65001729105011"><a name="en-us_topic_0203988109_p65001729105011"></a><a name="en-us_topic_0203988109_p65001729105011"></a>If <strong id="en-us_topic_0203988109_b13252222105114"><a name="en-us_topic_0203988109_b13252222105114"></a><a name="en-us_topic_0203988109_b13252222105114"></a>Privileged Container</strong> is <strong id="en-us_topic_0203988109_b11849182725112"><a name="en-us_topic_0203988109_b11849182725112"></a><a name="en-us_topic_0203988109_b11849182725112"></a>On</strong>, the container is granted superuser permissions. For example, privileged containers can manipulate network devices on the host machine and modify kernel parameters.</p>
        </td>
        </tr>
        <tr id="en-us_topic_0203988109_row152831345485"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0203988109_p875325925918"><a name="en-us_topic_0203988109_p875325925918"></a><a name="en-us_topic_0203988109_p875325925918"></a>Container Resources</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0203988109_p5379182494610"><a name="en-us_topic_0203988109_p5379182494610"></a><a name="en-us_topic_0203988109_p5379182494610"></a>CPU quotas:</p>
        <a name="en-us_topic_0203988109_ul67283495467"></a><a name="en-us_topic_0203988109_ul67283495467"></a><ul id="en-us_topic_0203988109_ul67283495467"><li><strong id="en-us_topic_0203988109_b837912315811"><a name="en-us_topic_0203988109_b837912315811"></a><a name="en-us_topic_0203988109_b837912315811"></a>Request</strong>: the minimum number of CPU cores required by a container. The default value is 0.25 core.</li><li><strong id="en-us_topic_0203988109_b1728781088"><a name="en-us_topic_0203988109_b1728781088"></a><a name="en-us_topic_0203988109_b1728781088"></a>Limit</strong>: the maximum number of CPU cores available for a container. Do not leave <strong id="en-us_topic_0203988109_b71778281894"><a name="en-us_topic_0203988109_b71778281894"></a><a name="en-us_topic_0203988109_b71778281894"></a>Limit</strong> unspecified. Otherwise, intensive use of container resources will occur and your workload may exhibit unexpected behavior.</li></ul>
        <p id="en-us_topic_0203988109_p633394210502"><a name="en-us_topic_0203988109_p633394210502"></a><a name="en-us_topic_0203988109_p633394210502"></a>Memory quotas:</p>
        <a name="en-us_topic_0203988109_ul14326165915010"></a><a name="en-us_topic_0203988109_ul14326165915010"></a><ul id="en-us_topic_0203988109_ul14326165915010"><li><strong id="en-us_topic_0203988109_b2325104041116"><a name="en-us_topic_0203988109_b2325104041116"></a><a name="en-us_topic_0203988109_b2325104041116"></a>Request</strong>: the minimum amount of memory required by a container. The default value is 512 MiB.</li><li><strong id="en-us_topic_0203988109_b4467144318115"><a name="en-us_topic_0203988109_b4467144318115"></a><a name="en-us_topic_0203988109_b4467144318115"></a>Limit</strong>: the maximum amount of memory available for a container. When memory usage exceeds the specified memory limit, the container will be terminated.</li></ul>
        <p id="en-us_topic_0203988109_p1825119142351"><a name="en-us_topic_0203988109_p1825119142351"></a><a name="en-us_topic_0203988109_p1825119142351"></a>For more information about <strong id="en-us_topic_0203988109_b1672210449245"><a name="en-us_topic_0203988109_b1672210449245"></a><a name="en-us_topic_0203988109_b1672210449245"></a>Request</strong> and <strong id="en-us_topic_0203988109_b5722194432420"><a name="en-us_topic_0203988109_b5722194432420"></a><a name="en-us_topic_0203988109_b5722194432420"></a>Limit</strong>, see <a href="setting-container-specifications.md">Setting Container Specifications</a>.</p>
        <div class="p" id="en-us_topic_0203988109_p1684921311567"><a name="en-us_topic_0203988109_p1684921311567"></a><a name="en-us_topic_0203988109_p1684921311567"></a>GPU quotas: configurable only when the cluster contains GPU nodes.<a name="en-us_topic_0203988109_ul1634514911568"></a><a name="en-us_topic_0203988109_ul1634514911568"></a><ul id="en-us_topic_0203988109_ul1634514911568"><li><strong id="en-us_topic_0203988109_b42101842349"><a name="en-us_topic_0203988109_b42101842349"></a><a name="en-us_topic_0203988109_b42101842349"></a>GPU</strong>: the percentage of GPU resources reserved for a container. Select <span class="uicontrol" id="en-us_topic_0203988109_uicontrol19942102410563"><a name="en-us_topic_0203988109_uicontrol19942102410563"></a><a name="en-us_topic_0203988109_uicontrol19942102410563"></a><b>Use</b></span> and set the percentage. For example, if this parameter is set to 10%, the container is allowed to use 10% of GPU resources. If you do not select <span class="uicontrol" id="en-us_topic_0203988109_uicontrol13191233125719"><a name="en-us_topic_0203988109_uicontrol13191233125719"></a><a name="en-us_topic_0203988109_uicontrol13191233125719"></a><b>Use</b></span> or set this parameter to 0, no GPU resources can be used.</li><li><strong id="en-us_topic_0203988109_b20489865364"><a name="en-us_topic_0203988109_b20489865364"></a><a name="en-us_topic_0203988109_b20489865364"></a>GPU/Graphics Card</strong>: The workload's pods will be scheduled to the node with the specified GPU. If <strong id="en-us_topic_0203988109_b376171219323"><a name="en-us_topic_0203988109_b376171219323"></a><a name="en-us_topic_0203988109_b376171219323"></a>Any GPU type</strong> is selected, the container uses a random GPU in the node. If you select a specific GPU, the container uses this GPU.</li></ul>
        </div>
        </td>
        </tr>
        </tbody>
        </table>

    3.  Configure the container lifecycle: Set the commands for starting and running containers.
        -   **Startup Command**: executed when the workload is started. For details, see  [Setting Container Startup Commands](setting-container-startup-commands.md).
        -   **Post-Start**: executed after the workload runs successfully. For more information, see  [Setting Container Lifecycle Parameters](setting-container-lifecycle-parameters.md).
        -   **Pre-Stop**: executed to delete logs or temporary files before the workload ends. For more information, see  [Setting Container Lifecycle Parameters](setting-container-lifecycle-parameters.md).

    4.  Configure the health check function to check whether containers and services are running properly. CCE provides two types of probes: liveness probes and readiness probes. For more information, see  [Setting Health Check for a Container](setting-health-check-for-a-container.md).
        -   **Liveness Probe**: restarts the unhealthy container.
        -   **Readiness Probe**: changes the container to the unready state when detecting that the container is unhealthy. In this way, service traffic will not be directed to the container.

    5.  Configure environment variables. Environment variables can be added to a container. In general, environment variables are used to set parameters.

        On the  **Environment Variables**  tab page, click  **Add Environment Variable**. Add an environment variable in one of the following ways:

        -   **Added manually**: Set  **Variable Name**  and  **Variable Value/Reference**.
        -   **Added from Secret**: Set  **Variable Name**  and select the desired secret name and data. A secret must be created in advance. For details, see  [Creating a Secret](creating-a-secret.md).
        -   **Added from ConfigMap**: Set  **Variable Name**  and select the desired ConfigMap name and data. A ConfigMap must be created in advance. For details, see  [Creating a ConfigMap](creating-a-configmap.md).

    6.  Mount data storage to containers for persistent storage and high disk I/O. For details, see  [Storage Management](storage_management).
    7.  Configure container permissions to protect CCE and other containers from being affected.

        Enter the user ID to set container permissions and prevent systems and other containers from being affected.

    8.  Configure the log collection policies and log directory to collect container logs for unified management and analysis. For details, see  [Collecting Standard Output Logs of Containers](collecting-standard-output-logs-of-containers.md)  and  [Collecting Container Logs from Specified Paths](collecting-container-logs-from-specified-paths.md).
    9.  \(Optional\) A pod contains one or more closely related containers. If your workload is a multi-container workload, click  **Add Container**  to add more containers.

4.  Click  **Next: Set Application Access**. Then, click  **Add Service**  and set the workload access type.

    If your workload will be reachable to other workloads or public networks, add a service to define the workload access type.

    The workload access type determines the network attributes of the workload. Workloads with different access types can provide different network capabilities. For details, see  [Network Overview](network-overview.md).

5.  Click  **Next: Configure Advanced Settings**  and configure advanced settings.
    -   **Upgrade Policy**: Only  **Rolling Upgrade**  is supported.

        **Rolling upgrade**: Gradually replaces an old pod with a new pod. During the upgrade, service traffic is evenly distributed to the old and new pods to ensure service continuity.

        **Maximum Number of Unavailable Pods**: Maximum number of unavailable pods allowed in a rolling upgrade. If the number is equal to the total number of pods, services may be interrupted. Minimum number of alive pods = Total pods – Maximum number of unavailable pods

    -   **Graceful Deletion**: On the  **Graceful Time Window \(s\)**  page, set a time window \(0–9999s\) for pre-stop commands to finish execution before a workload is deleted. The default value is 30s. The graceful scale-in policy provides a time window for workload deletion and is reserved for executing commands in the PreStop phase in the lifecycle. If workload processes are not terminated after the time window elapses, the workload will be forcibly deleted.
    -   **Scheduling Policies**: You can combine static global scheduling policies or dynamic runtime scheduling policies as required. For more information, see  [Scheduling Policy Overview](scheduling-policy-overview.md).
    -   **Advanced Pod Settings**  \>  **Pod Label**: Built-in app labels are specified during workload creation and cannot be modified. You can click  **Add Label**  to add labels.
    -   **Client DNS Configuration**: A CCE cluster has a built-in DNS add-on \(CoreDNS\) to provide domain name resolution for workloads in the cluster. For details, see  [Using Kubernetes In-Cluster DNS](using-kubernetes-in-cluster-dns.md).
        -   **DNS Policy**:
            -   **ClusterFirst**: The default DNS configuration overrides the  **Nameserver**  and  **DNS Search Domain**  configurations of the client.
            -   **None**: The pod uses the following configurations of the client.
            -   **Default**: The pod inherits the DNS configuration from the node on which the pods run.

        -   **Nameserver**: You can configure a domain name server for a user-defined domain name. The value is one or a group of DNS IP addresses, for example, 1.2.3.4.
        -   **DNS Search Domain**: a search list for host-name lookup. When a domain name cannot be resolved, DNS queries will be attempted combining the domain name with each domain in the search list in turn until a match is found or all domains in the search list are tried.
        -   **Timeout \(s\)**: the amount of time the resolver will wait for a response from a remote name server before retrying the query on a different name server. Set it based on the site requirements.
        -   **ndots**: threshold for the number of dots that must appear in a domain name before an initial absolute query will be made. If a domain name has  **ndots**  or more than  **ndots**  dots, the name is a fully qualified domain name \(FQDN\) and will be tried first as an absolute name. If a domain name has less than  **ndots**  dots, the operating system will look up the name in a list of search domain names.

6.  Click  **Create**. Then, click  **Back to Deployment List**  to view the workload status.

    If the workload is in the  **Running**  state, it has been successfully created.

    Workload status is not updated in real time. Click  ![](figures/icon-upgrade-5.png)  in the upper right corner or press  **F5**  to refresh the page.


