# Using SFS File Systems for Storage<a name="cce_01_0111"></a>

File storage  is applicable to various scenarios, such as  media processing,  content management,  big data, and workload analysis.

**Figure  1**  Mounting SFS file systems to CCE<a name="fig1743195012373"></a>  
![](figures/mounting-sfs-file-systems-to-cce.png "mounting-sfs-file-systems-to-cce")

## Description<a name="section313719276380"></a>

-   Complying with standard file protocols, file systems can be mounted to servers, the same as using local directories.
-   Data sharing: The same file system can be mounted to multiple servers, so that access to data can be shared.
-   Private network: Data access must be performed in the internal network of the data center.
-   The capacity of a single file system is high \(at PB level\) and the performance is excellent \(at ms level\), suitable to media editing, HPC, and file sharing scenarios.
-   Applicable to Deployments, StatefulSets, and jobs in the ReadWriteMany scenarios.

## Constraints<a name="section5807185714121"></a>

Container storage in CCE clusters of Kubernetes 1.13 or later version supports encryption. Currently, E2E encryption is supported only in certain regions.

## Creating an SFS File System<a name="section1123416794811"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Storage**.
2.  On the  **SFS**  tab, click  **Create SFS File System**.
3.  Configure basic information, as listed in  [Table 1](#table20328123218464).

    **Table  1**  Basic SFS file system information

    <a name="table20328123218464"></a>
    <table><thead align="left"><tr id="row533073264618"><th class="cellrowborder" valign="top" width="25.990000000000002%" id="mcps1.2.3.1.1"><p id="p12330932164617"><a name="p12330932164617"></a><a name="p12330932164617"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="74.00999999999999%" id="mcps1.2.3.1.2"><p id="p133306326467"><a name="p133306326467"></a><a name="p133306326467"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row0330113224615"><td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p18330232154618"><a name="p18330232154618"></a><a name="p18330232154618"></a>* PVC Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p376419205498"><a name="p376419205498"></a><a name="p376419205498"></a>Name of the new PVC, which is different from the volume name. The actual volume name is automatically generated when the PVC is created.</p>
    </td>
    </tr>
    <tr id="row20242958195514"><td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p1243195835517"><a name="p1243195835517"></a><a name="p1243195835517"></a>Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p4243258145517"><a name="p4243258145517"></a><a name="p4243258145517"></a>Cluster where the SFS file system is deployed.</p>
    </td>
    </tr>
    <tr id="row632053011411"><td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p1332113301649"><a name="p1332113301649"></a><a name="p1332113301649"></a>Namespace</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p13321133018413"><a name="p13321133018413"></a><a name="p13321133018413"></a>Namespace where the SFS file system is located.</p>
    </td>
    </tr>
    <tr id="row17020817474"><td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p421381478"><a name="p421381478"></a><a name="p421381478"></a>Total Capacity</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p4766420114910"><a name="p4766420114910"></a><a name="p4766420114910"></a>Capacity of a single volume. The usage fee is charged based on the actual capacity.</p>
    </td>
    </tr>
    <tr id="row722105713116"><td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p72315741119"><a name="p72315741119"></a><a name="p72315741119"></a>Access Mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p15247573114"><a name="p15247573114"></a><a name="p15247573114"></a>Access mode. If this parameter is set to <strong id="b15232185219482"><a name="b15232185219482"></a><a name="b15232185219482"></a>ReadWriteMany</strong>, the volume can be mounted as read-write by multiple nodes.</p>
    </td>
    </tr>
    <tr id="row272414094414"><td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p187251040134420"><a name="p187251040134420"></a><a name="p187251040134420"></a>Storage Format</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.00999999999999%" headers="mcps1.2.3.1.2 "><p id="p94275532262"><a name="p94275532262"></a><a name="p94275532262"></a>Storage format of the file system. The default value is <strong id="b1842718538265"><a name="b1842718538265"></a><a name="b1842718538265"></a>CSI</strong>.</p>
    <p id="p10427135315261"><a name="p10427135315261"></a><a name="p10427135315261"></a>The Container Storage Interface (CSI) was developed as a standard for exposing external storage systems to containerized workloads on container orchestration systems such as Kubernetes.</p>
    <p id="p1437382413459"><a name="p1437382413459"></a><a name="p1437382413459"></a>This parameter is displayed only for clusters of v1.15.6-r1 and later.</p>
    </td>
    </tr>
    <tr id="row136563921516"><td class="cellrowborder" valign="top" width="25.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p136915265434"><a name="p136915265434"></a><a name="p136915265434"></a>Encryption</p>
    </td>
    <td class="cellrowborder" valign="top" width="74.00999999999999%" headers="mcps1.2.3.1.2 "><div class="p" id="p1984920438435"><a name="p1984920438435"></a><a name="p1984920438435"></a><span class="uicontrol" id="uicontrol1951612227355"><a name="uicontrol1951612227355"></a><a name="uicontrol1951612227355"></a><b>KMS Encryption</b></span> is deselected by default. If <span class="uicontrol" id="uicontrol168318320369"><a name="uicontrol168318320369"></a><a name="uicontrol168318320369"></a><b>KMS Encryption</b></span> is selected, set the following parameters:<a name="ul32358634612"></a><a name="ul32358634612"></a><ul id="ul32358634612"><li><strong id="b197291123125918"><a name="b197291123125918"></a><a name="b197291123125918"></a>Agency Name</strong>: Agencies can be used to assign permissions to trusted accounts or cloud services for a specific period of time. If no agency is created, click <span class="uicontrol" id="uicontrol1314249548"><a name="uicontrol1314249548"></a><a name="uicontrol1314249548"></a><b>Create Agency</b></span>. The agency name <strong id="b1489813231518"><a name="b1489813231518"></a><a name="b1489813231518"></a>SFSAccessKMS</strong> indicates that SFS is granted the permission to access KMS. After SFS is authorized successfully, it can obtain KMS keys to encrypt and decrypt SFS systems.</li><li><strong id="b35963176410"><a name="b35963176410"></a><a name="b35963176410"></a>Key Name</strong>: A secret is a type of resource that holds sensitive data, such as authentication and key information. All content in secrets is user-defined. Secrets can be loaded into containerized applications. For details on how to create a secret, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0014250631.html" target="_blank" rel="noopener noreferrer">Creating a Key Pair</a>.</li><li><strong id="b95534651410"><a name="b95534651410"></a><a name="b95534651410"></a>Key ID</strong>: generated by default.</li></ul>
    </div>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Create**, and wait until the creation is successful.

    The file system is displayed in the list. When its status becomes  **Normal**, the file system is created successfully.

5.  Click the PVC name to view detailed information about the SFS file system.

## Using an SFS File System<a name="section836684712447"></a>

1.  Create a workload by referring to  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md). After you add a container, expand  **Data Storage**. On the  **Cloud Volume**  tab page, click  **Add Cloud Volume**.
2.  Set the storage type to  **SFS**.

    **Table  2**  Parameters for mounting an SFS file system

    <a name="table6514150195315"></a>
    <table><thead align="left"><tr id="row1250916010532"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.3.1.1"><p id="p1550914012531"><a name="p1550914012531"></a><a name="p1550914012531"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="79%" id="mcps1.2.3.1.2"><p id="p850913012539"><a name="p850913012539"></a><a name="p850913012539"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15510806536"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p851018010531"><a name="p851018010531"></a><a name="p851018010531"></a>Type</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p2874185810616"><a name="p2874185810616"></a><a name="p2874185810616"></a>SFS: This storage type applies to a wide range of scenarios, including media processing, content management, big data, and application analysis.</p>
    </td>
    </tr>
    <tr id="row1851090115317"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p1251017085312"><a name="p1251017085312"></a><a name="p1251017085312"></a>Allocation Mode</p>
    </td>
    </tr>
    <tr id="row145119035310"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p8510130125311"><a name="p8510130125311"></a><a name="p8510130125311"></a>Manual</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p1351014055320"><a name="p1351014055320"></a><a name="p1351014055320"></a><strong id="b1191431115516"><a name="b1191431115516"></a><a name="b1191431115516"></a>Name</strong>: Select a created storage device. You need to create a storage device in advance. For details about how to create a storage device, see <a href="#section1123416794811">Creating an SFS File System</a>.</p>
    </td>
    </tr>
    <tr id="row105123014531"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p155113095317"><a name="p155113095317"></a><a name="p155113095317"></a>Automatic</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p195111307532"><a name="p195111307532"></a><a name="p195111307532"></a>An SFS file system is created automatically. You need to enter the storage capacity.</p>
    <a name="ol10512509534"></a><a name="ol10512509534"></a><ol id="ol10512509534"><li>Select the SFS file system subtype.<p id="p1651115095319"><a name="p1651115095319"></a><a name="p1651115095319"></a>The SFS file system subtype is <strong id="b1872452155143044"><a name="b1872452155143044"></a><a name="b1872452155143044"></a>NFS</strong>.</p>
    </li><li>Enter the storage capacity in the unit of GB. Ensure that the storage capacity quota is not exceeded; otherwise, creation will fail.</li><li>Storage format of the file system. The default value is <strong id="b172081743131914"><a name="b172081743131914"></a><a name="b172081743131914"></a>CSI</strong>.<p id="p152084431199"><a name="p152084431199"></a><a name="p152084431199"></a>The Container Storage Interface (CSI) was developed as a standard for exposing external storage systems to containerized workloads on container orchestration systems such as Kubernetes.</p>
    <p id="p1793271842110"><a name="p1793271842110"></a><a name="p1793271842110"></a>This parameter is displayed only for clusters of v1.15.6-r1 and later.</p>
    </li><li>Set the encryption mode. Select <span class="uicontrol" id="uicontrol1299064913571"><a name="uicontrol1299064913571"></a><a name="uicontrol1299064913571"></a><b>KMS Encryption</b></span> and set the following parameters:<a name="ul1738911481971"></a><a name="ul1738911481971"></a><ul id="ul1738911481971"><li><strong id="b848418599329"><a name="b848418599329"></a><a name="b848418599329"></a>Agency Name</strong>: Agencies can be used to assign permissions to trusted accounts or cloud services for a specific period of time. If no agency is created, click <span class="uicontrol" id="uicontrol9485659193220"><a name="uicontrol9485659193220"></a><a name="uicontrol9485659193220"></a><b>Create Agency</b></span>. The agency name <strong id="b977164143319"><a name="b977164143319"></a><a name="b977164143319"></a>SFSAccessKMS</strong> indicates that SFS is granted the permission to access KMS. After SFS is authorized successfully, it can obtain KMS keys to encrypt and decrypt SFS systems.</li><li><strong id="b280781514330"><a name="b280781514330"></a><a name="b280781514330"></a>Key Name</strong>: A secret is a type of resource that holds sensitive data, such as authentication and key information. All content in secrets is user-defined. After resource creation is complete, you can use and load the resources in the containerized applications. For details about how to create a key, see <a href="https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0014250631.html" target="_blank" rel="noopener noreferrer">Creating a Key Pair</a>.</li><li><strong id="b1612214229"><a name="b1612214229"></a><a name="b1612214229"></a>Key ID</strong>: generated by default.</li></ul>
    </li></ol>
    </td>
    </tr>
    <tr id="row18514401530"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p451280115318"><a name="p451280115318"></a><a name="p451280115318"></a>Add Container Path</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><a name="ol14514160165311"></a><a name="ol14514160165311"></a><ol id="ol14514160165311"><li>Click <strong id="b145812410218"><a name="b145812410218"></a><a name="b145812410218"></a>Add Container Path</strong>.</li><li><strong id="b1687953018501"><a name="b1687953018501"></a><a name="b1687953018501"></a>subPath</strong>: Enter the subpath of the file storage.<div class="notice" id="note13692135014457"><a name="note13692135014457"></a><a name="note13692135014457"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><p id="p1169215507459"><a name="p1169215507459"></a><a name="p1169215507459"></a>In Kubernetes, the subpath to which the data volume is mounted refers to the subpath of the referenced volume rather than its root. The subpath must be a relative path and cannot start with a slash (/) or ../. If this parameter is not set, the root directory is used by default.</p>
    </div></div>
    </li><li><strong id="b547694414513"><a name="b547694414513"></a><a name="b547694414513"></a>Container Path</strong>: Enter the container path to which the data volume is mounted.<div class="notice" id="note1351410010535"><a name="note1351410010535"></a><a name="note1351410010535"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul1351418025318"></a><a name="ul1351418025318"></a><ul id="ul1351418025318"><li>Do not mount a data volume to a system directory such as <strong id="b79266851514485"><a name="b79266851514485"></a><a name="b79266851514485"></a>/</strong> or <strong id="b97437393214485"><a name="b97437393214485"></a><a name="b97437393214485"></a>/var/run</strong>; otherwise, the container becomes abnormal. You are advised to mount SFS volumes to an empty directory. If the directory is not empty, ensure that there are no files affecting container startup in the directory. Otherwise, such files will be replaced, resulting in failures to start the container and create the workload.</li><li>When the data volume is mounted to a high-risk directory, you are advised to use a low-permission account to start the container; otherwise, high-risk files on the host machine may be damaged.</li></ul>
    </div></div>
    </li><li>Set permissions.<a name="ul1651480165315"></a><a name="ul1651480165315"></a><ul id="ul1651480165315"><li><strong id="b474465405115"><a name="b474465405115"></a><a name="b474465405115"></a>Read-only</strong>: allows you only to read data volumes in the container path.</li><li><strong id="b15880123195218"><a name="b15880123195218"></a><a name="b15880123195218"></a>Read/Write</strong>: allows you to modify the data volumes in the container path. Newly written data will not be migrated during container migration; otherwise, data loss occurs.</li></ul>
    </li></ol>
    </td>
    </tr>
    </tbody>
    </table>

