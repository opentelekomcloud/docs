# Using Local Disks for Storage<a name="cce_01_0053"></a>

Use the  local disk storage  to mount the file directory of the host where the container is located to the specified path of the container, or leave the source path empty.

## Scenario<a name="section12724113154514"></a>

Local hard disks are applicable to the following scenarios:

-   Host path mounting: Mount the file directory of the host where the container is located to the specified mounting point of the container. If the container needs to access  **/etc/hosts**, use  **HostPath**  to map  **/etc/hosts**.
-   Temporary path mounting: Used for temporary storage. The lifecycle is the same as that of the container instance. When a container instance disappears,  **EmptyDir**  will be deleted and the data is permanently lost.
-   ConfigMap mounting: Keys in the configuration items of  ConfigMap  are mapped to a container so that configuration files can be mounted to the specified container directory. For details about how to create a ConfigMap, see  [Creating a ConfigMap](creating-a-configmap.md). For details about how to use a ConfigMap, see  [Using a ConfigMap](using-a-configmap.md).
-   Secret mounting: Data in the keys is mounted to a path of the container. A secret is a type of resource that holds sensitive data, such as authentication and key information. All content is user-defined. For details about how to create a  secret, see  [Creating a Secret](creating-a-secret.md). For details about how to use a  secret, see  [Using a Secret](using-a-secret.md).

## Host Path<a name="section196700523438"></a>

In this scenario, the files or directories on the host machine are mounted to a  container. Such a volume is usually used to store containerized workload logs that need to be stored permanently or containerized workloads that need to access internal data structure of the  Docker  engine on the host.

