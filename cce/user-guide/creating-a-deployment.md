# Creating a Deployment<a name="cce_01_0047"></a>

Deployments are workloads \(for example, Nginx\) that do not store any data or status.

## Prerequisites<a name="section7271245481"></a>

-   Before creating a containerized workload, you must have an available cluster. For details on how to create a cluster, see  [Creating a Hybrid Cluster](creating-a-hybrid-cluster.md).

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >When creating multiple containerized workloads, ensure that each container has a unique port. Otherwise, workload creation will fail.

-   To enable access to a workload from a public network, ensure that an elastic IP address \(EIP\) has been bound to or a load balancer has been configured for at least one node in the cluster.

## Using the CCE Console<a name="section1996635141916"></a>

1.  CCE provides multiple methods for creating a workload. You can use any of the following methods:
    -   Use a third-party image to create a workload, without the need to upload an image.
    -   Perform required operations on the  **My Images**  page on the CCE console to create a workload, you need to upload the image to the Software Repository for Container \(SWR\). For details about how to upload an image, see  [Image Repository](image-repository.md).
    -   Use a shared image to create a workload. Specifically, other tenants share an image with you by using the SWR service.
    -   Use a YAML file to create a workload. You can click  **Create YAML**  on the right of the  **Create Deployment**  page. For details about YAML, see  [Using kubectl](#section155246177178). After the YAML file is written, click  **Create**  to create a workload.

        >![](public_sys-resources/icon-note.gif) **NOTE:** 
        >Settings in the YAML file are synchronized with settings on the console. You can also interact with the YAML to create a workload. For example, if you enter a workload name on the console, the name will automatically appear in the YAML file. Similarly, if you add an image on the console, the image will be automatically added to the YAML file.


2.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**. On the displayed page, click  **Create Deployment**. Set basic workload parameters as described in  [Table 1](#table12741447488). The parameters marked with an asterisk \(\*\) are mandatory.

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
    <tr id="row165805182316"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p45913512317"><a name="p45913512317"></a><a name="p45913512317"></a>* Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1042648123717"><a name="p1042648123717"></a><a name="p1042648123717"></a>Number of instances in the workload. A workload can have one or more instances. You can set the number of instances. The default value is <strong id="b842352706154640"><a name="b842352706154640"></a><a name="b842352706154640"></a>2</strong> and can be set to <strong id="b842352706154646"><a name="b842352706154646"></a><a name="b842352706154646"></a>1</strong>.</p>
    <p id="p17713926910"><a name="p17713926910"></a><a name="p17713926910"></a>Each workload instance consists of the same containers. Configuring multiple instances for a workload ensures that the workload can still run properly even if an instance is faulty. If only one instance is used, a node or instance exception may cause service exceptions.</p>
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

        <a name="table128216444815"></a>
        <table><thead align="left"><tr id="row0282348486"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p3282147483"><a name="p3282147483"></a><a name="p3282147483"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p1828244144819"><a name="p1828244144819"></a><a name="p1828244144819"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1844916557597"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p182837474815"><a name="p182837474815"></a><a name="p182837474815"></a>Image Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p3283134134820"><a name="p3283134134820"></a><a name="p3283134134820"></a>Name of the image. You can click <strong id="b84235270617012"><a name="b84235270617012"></a><a name="b84235270617012"></a>Change Image</strong> to update it.</p>
        </td>
        </tr>
        <tr id="row338117362515"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1038143616517"><a name="p1038143616517"></a><a name="p1038143616517"></a>* Image Version</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1338110368519"><a name="p1338110368519"></a><a name="p1338110368519"></a>Version of the image to be deployed.</p>
        </td>
        </tr>
        <tr id="row32839494813"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p122831140486"><a name="p122831140486"></a><a name="p122831140486"></a>* Container Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p528314415486"><a name="p528314415486"></a><a name="p528314415486"></a>Name of the container. You can modify it.</p>
        </td>
        </tr>
        <tr id="row1449911299503"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p53374336504"><a name="p53374336504"></a><a name="p53374336504"></a>Privileged Container</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p49887211526"><a name="p49887211526"></a><a name="p49887211526"></a>Programs in a privileged container have certain privileges.</p>
        <p id="p65001729105011"><a name="p65001729105011"></a><a name="p65001729105011"></a>If <strong id="b13252222105114"><a name="b13252222105114"></a><a name="b13252222105114"></a>Privileged Container</strong> is <strong id="b11849182725112"><a name="b11849182725112"></a><a name="b11849182725112"></a>On</strong>, the container is granted superuser permissions. For example, privileged containers can manipulate network devices on the host machine and modify kernel parameters.</p>
        </td>
        </tr>
        <tr id="row152831345485"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p875325925918"><a name="p875325925918"></a><a name="p875325925918"></a>Container Resources</p>
        </td>
        <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p5379182494610"><a name="p5379182494610"></a><a name="p5379182494610"></a>CPU quotas:</p>
        <a name="ul67283495467"></a><a name="ul67283495467"></a><ul id="ul67283495467"><li><strong id="b837912315811"><a name="b837912315811"></a><a name="b837912315811"></a>Request</strong>: the minimum number of CPU cores required by a container. The default value is 0.25 core.</li><li><strong id="b1728781088"><a name="b1728781088"></a><a name="b1728781088"></a>Limit</strong>: the maximum number of CPU cores available for a container. Do not leave <strong id="b71778281894"><a name="b71778281894"></a><a name="b71778281894"></a>Limit</strong> unspecified. Otherwise, intensive use of container resources will occur and your workload may exhibit unexpected behavior.</li></ul>
        <p id="p633394210502"><a name="p633394210502"></a><a name="p633394210502"></a>Memory quotas:</p>
        <a name="ul14326165915010"></a><a name="ul14326165915010"></a><ul id="ul14326165915010"><li><strong id="b2325104041116"><a name="b2325104041116"></a><a name="b2325104041116"></a>Request</strong>: the minimum amount of memory required by a container. The default value is 512 MiB.</li><li><strong id="b4467144318115"><a name="b4467144318115"></a><a name="b4467144318115"></a>Limit</strong>: the maximum amount of memory available for a container. When memory usage exceeds the specified memory limit, the container will be terminated.</li></ul>
        <p id="p1825119142351"><a name="p1825119142351"></a><a name="p1825119142351"></a>For more information about <strong id="b1672210449245"><a name="b1672210449245"></a><a name="b1672210449245"></a>Request</strong> and <strong id="b5722194432420"><a name="b5722194432420"></a><a name="b5722194432420"></a>Limit</strong>, see <a href="setting-container-specifications.md">Setting Container Specifications</a>.</p>
        <div class="p" id="p1684921311567"><a name="p1684921311567"></a><a name="p1684921311567"></a>GPU quotas: configurable only when the cluster contains GPU nodes.<a name="ul1634514911568"></a><a name="ul1634514911568"></a><ul id="ul1634514911568"><li><strong id="b42101842349"><a name="b42101842349"></a><a name="b42101842349"></a>GPU</strong>: the percentage of GPU resources reserved for a container. Select <span class="uicontrol" id="uicontrol19942102410563"><a name="uicontrol19942102410563"></a><a name="uicontrol19942102410563"></a><b>Use</b></span> and set the percentage. For example, if this parameter is set to 10%, the container is allowed to use 10% of GPU resources. If you do not select <span class="uicontrol" id="uicontrol13191233125719"><a name="uicontrol13191233125719"></a><a name="uicontrol13191233125719"></a><b>Use</b></span> or set this parameter to 0, no GPU resources can be used.</li><li><strong id="b20489865364"><a name="b20489865364"></a><a name="b20489865364"></a>GPU/Graphics Card</strong>: The workload's pods will be scheduled to the node with the specified GPU. If <strong id="b376171219323"><a name="b376171219323"></a><a name="b376171219323"></a>Any GPU type</strong> is selected, the container uses a random GPU in the node. If you select a specific GPU, the container uses this GPU.</li></ul>
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

    6.  Mount data storage to containers for persistent storage and high disk I/O. For details, see  [Storage Management](storage-management.md).
    7.  Configure container permissions to protect CCE and other containers from being affected.

        Enter the user ID to set container permissions and prevent systems and other containers from being affected.

    8.  Configure the log collection policies and log directory to collect container logs for unified management and analysis. For details, see  [Collecting Standard Output Logs of Containers](collecting-standard-output-logs-of-containers.md)  and  [Collecting Container Logs from Specified Paths](collecting-container-logs-from-specified-paths.md).
    9.  \(Optional\) A pod contains one or more closely related containers. If your workload is a multi-container workload, click  **Add Container**  to add more containers.

4.  Click  **Next: Set Application Access**. Then, click  **Add Service**  and set the workload access type.

    If your workload will be reachable to other workloads or public networks, add a service to define the workload access type.

    The workload access type determines the network attributes of the workload. Workloads with different access types can provide different network capabilities. For details, see  [Network Overview](network-overview.md).

5.  Click  **Next: Configure Advanced Settings**  and configure advanced settings.
    -   **Upgrade Policy**
        -   **Rolling upgrade**: Gradually replaces an old pod with a new pod. During the upgrade, service traffic is evenly distributed to the old and new pods to ensure service continuity.

            **Maximum Number of Unavailable Pods**: Maximum number of unavailable pods allowed in a rolling upgrade. If the number is equal to the total number of pods, services may be interrupted. Minimum number of alive pods = Total pods – Maximum number of unavailable pods

        -   **In-place upgrade**: Deletes an old pod and then creates a new one. Services are interrupted during the upgrade.

    -   **Graceful Deletion**:
        -   **Graceful Time Window \(s\)**: Set a time window \(0–9999s\) for pre-stop commands to finish execution before a workload is deleted. The default value is 30s.
        -   **Scale Order**: Choose  **Prioritize new pods**  or  **Prioritize old pods**  based on service requirements.

    -   **Migration Policy**: Set the time window. When the node where workload's pods are located is unavailable for the specified amount of time, the pods will be rescheduled to other available nodes. By default, the time window is 300s.
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

    Workload status is not updated in real time. Click  ![](figures/icon-upgrade.png)  in the upper right corner or press  **F5**  to refresh the page.

7.  To access the workload in a browser, go to the workload list on the  **Workload**  page. Copy the corresponding  **External Access Address**  and paste it into the address box in the browser.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   External access addresses are available only if the deployment access type is set to  **Node access \(node port\)**  and an EIP is assigned to any node in the cluster, or if the deployment access type is set to  **Load balancing \(load balancer\)**.
    >-   If the workload list contains more than 500 records, the Kubernetes pagination mechanism will be used. Specifically, you can only go to the first page or the next page, but cannot go to the previous page. In addition, if resources are divided into discrete pages, the total number of resources displayed is the maximum number of resources that can be queried at a time, not the actual total number of resources.


## Using kubectl<a name="section155246177178"></a>

The following procedure uses Nginx as an example to describe how to  create a workload using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

1.  Log in to the ECS on which kubectl has been configured. For details, see  [Logging In to a Linux ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0013771089.html).
2.  Create and edit the  **nginx-deployment.yaml**  file.  **nginx-deployment.yaml**  is an example file name, and you can change it as required.

    **vi nginx-deployment.yaml**

    The following is an example YAML file. For more information about Deployments, see  [Kubernetes documentation](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

    ```
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: nginx
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx
      strategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - image: nginx 
            imagePullPolicy: Always
            name: nginx
          imagePullSecrets:
          - name: default-secret
    ```

    For details about deployment.yaml parameters, see  [Table 3](#table132326831016).

    **Table  3**  Deployment.yaml parameters

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
    <div class="note" id="note143305521379"><a name="note143305521379"></a><a name="note143305521379"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p19331452133715"><a name="p19331452133715"></a><a name="p19331452133715"></a>For clusters earlier than 1.9, the apiVersion format of Deployments is extensions/v1beta1. For clusters later than 1.9, the apiVersion format can be extensions/v1beta1 or apps/v1. Set this parameter based on the cluster version.</p>
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
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p1036510541116"><a name="p1036510541116"></a><a name="p1036510541116"></a>Name of a deployment.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p1936585415110"><a name="p1936585415110"></a><a name="p1936585415110"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row52341382109"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p2234188171017"><a name="p2234188171017"></a><a name="p2234188171017"></a>Spec</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p1023414811012"><a name="p1023414811012"></a><a name="p1023414811012"></a>Detailed description of the deployment.</p>
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
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p10938171341312"><a name="p10938171341312"></a><a name="p10938171341312"></a>Container instance that can be managed by the deployment.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p5939181320135"><a name="p5939181320135"></a><a name="p5939181320135"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row393931310133"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p8731714131517"><a name="p8731714131517"></a><a name="p8731714131517"></a>strategy</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p24327545152918"><a name="p24327545152918"></a><a name="p24327545152918"></a>Upgrade mode. Possible values:</p>
    <a name="ul2391401152910"></a><a name="ul2391401152910"></a><ul id="ul2391401152910"><li>RollingUpdate</li><li>ReplaceUpdate</li></ul>
    <p id="p43301055163212"><a name="p43301055163212"></a><a name="p43301055163212"></a>By default, rolling update is used.</p>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p169393137138"><a name="p169393137138"></a><a name="p169393137138"></a>Optional</p>
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
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><a name="ul48282256265"></a><a name="ul48282256265"></a><ul id="ul48282256265"><li><strong id="b021334265015"><a name="b021334265015"></a><a name="b021334265015"></a>image</strong> (mandatory): Name of a container image.</li><li><strong id="b132081541916"><a name="b132081541916"></a><a name="b132081541916"></a>imagePullPolicy</strong> (optional): Policy for obtaining an image. The options include <strong id="b47004369113256"><a name="b47004369113256"></a><a name="b47004369113256"></a>Always</strong> (attempting to download images each time), <strong id="b1385119962113256"><a name="b1385119962113256"></a><a name="b1385119962113256"></a>Never</strong> (only using local images), and <strong id="b1264351417113256"><a name="b1264351417113256"></a><a name="b1264351417113256"></a>IfNotPresent</strong> (using local images if they are available; downloading images if local images are unavailable). The default value is <strong id="b184934519113256"><a name="b184934519113256"></a><a name="b184934519113256"></a>Always</strong>.</li><li><strong id="b10210122381914"><a name="b10210122381914"></a><a name="b10210122381914"></a>name</strong> (mandatory): Container name.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p1193991381318"><a name="p1193991381318"></a><a name="p1193991381318"></a>Mandatory</p>
    </td>
    </tr>
    <tr id="row18939013161315"><td class="cellrowborder" valign="top" width="37%" headers="mcps1.2.4.1.1 "><p id="p159394135139"><a name="p159394135139"></a><a name="p159394135139"></a>imagePullSecrets</p>
    </td>
    <td class="cellrowborder" valign="top" width="47%" headers="mcps1.2.4.1.2 "><p id="p49391813131318"><a name="p49391813131318"></a><a name="p49391813131318"></a>Name of the secret used during image pulling. If a private image is used, this parameter is mandatory.</p>
    <a name="ul125550172614"></a><a name="ul125550172614"></a><ul id="ul125550172614"><li>To pull an image from the Software Repository for Container (SWR), set this parameter to default-secret.</li><li>To pull an image from a third-party image repository, set this parameter to the name of the created secret.</li></ul>
    </td>
    <td class="cellrowborder" valign="top" width="16%" headers="mcps1.2.4.1.3 "><p id="p1193981391318"><a name="p1193981391318"></a><a name="p1193981391318"></a>Optional</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Create a Deployment.

    **kubectl create -f nginx-deployment.yaml**

    If the following information is displayed, the Deployment is being created.

    ```
    deployment "nginx" created
    ```

4.  Query the Deployment status.

    **kubectl get po**

    If the following information is displayed, the Deployment is running.

    ```
    NAME                     READY     STATUS    RESTARTS   AGE
    icagent-m9dkt            0/0       Running   0          3d
    nginx-1212400781-qv313   1/1       Running   0          3d
    ```

5.  If the Deployment will be accessed through a ClusterIP or NodePort service, add the corresponding service. For details, see  [Network Management](network-management.md).