3.  Click  **OK**.

## Importing SFS File Systems<a name="section283015149184"></a>

CCE allows you to import existing SFS file systems.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management **\>** Storage**. On the  **SFS**  tab page, click  **Import**.
2.  Select one or more SFS file systems that you want to attach and mount.
3.  Select the cluster and namespace to which you want to attach and mount the file system. Then, click  **OK**.

## Unbinding an SFS File System<a name="section1818108834"></a>

When an SFS file system is successfully created or attached, the SFS file system is automatically bound to the current cluster. Other clusters can also use the file system. When the SFS file system is unbound from the cluster, other clusters can still import and use the file system.

If the SFS file system has been mounted to a workload, the SFS file system cannot be unbound from the cluster.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Storage**. In the file system list, click  **Unbind**  next to the target file system.
2.  Confirm the unbinding, and click  **OK**.

## Using kubectl to Create an SFS File System<a name="section5806637172015"></a>

CCE allows you to create an SFS file system in the form of PersistentVolumeClaim \(PVC\).

1.  Configure kubectl. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).
2.  Run the following commands to configure the  **pvc-sfs-auto-example.yaml**  file, which is used to create a PVC.

    **touch pvc-sfs-auto-example.yaml**

    **vi pvc-sfs-auto-example.yaml**

    -   **Example YAML file for clusters of v1.15:**

        ```
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          name:  pvc-sfs-auto-example
          namespace: default
        spec:
          accessModes:
          - ReadWriteMany
          resources:
            requests:
              storage: 10Gi
          storageClassName: csi-nas
        ```

        In this example:

        -   **storageClassName**: name of the Kubernetes storage class. Set it to  **csi-nas**.
        -   **name**: name of the PVC to be created.
        -   **storage**: storage capacity in Gi.

    -   **Example YAML file for clusters of v1.13 or earlier:**

        ```
        apiVersion: v1 
        kind: PersistentVolumeClaim 
        metadata: 
          annotations: 
            volume.beta.kubernetes.io/storage-class: nfs-rw
          name: pvc-sfs-auto-example 
          namespace: default 
        spec: 
          accessModes: 
          - ReadWriteMany 
          resources: 
            requests: 
              storage: 10Gi
        ```

        In this example:

        -   volume.beta.kubernetes.io/storage-class: SFS file system type. Currently, the standard file protocol type \(nfs-rw\) is supported.
        -   name: name of the PVC to be created.
        -   storage: storage capacity in Gi.