1.  Create a workload by referring to  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md). After you add a container, expand  **Data Storage**, and click  **Add Local Disk**.
2.  Set parameters for adding a local disk, as listed in  [Table 1](#table14312815449).

    **Table  1**  Setting the volume type to host path mounting

    <a name="table14312815449"></a>
    <table><thead align="left"><tr id="row1430108144414"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p3304815443"><a name="p3304815443"></a><a name="p3304815443"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p63012813442"><a name="p63012813442"></a><a name="p63012813442"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row931118184415"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p7315824414"><a name="p7315824414"></a><a name="p7315824414"></a>Volume Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p193112817449"><a name="p193112817449"></a><a name="p193112817449"></a>HostPath.</p>
    </td>
    </tr>
    <tr id="row203214811443"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p5314818448"><a name="p5314818448"></a><a name="p5314818448"></a>Host Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p133114874418"><a name="p133114874418"></a><a name="p133114874418"></a>Path of the host to which the local disk is to be mounted, for example, <strong id="b1936602094412"><a name="b1936602094412"></a><a name="b1936602094412"></a>/etc/hosts</strong>.</p>
    </td>
    </tr>
    <tr id="row53620864414"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p153212810443"><a name="p153212810443"></a><a name="p153212810443"></a>Add Container Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><a name="ol1535285447"></a><a name="ol1535285447"></a><ol id="ol1535285447"><li>Click <span class="uicontrol" id="uicontrol962276955105213"><a name="uicontrol962276955105213"></a><a name="uicontrol962276955105213"></a><b>Add Container Path</b></span>.</li><li>Enter the container path to which the data volume is mounted.<div class="notice" id="note235158114415"><a name="note235158114415"></a><a name="note235158114415"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul12344814413"></a><a name="ul12344814413"></a><ul id="ul12344814413"><li>The container path cannot be a system directory, such as <strong id="b8930115520267"><a name="b8930115520267"></a><a name="b8930115520267"></a>/</strong> or /<strong id="b1739622817252"><a name="b1739622817252"></a><a name="b1739622817252"></a>var/run</strong>. Otherwise, the container may not function properly. You are advised to mount the container to an empty directory. If the directory is not empty, ensure that there are no files affecting container startup in the directory. Otherwise, such files will be replaced, resulting in failures to start the container and create the workload.</li><li>When the container is mounted to a high-risk directory, you are advised to use an account with minimum permissions to start the container; otherwise, high-risk files on the host machine may be damaged.</li></ul>
    </div></div>
    </li><li>Set permissions.<a name="ul3352818447"></a><a name="ul3352818447"></a><ul id="ul3352818447"><li><strong id="b75061752152618"><a name="b75061752152618"></a><a name="b75061752152618"></a>Read-only</strong>: You can only read the data volumes in the path.</li><li><strong id="b1534191362715"><a name="b1534191362715"></a><a name="b1534191362715"></a>Read/Write</strong>: You can modify the data volumes in the path. Newly written data is not migrated if the container is migrated, which may cause a data loss.</li></ul>
    </li><li>Click <strong id="b143281381402"><a name="b143281381402"></a><a name="b143281381402"></a>OK</strong>.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>


## EmptyDir<a name="section550555216467"></a>

EmptyDir applies to temporary data storage, disaster recovery, and shared running. It will be deleted upon deletion or transfer of workload instances.

1.  Create a workload by referring to  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md). After you add a container, expand  **Data Storage**, and click  **Add Local Disk**.
2.  Set the local disk type to temporary path mounting and set parameters for adding a local disk, as shown in  [Table 2](#table1867417102475).

    **Table  2**  Setting the volume type to temporary path mounting

    <a name="table1867417102475"></a>
    <table><thead align="left"><tr id="row116705107477"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.3.1.1"><p id="p367021084716"><a name="p367021084716"></a><a name="p367021084716"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="76%" id="mcps1.2.3.1.2"><p id="p1367017107472"><a name="p1367017107472"></a><a name="p1367017107472"></a><strong id="b9535112094414"><a name="b9535112094414"></a><a name="b9535112094414"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row867231016476"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p15672210204710"><a name="p15672210204710"></a><a name="p15672210204710"></a>Volume Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p1267271094716"><a name="p1267271094716"></a><a name="p1267271094716"></a>Temporary path (EmptyDir).</p>
    </td>
    </tr>
    <tr id="row8672181011474"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p967231014479"><a name="p967231014479"></a><a name="p967231014479"></a>Storage Media Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><a name="ul2672201015476"></a><a name="ul2672201015476"></a><ul id="ul2672201015476"><li>If you select <strong id="b84235270614480"><a name="b84235270614480"></a><a name="b84235270614480"></a>In-memory</strong> <strong id="b084920592428"><a name="b084920592428"></a><a name="b084920592428"></a>storage</strong>, the running speed is improved, but the storage capacity is limited by the memory size. This mode applies to scenarios where the data volume is small and the read and write efficiency is high.</li><li>If <strong id="b22791941418"><a name="b22791941418"></a><a name="b22791941418"></a>In-memory</strong> <strong id="b127914420411"><a name="b127914420411"></a><a name="b127914420411"></a>storage</strong> is deselected, data is stored in disks, which is applicable to a large amount of data with low requirements on reading and writing efficiency.</li></ul>
    </td>
    </tr>
    <tr id="row10674101084717"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p96728108473"><a name="p96728108473"></a><a name="p96728108473"></a>Add Container Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><a name="ol186742104479"></a><a name="ol186742104479"></a><ol id="ol186742104479"><li>Click <span class="uicontrol" id="uicontrol283550550"><a name="uicontrol283550550"></a><a name="uicontrol283550550"></a><b>Add Container Path</b></span>.</li><li>Enter the container path to which the data volume is mounted.<div class="notice" id="note767281014713"><a name="note767281014713"></a><a name="note767281014713"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul12672010114719"></a><a name="ul12672010114719"></a><ul id="ul12672010114719"><li>The container path cannot be a system directory, such as <strong id="b110136275"><a name="b110136275"></a><a name="b110136275"></a>/</strong> or /<strong id="b2084791252"><a name="b2084791252"></a><a name="b2084791252"></a>var/run</strong>. Otherwise, the container may not function properly. You are advised to mount the container to an empty directory. If the directory is not empty, ensure that there are no files affecting container startup in the directory. Otherwise, such files will be replaced, resulting in failures to start the container and create the workload.</li><li>When the container is mounted to a high-risk directory, you are advised to use an account with minimum permissions to start the container; otherwise, high-risk files on the host machine may be damaged.</li></ul>
    </div></div>
    </li><li>Set permissions.<a name="ul2673810164716"></a><a name="ul2673810164716"></a><ul id="ul2673810164716"><li><strong id="b1595618187"><a name="b1595618187"></a><a name="b1595618187"></a>Read-only</strong>: You can only read the data volumes in the path.</li><li><strong id="b1543536318"><a name="b1543536318"></a><a name="b1543536318"></a>Read/Write</strong>: You can modify the data volumes in the path. Newly written data is not migrated if the container is migrated, which may cause a data loss.</li></ul>
    </li><li>Click <strong id="b1803214168"><a name="b1803214168"></a><a name="b1803214168"></a>OK</strong>.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>


## ConfigMap<a name="section18638191594712"></a>

The platform provides the separation of workload codes and configuration files. ConfigMap mounting is used to process workload configuration parameters. You need to create workload configurations in advance. For more information, see  [Creating a ConfigMap](creating-a-configmap.md).

1.  Create a workload by referring to  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md). After you add a container, expand  **Data Storage**, and click  **Add Local Disk**.
2.  Set the local disk type to ConfigMap mounting and set parameters for adding a local disk, as shown in  [Table 3](#table1776324831114).

    **Table  3**  Setting the volume type to ConfigMap mounting

    <a name="table1776324831114"></a>
    <table><thead align="left"><tr id="row177484871120"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.3.1.1"><p id="p977974818111"><a name="p977974818111"></a><a name="p977974818111"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="76%" id="mcps1.2.3.1.2"><p id="p978113488113"><a name="p978113488113"></a><a name="p978113488113"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20785144820118"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p197881548171117"><a name="p197881548171117"></a><a name="p197881548171117"></a>Volume Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p479110483117"><a name="p479110483117"></a><a name="p479110483117"></a>ConfigMap.</p>
    </td>
    </tr>
    <tr id="row342915156166"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p17429315151617"><a name="p17429315151617"></a><a name="p17429315151617"></a>ConfigMap</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><div class="p" id="p3133142513414"><a name="p3133142513414"></a><a name="p3133142513414"></a>Select the desired ConfigMap name.<div class="note" id="note15907929472"><a name="note15907929472"></a><a name="note15907929472"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p11907229678"><a name="p11907229678"></a><a name="p11907229678"></a>A ConfigMap must be created in advance. For details, see <a href="creating-a-configmap.md">Creating a ConfigMap</a>.</p>
    </div></div>
    </div>
    </td>
    </tr>
    <tr id="row28091948181115"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p9813048191118"><a name="p9813048191118"></a><a name="p9813048191118"></a>Add Container Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><a name="ol18607172216391"></a><a name="ol18607172216391"></a><ol id="ol18607172216391"><li>Click <span class="uicontrol" id="uicontrol1561422293919"><a name="uicontrol1561422293919"></a><a name="uicontrol1561422293919"></a><b>Add Container Path</b></span>.</li><li>Enter the container path to which the data volume is mounted.<div class="notice" id="note36191022193911"><a name="note36191022193911"></a><a name="note36191022193911"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul3921344985"></a><a name="ul3921344985"></a><ul id="ul3921344985"><li>Do not mount a data volume to a system directory such as <strong id="b1336093528144242"><a name="b1336093528144242"></a><a name="b1336093528144242"></a>/</strong> or <strong id="b903433524144242"><a name="b903433524144242"></a><a name="b903433524144242"></a>/var/run</strong>; otherwise, the container becomes abnormal. You are advised to mount the container to an empty directory. If the directory is not empty, ensure that there are no files affecting container startup in the directory. Otherwise, such files will be replaced, resulting in failures to start the container and create the workload.</li><li>When the data volume is mounted to a high-risk directory, you are advised to use an account with minimum permissions to start the container; otherwise, high-risk files on the host machine may be damaged.</li></ul>
    </div></div>
    </li><li>Set the permission to <strong id="b617845293615"><a name="b617845293615"></a><a name="b617845293615"></a>Read-only</strong>. Data volumes in the path are read-only.</li><li>Click <span class="uicontrol" id="uicontrol76431122133918"><a name="uicontrol76431122133918"></a><a name="uicontrol76431122133918"></a><b>OK</b></span>.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>


## Secret<a name="section10197243134710"></a>

Mount the data in the key to the specified container. The content of the key is user-defined. You need to create application configurations in advance. For more information, see  [Creating a Secret](creating-a-secret.md).

1.  Create a workload by referring to  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md). After you add a container, expand  **Data Storage**, and click  **Add** **Local** **Disk**.
2.  Set the local disk type to secret mounting and set parameters for adding a local disk, as shown in  [Table 4](#table861818920109).

    **Table  4**  Setting the volume type to secret mounting

    <a name="table861818920109"></a>
    <table><thead align="left"><tr id="row1962619171020"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.3.1.1"><p id="p196285991018"><a name="p196285991018"></a><a name="p196285991018"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="76%" id="mcps1.2.3.1.2"><p id="p126314951020"><a name="p126314951020"></a><a name="p126314951020"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row20632792101"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p56341798108"><a name="p56341798108"></a><a name="p56341798108"></a>Volume Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p206363911018"><a name="p206363911018"></a><a name="p206363911018"></a>Secret.</p>
    </td>
    </tr>
    <tr id="row563713981015"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p16638594102"><a name="p16638594102"></a><a name="p16638594102"></a>Secret</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><div class="p" id="p790921317488"><a name="p790921317488"></a><a name="p790921317488"></a>Select the desired secret name.<div class="note" id="note293611291713"><a name="note293611291713"></a><a name="note293611291713"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p09361129375"><a name="p09361129375"></a><a name="p09361129375"></a>A secret must be created in advance. For details, see <a href="creating-a-secret.md">Creating a Secret</a>.</p>
    </div></div>
    </div>
    </td>
    </tr>
    <tr id="row146458911015"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p46473921020"><a name="p46473921020"></a><a name="p46473921020"></a>Add Container Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><a name="ol1365012913103"></a><a name="ol1365012913103"></a><ol id="ol1365012913103"><li>Click <span class="uicontrol" id="uicontrol1045062984"><a name="uicontrol1045062984"></a><a name="uicontrol1045062984"></a><b>Add Container Path</b></span>.</li><li>Enter the container path to which the data volume is mounted.<div class="notice" id="note86567931015"><a name="note86567931015"></a><a name="note86567931015"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul116574911106"></a><a name="ul116574911106"></a><ul id="ul116574911106"><li>Do not mount a data volume to a system directory such as <strong id="b50506472010547"><a name="b50506472010547"></a><a name="b50506472010547"></a>/</strong> or <strong id="b96350457710547"><a name="b96350457710547"></a><a name="b96350457710547"></a>/var/run</strong>; otherwise, the container becomes abnormal. You are advised to mount the container to an empty directory. If the directory is not empty, ensure that there are no files affecting container startup in the directory. Otherwise, such files will be replaced, resulting in failures to start the container and create the workload.</li><li>When the data volume is mounted to a high-risk directory, you are advised to use an account with minimum permissions to start the container; otherwise, high-risk files on the host machine may be damaged.</li></ul>
    </div></div>
    </li><li>Set the permission to <strong id="b101758409373"><a name="b101758409373"></a><a name="b101758409373"></a>Read-only</strong>. Data volumes in the path are read-only.</li><li>Click <span class="uicontrol" id="uicontrol1920679261"><a name="uicontrol1920679261"></a><a name="uicontrol1920679261"></a><b>OK</b></span>.</li></ol>
    </td>
    </tr>
    </tbody>
    </table>


## Mounting a Host Path Using kubectl<a name="section2432104516110"></a>

You can mount a file directory of the host where the container is located to a specified mount path of the container using kubectl.

1.  Configure kubectl. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).
2.  Run the following commands to configure the  **hostPath-pod-example.yaml**  file, which is used to create a pod.

    **touch hostPath-pod-example.yaml**

    **vi hostPath-pod-example.yaml**

    Mount the host path for the Deployment. The following is an example:

    ```
    apiVersion: extensions/v1beta1 
    kind: Deployment 
    metadata: 
      name: hostpath-pod-example 
      namespace: default 
    spec: 
      replicas: 1 
      selector: 
        matchLabels: 
          app: hostpath-pod-example 
      template: 
        metadata: 
          labels: 
            app: hostpath-pod-example 
        spec: 
          containers: 
          - image: nginx
            name: container-0 
            volumeMounts: 
            - mountPath: /tmp 
              name: hostpath-example 
          restartPolicy: Always 
          volumes: 
          - name: hostpath-example 
            hostPath: 
              path: /tmp
    ```

    In this example:

    -   **name**: name of the pod to be created.
    -   **app**: name of the pod workload.
    -   **mountPath**: mount path of the container. In this example, the host path is mounted to the  **/tmp**  directory.
    -   **hostPath**: host path. In this example, the host path is  **/tmp**.
    -   **spec.template.spec.containers.volumeMounts.name**  and  **spec.template.spec.volumes.name**  must be consistent because they have a mapping relationship.

3.  Run the following command to create a pod:

    **kubectl create -f hostPath-pod-example.yaml**


