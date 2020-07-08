# Using an EVS Disk<a name="cce_01_0147"></a>

CCE connects to EVS disks through its own plug-in to support persistent storage.

The following example shows how to define an EVS disk in a chart. When creating a workload from the chart, the  container  dynamically creates a 10 Gi EVS volume and mounts it to the container.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Currently, CCE supports only dynamic creation of EVS volumes.  

```
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: helm-test-slave
spec:
  updateStrategy: 
    type: "RollingUpdate"
  serviceName: helm-test-slave-headless
  replicas: 1
  template:
    metadata:
      labels:
        app: helm-test-slave
        type: slave
        release: "helm-test"
        failure-domain.beta.kubernetes.io/region: eu-de
        failure-domain.beta.kubernetes.io/zone: eu-de-02
    spec:
      containers:
        - name: helm-test-slave
          image: nginx:alpine-per1
          volumeMounts:
          - mountPath: /redis-data
            name: helm-test-slave
          - mountPath: /opt/rancher/
            name: utility
          - mountPath: /etc/redis/
            name: redis-conf
          ports:
            - containerPort: 6379
  volumeClaimTemplates:
  - metadata:
      labels:
        app: helm-test-slave
        type: slave
        release: "helm-test"
      name: helm-test-slave
      annotations:
        "volume.beta.kubernetes.io/storage-class": sata
        "volume.beta.kubernetes.io/storage-provisioner": flexvolume-huawei.com/fuxivol
    spec:
      accessModes: [ "ReadWriteMany" ]
      resources:
        requests:
          storage: 10Gi
```

**Table  1**  Key parameters

<a name="tf0d74c96d4d644c28756080d96ae451f"></a>
<table><thead align="left"><tr id="rb19bb2af6a804eb4ae712095c23e8528"><th class="cellrowborder" valign="top" width="34%" id="mcps1.2.3.1.1"><p id="af2270c23e4e0422a9fa4819d6668ce30"><a name="af2270c23e4e0422a9fa4819d6668ce30"></a><a name="af2270c23e4e0422a9fa4819d6668ce30"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="66%" id="mcps1.2.3.1.2"><p id="aa79c0bc202524cd8944e255b9764cfa4"><a name="aa79c0bc202524cd8944e255b9764cfa4"></a><a name="aa79c0bc202524cd8944e255b9764cfa4"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r3d6dd4d548f442d1b359beb9c9e2de02"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="a07b743a5ef3f4ac499454fc2781113a8"><a name="a07b743a5ef3f4ac499454fc2781113a8"></a><a name="a07b743a5ef3f4ac499454fc2781113a8"></a>* annotations</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="ac0e438319d1945a5be562776bd3c1c66"><a name="ac0e438319d1945a5be562776bd3c1c66"></a><a name="ac0e438319d1945a5be562776bd3c1c66"></a>Used for console display. <strong id="b84235270616237"><a name="b84235270616237"></a><a name="b84235270616237"></a>volume.beta.kubernetes.io/storage-class</strong> indicates the EVS disk type (SAS, SATA, or SSD). For details, see the definition of the EVS service. The value of <strong id="b632055709154325"><a name="b632055709154325"></a><a name="b632055709154325"></a>volume.beta.kubernetes.io/storage-provisioner</strong> is fixed at <strong id="b169980909154325"><a name="b169980909154325"></a><a name="b169980909154325"></a>flexvolume-huawei.com/fuxivol</strong>.</p>
</td>
</tr>
<tr id="r5b59ac4055b34c05b6a257adef5cd4b4"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="a1d449c56d98f4352bf4ef856c9ddfb11"><a name="a1d449c56d98f4352bf4ef856c9ddfb11"></a><a name="a1d449c56d98f4352bf4ef856c9ddfb11"></a>* accessModes</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p1299316521864"><a name="p1299316521864"></a><a name="p1299316521864"></a>EVS access mode.</p>
<a name="ul10542036464"></a><a name="ul10542036464"></a><ul id="ul10542036464"><li>ReadWriteOnce: The volume can be mounted as read-write by a single node.</li><li>ReadWriteMany: The volume can be mounted as read-write by many nodes.</li></ul>
</td>
</tr>
<tr id="rb135310abbeb43688de992c1ef4eae22"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="ae0e236ce839e4e749650c9df9855fed5"><a name="ae0e236ce839e4e749650c9df9855fed5"></a><a name="ae0e236ce839e4e749650c9df9855fed5"></a>* resource.request.storage</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="ab88fcdbd4a6a40a08d0c625ffefc9410"><a name="ab88fcdbd4a6a40a08d0c625ffefc9410"></a><a name="ab88fcdbd4a6a40a08d0c625ffefc9410"></a>Size of the EVS disk, in Gi. The minimum value is <strong id="b1564838559154343"><a name="b1564838559154343"></a><a name="b1564838559154343"></a>10</strong>.</p>
</td>
</tr>
<tr id="row1537016132912"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1353891602913"><a name="p1353891602913"></a><a name="p1353891602913"></a>* failure-domain.beta.kubernetes.io/region</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p10538181662913"><a name="p10538181662913"></a><a name="p10538181662913"></a>Region where an EVS disk is located.</p>
</td>
</tr>
<tr id="row229820317299"><td class="cellrowborder" valign="top" width="34%" headers="mcps1.2.3.1.1 "><p id="p1929823117296"><a name="p1929823117296"></a><a name="p1929823117296"></a>* failure-domain.beta.kubernetes.io/zone</p>
</td>
<td class="cellrowborder" valign="top" width="66%" headers="mcps1.2.3.1.2 "><p id="p3298123113295"><a name="p3298123113295"></a><a name="p3298123113295"></a>Partition where an EVS disk is located.</p>
</td>
</tr>
</tbody>
</table>