3.  Run the following command to create a PVC:

    **kubectl create -f pvc-sfs-auto-example.yaml**

    After the command is executed, an SFS file system is created in the VPC to which the cluster belongs. Choose  **Resource Management \> Storage**  \>  **SFS**  or log in to the SFS console to view the file system.


## Using the Existing File Storage to Create a PVC<a name="section5378421361"></a>

CCE allows you to use the existing file storage to create a PersistentVolume. After the creation is successful, create the corresponding PersistentVolumeClaim and bind it to the PersistentVolume.

1.  Log in to the SFS console, create a file storage, and record the file storage ID, shared path, and capacity.
2.  Configure kubectl. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).
3.  Create a YAML file for creating the PersistentVolume. Assume that the file name is  **pv-sfs-example.yaml**

    **touch pv-sfs-example.yaml**

    **vi pv-sfs-example.yaml**

    -   **Example YAML file for clusters of v1.15:**

        ```
        apiVersion: v1
        kind: PersistentVolume
        metadata:
          name: pv-sfs-example
        spec:
          accessModes:
          - ReadWriteMany
          capacity:
            storage: 10Gi
          csi:
            driver: nas.csi.everest.io
            fsType: nfs
            volumeAttributes:
              everest.io/share-export-location: sfs-nas01.eu-de.otc.t-systems.com:/share-436304e8
              storage.kubernetes.io/csi
            ProvisionerIdentity: everest-csi-provisioner
            volumeHandle: 682f00bb-ace0-41d8-9b3e-913c9aa6b695
          persistentVolumeReclaimPolicy: Delete
          storageClassName: csi-nas
        ```

        In this example:

        -   **driver**: storage driver used to mount the volume. Set the driver to  **nas.csi.everest.io**  for the file system.
        -   **everest.io/share-export-location**: shared path for storing files.
        -   **volumeHandle**: file system ID.
        -   **storage**: file system size.
        -   **storageClassName**: name of the Kubernetes storage class. Set this field to  **csi-nas**.

    -   **Example YAML file for clusters of v1.11 and v1.13:**

        ```
        apiVersion: v1 
        kind: PersistentVolume 
        metadata: 
          name: pv-sfs-example 
        spec: 
          accessModes: 
          - ReadWriteMany 
          capacity: 
            storage: 10Gi 
          flexVolume: 
            driver: huawei.com/fuxinfs 
            fsType: nfs 
            options: 
              deviceMountPath: sfs-nas1.eu-de.otc.t-systems.com:/share-73bdfafd
              fsType: nfs 
              volumeID: f6976f9e-2493-419b-97ca-d7816008d91c 
          persistentVolumeReclaimPolicy: Delete 
          storageClassName: nfs-rw
        ```

        In this example:

        -   **driver**: storage driver used to mount the volume. Set the driver to  **huawei.com/fuxinfs**.
        -   **deviceMountPath**: shared path for storing files.
        -   **volumeID**: file system ID.
        -   **storage**: file system size.
        -   **storageClassName**: read/write mode supported by the file system. Currently,  **nfs-rw**  and  **nfs-ro **are supported.

    -   **Example YAML file for clusters of v1.9:**

        ```
        apiVersion: v1 
        kind: PersistentVolume 
        metadata: 
          name: pv-sfs-example 
          namespace: default 
        spec: 
          accessModes: 
          - ReadWriteMany 
          capacity: 
            storage: 10Gi 
          flexVolume: 
            driver: huawei.com/fuxinfs 
            fsType: nfs 
            options: 
              deviceMountPath: sfs-nas1.eu-de.***.t-systems.com:/share-73bdfafd
              fsType: nfs 
              kubernetes.io/namespace: default 
              volumeID: f6976f9e-2493-419b-97ca-d7816008d91c 
          persistentVolumeReclaimPolicy: Delete 
          storageClassName: nfs-rw
        ```

        In this example:

        -   **driver**: storage driver used to mount the volume. Set the driver to  **huawei.com/fuxinfs**.
        -   **deviceMountPath**: shared path for storing files.
        -   **volumeID**: file system ID.
        -   **storage**: file system size.
        -   **storageClassName**: read/write mode supported by the file system. Currently,  **nfs-rw**  and  **nfs-ro **are supported.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >The VPC to which the file system belongs must be the same as the VPC of the ECS VM to which the workload is planned.  

4.  Create a PV.

    **kubectl create -f pv-sfs-example.yaml**

5.  Create a YAML file for creating the PVC. Assume that the file name is  **pvc-sfs-example.yaml**.****

    **touch pvc-sfs-example.yaml**

    **vi pvc-sfs-example.yaml**

    -   **Example YAML file for clusters of v1.15:**

        ```
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          name: pvc-sfs-example
          namespace: default
        spec:
          accessModes:
          - ReadWriteMany
          resources:
            requests:
              storage: 10Gi
          storageClassName: csi-nas
          volumeName: pv-sfs-example
        ```

        In this example:

        -   **storageClassName**: Set it to  **csi-nas**. The value must be the same as that of the existing PV.
        -   **storage**: storage capacity, in the unit of Gi. The value must be the same as the storage size of the existing PV.
        -   **volumeName**: name of the PV.

    -   **Example YAML file for clusters of v1.11 and v1.13:**

        ```
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          annotations:
            volume.beta.kubernetes.io/storage-class: nfs-rw
            volume.beta.kubernetes.io/storage-provisioner: flexvolume-huawei.com/fuxinfs
          name: pvc-sfs-example
          namespace: default
        spec:
          accessModes:
          - ReadWriteMany
          resources:
            requests:
              storage: 10Gi
          volumeName: pv-sfs-example
        ```

        In this example:

        -   **volume.beta.kubernetes.io/storage-class**: read/write mode supported by the file system. Currently,  **nfs-rw**  and  **nfs-ro **are supported. The value must be the same as that of the existing PV.
        -   **volume.beta.kubernetes.io/storage-provisioner**: must be set to  **flexvolume-huawei.com/fuxinfs**.
        -   **storage**: storage capacity, in the unit of Gi. The value must be the same as the storage size of the existing PV.
        -   **volumeName**: name of the PV.

    -   **Example YAML file for clusters of v1.9:**

        ```
        apiVersion: v1
        kind: PersistentVolumeClaim
        metadata:
          annotations:
            volume.beta.kubernetes.io/storage-class: nfs-rw
            volume.beta.kubernetes.io/storage-provisioner: flexvolume-huawei.com/fuxinfs
          name: pvc-sfs-example
          namespace: default
        spec:
          accessModes:
          - ReadWriteMany
          resources:
            requests:
              storage: 10Gi
          volumeName: pv-sfs-example
          volumeNamespace: default
        ```

        In this example:

        -   **volume.beta.kubernetes.io/storage-class**: read/write mode supported by the file system. Currently,  **nfs-rw**  and  **nfs-ro **are supported. The value must be the same as that of the existing PV.
        -   **volume.beta.kubernetes.io/storage-provisioner**: must be set to  **flexvolume-huawei.com/fuxinfs**.
        -   **storage**: storage capacity, in the unit of Gi. The value must be the same as the storage size of the existing PV.
        -   **volumeName**: name of the PV.

6.  Create a PVC.

    **kubectl create -f pvc-sfs-example.yaml**


## Using an Existing PVC to Create a StatefulSet<a name="section740411301418"></a>

CCE allows you to use the existing file storage \(PersistentVolumeClaim\) to create a workload \(StatefulSet\).

1.  Create a file system by referring to  [Creating an SFS File System](#section1123416794811)  and record the name of the file system.
2.  Configure kubectl. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).
3.  Create a PVC file to create a workload. Assume that the file name is  **sfs-statefulset-example.yaml**.

    **touch sfs-statefulset-example.yaml**

    **vi sfs-statefulset-example.yaml**

    Configuration example:

    ```
    apiVersion: apps/v1
    kind: StatefulSet
    metadata:
      name: sfs-statefulset-example
      namespace: default
    spec:
      podManagementPolicy: OrderedReady
      replicas: 2
      revisionHistoryLimit: 10
      selector:
        matchLabels:
          app: sfs-statefulset-example
      serviceName: qwqq
      template:
        metadata:
          annotations:
            metrics.alpha.kubernetes.io/custom-endpoints: '[{"api":"","path":"","port":"","names":""}]'
            pod.alpha.kubernetes.io/initialized: "true"
          creationTimestamp: null
          labels:
            app: sfs-statefulset-example
        spec:
          affinity: {}
          containers:
          - env:
            - name: PAAS_APP_NAME
              value: sfs-statefulset-example
            - name: PAAS_NAMESPACE
              value: default
            - name: PAAS_PROJECT_ID
              value: b7bb7d77a2974a8fa8985cbfb63f23c0
            image: nginx:latest
            imagePullPolicy: Always
            name: container-0
            resources: {}
            terminationMessagePath: /dev/termination-log
            terminationMessagePolicy: File
            volumeMounts:
            - mountPath: /tmp
              name: pvc-sfs-example
          dnsPolicy: ClusterFirst
          imagePullSecrets:
          - name: default-secret
          restartPolicy: Always
          schedulerName: default-scheduler
          securityContext: {}
          terminationGracePeriodSeconds: 30
          volumes:
            - name: pvc-sfs-example
              persistentVolumeClaim:
                claimName: cce-sfs-demo
          tolerations:
          - effect: NoExecute
            key: node.kubernetes.io/not-ready
            operator: Exists
            tolerationSeconds: 300
          - effect: NoExecute
            key: node.kubernetes.io/unreachable
            operator: Exists
            tolerationSeconds: 300
      updateStrategy:
        type: RollingUpdate
    ```

    In this example:

    -   **spec.template.spec.containers.volumeMounts.name**  and  **spec.template.spec.volumes.name**  must be consistent because they have a mapping relationship.
    -   **replicas**: number of instances.
    -   **name**: name of the new workload.
    -   **image**: image used by the workload.
    -   **mountPath**: mounting path of a container.
    -   **serviceName**: service corresponding to the workload. For details about how to create a service, see  [Creating a StatefulSet](creating-a-statefulset.md).
    -   **claimName**: name of an existing PVC.

4.  Create a StatefulSet.

    **kubectl create -f  sfs-statefulset-example .yaml**


## Using kubectl to Mount a File Storage<a name="section1094712153215"></a>

1.  Run the following commands to configure the  **sfs-pod-example.yaml**  file, which is used to create a pod.

    **_touch sfs-pod-example.yaml_**

    **_vi sfs-pod-example.yaml_**

    -   Example of mounting file storage to a Deployment \(PVC sharing\):

        ```
        apiVersion: extensions/v1beta1 
        kind: Deployment 
        metadata: 
          name: sfs-pod-example                                # Workload name.
          namespace: default 
        spec: 
          replicas: 1 
          selector: 
            matchLabels: 
              app: sfs-pod-example 
          template: 
            metadata: 
              labels: 
                app: sfs-pod-example 
            spec: 
              containers: 
              - image: nginx 
                name: container-0 
                volumeMounts: 
                - mountPath: /tmp                                # Mounting path.
                  name: pvc-sfs-example 
              restartPolicy: Always 
              volumes: 
              - name: pvc-sfs-example 
                persistentVolumeClaim: 
                  claimName: pvc-sfs-auto-example                # Mounting PVC.
        ```

        In this example:

        -   **name**: name of the pod to be created.
        -   **app**: name of the pod workload.
        -   **mountPath**: mount path of the container. In this example, the mount path is  **/tmp**.
        -   **spec.template.spec.containers.volumeMounts.name**  and  **spec.template.spec.volumes.name**  must be consistent because they have a mapping relationship.

    -   Example of mounting a file system to a StatefulSet \(PVCTemplate inclusive\):
        -   **Example YAML file for clusters of v1.15:**

            ```
            apiVersion: apps/v1
            kind: StatefulSet
            metadata:
              name: deploy-sfs-nfs-rw-in
              namespace: default
              generation: 1
              labels:
                appgroup: ''
              annotations:
                container.io/container-0: 'https://console.***.t-systems/swr/dockerimage/nginx.png'
                description: ''
            spec:
              replicas: 2
              selector:
                matchLabels:
                  app: deploy-sfs-nfs-rw-in
              template:
                metadata:
                  labels:
                    app: deploy-sfs-nfs-rw-in
                  annotations:
                    metrics.alpha.kubernetes.io/custom-endpoints: '[{"api":"","path":"","port":"","names":""}]'
                    pod.alpha.kubernetes.io/initialized: 'true'
                spec:
                  containers:
                    - name: container-0
                      image: 'nginx:1.12-alpine-perl'
                      env:
                        - name: PAAS_APP_NAME
                          value: deploy-sfs-nfs-rw-in
                        - name: PAAS_NAMESPACE
                          value: default
                        - name: PAAS_PROJECT_ID
                          value: 8190a2a1692c46f284585c56fc0e2fb9
                      resources: {}
                      volumeMounts:
                        - name: bs-nfs-rw-mountoptionpvc
                          mountPath: /aaa
                      terminationMessagePath: /dev/termination-log
                      terminationMessagePolicy: File
                      imagePullPolicy: IfNotPresent
                  restartPolicy: Always
                  terminationGracePeriodSeconds: 30
                  dnsPolicy: ClusterFirst
                  securityContext: {}
                  imagePullSecrets:
                    - name: default-secret
                  affinity: {}
                  schedulerName: default-scheduler
              volumeClaimTemplates:
                - metadata:
                    name: bs-nfs-rw-mountoptionpvc
                    namespace: default
                    annotations: {}
                    enable: true
                  spec:
                    accessModes:
                      - ReadWriteMany
                    resources:
                      requests:
                        storage: 11Gi
                    storageClassName: csi-nas
              serviceName: wwww
              podManagementPolicy: OrderedReady
              updateStrategy:
                type: RollingUpdate
              revisionHistoryLimit: 10
            ```

            In this example:

            -   **name**: name of the StatefulSet.
            -   **image**: image of the StatefulSet.
            -   **mountPath**: mount path of the container. In this example, the mount path is  **/tmp**.
            -   **serviceName**: Service of the StatefulSet. For details about how to create a Service, see  [Creating a StatefulSet](creating-a-statefulset.md).
            -   **spec.template.spec.containers.volumeMounts.name**  and  **spec.volumeClaimTemplates.metadata.name**  must be consistent because they have a mapping relationship.

        -   **Example YAML file for clusters of v1.13 or earlier:**

            ```
            apiVersion: apps/v1
            kind: StatefulSet
            
            metadata:
              name: deploy-sfs-nfs-rw-in
              namespace: default
              generation: 1
              labels:
                appgroup: ''
              annotations:
                container.io/container-0: 'https://console.***.t-systems/swr/dockerimage/nginx.png'
                description: ''
            spec:
              replicas: 2
              selector:
                matchLabels:
                  app: deploy-sfs-nfs-rw-in
              template:
                metadata:
                  labels:
                    app: deploy-sfs-nfs-rw-in
                  annotations:
                    metrics.alpha.kubernetes.io/custom-endpoints: '[{"api":"","path":"","port":"","names":""}]'
                    pod.alpha.kubernetes.io/initialized: 'true'
                spec:
                  containers:
                    - name: container-0
                      image: 'nginx:1.12-alpine-perl'
                      env:
                        - name: PAAS_APP_NAME
                          value: deploy-sfs-nfs-rw-in
                        - name: PAAS_NAMESPACE
                          value: default
                        - name: PAAS_PROJECT_ID
                          value: 8190a2a1692c46f284585c56fc0e2fb9
                      resources: {}
                      volumeMounts:
                        - name: bs-nfs-rw-mountoptionpvc
                          mountPath: /aaa
                      terminationMessagePath: /dev/termination-log
                      terminationMessagePolicy: File
                      imagePullPolicy: IfNotPresent
                  restartPolicy: Always
                  terminationGracePeriodSeconds: 30
                  dnsPolicy: ClusterFirst
                  securityContext: {}
                  imagePullSecrets:
                    - name: default-secret
                  affinity: {}
                  schedulerName: default-scheduler
              volumeClaimTemplates:
                - metadata:
                    name: bs-nfs-rw-mountoptionpvc
                    creationTimestamp: null
                    annotations:
                      volume.beta.kubernetes.io/storage-class: nfs-rw
                      volume.beta.kubernetes.io/storage-provisioner: flexvolume-huawei.com/fuxinfs
                  spec:
                    accessModes:
                      - ReadWriteMany
                    resources:
                      requests:
                        storage: 11Gi
              serviceName: wwww
              podManagementPolicy: OrderedReady
              updateStrategy:
                type: RollingUpdate
              revisionHistoryLimit: 10
            ```

            In this example:

            -   **name**: name of the StatefulSet.
            -   **image**: image of the StatefulSet.
            -   **mountPath**: mount path of the container. In this example, the mount path is  **/tmp**.
            -   **serviceName**: Service of the StatefulSet. For details about how to create a Service, see  [Creating a StatefulSet](creating-a-statefulset.md).
            -   **spec.template.spec.containers.volumeMounts.name**  and  **spec.volumeClaimTemplates.metadata.name**  must be consistent because they have a mapping relationship.


2.  Run the following command to create a pod:

    **kubectl create -f sfs-pod-example.yaml**

    After the creation is complete, log in to the CCE console. In the navigation pane, choose  **Resource Management \> Storage**  \>  **SFS**. Then, click the PVC name. On the PVC details page, you can view the binding relationship between the SFS service and the PVC.


## Related Operations<a name="section359413445405"></a>

After the SFS file system is created, you can perform the operation described in  [Table 3](#table1619535674020).

**Table  3**  Other operations

<a name="table1619535674020"></a>
<table><thead align="left"><tr id="row111622425139"><th class="cellrowborder" valign="top" width="32%" id="mcps1.2.3.1.1"><p id="p81621742171318"><a name="p81621742171318"></a><a name="p81621742171318"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="68%" id="mcps1.2.3.1.2"><p id="p121621842131310"><a name="p121621842131310"></a><a name="p121621842131310"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row141621942121312"><td class="cellrowborder" valign="top" width="32%" headers="mcps1.2.3.1.1 "><p id="p4162174281310"><a name="p4162174281310"></a><a name="p4162174281310"></a>Deleting an SFS file system</p>
</td>
<td class="cellrowborder" valign="top" width="68%" headers="mcps1.2.3.1.2 "><a name="ol1216224219134"></a><a name="ol1216224219134"></a><ol id="ol1216224219134"><li>Select the name of the SFS file system to be deleted and click <strong id="b1458156395143933"><a name="b1458156395143933"></a><a name="b1458156395143933"></a>Delete</strong> in the <strong id="b182890197143933"><a name="b182890197143933"></a><a name="b182890197143933"></a>Operation</strong> column.</li><li>Follow the prompts to delete the SFS file system.</li></ol>
</td>
</tr>
</tbody>
</table>

