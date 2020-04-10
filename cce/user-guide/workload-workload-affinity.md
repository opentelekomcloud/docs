# Workload-Workload Affinity<a name="cce_01_0220"></a>

## Using the CCE Console<a name="section152331930174616"></a>

1.  When  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md), in the  **Scheduling Policies**  area on the  **Configure Advanced Settings**  page, choose  **Workload-Workload Affinity and Anti-affinity**  \>  **Affinity with Workloads**\>  **Add**.
2.  Select the workloads that will be co-located with the current workload on the same node, and click  **OK**.

    The workload to be created will be deployed on the same node as the selected affinity workloads.


## Using kubectl<a name="section5140193643912"></a>

This section uses Nginx as an example to describe how to create a workload using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

When  [Using kubectl to Create a Deployment](creating-a-deployment.md#section155246177178)  or  [Using kubectl to Create a StatefulSet](creating-a-statefulset.md#section113441881214), configure workload-workload affinity. The following is an example YAML file for workload-workload affinity.

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
      affinity:
        podAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
                - key: app          #workload's label key
                  operator: In        
                  values:
                  - test     #workload's label value
```

## Setting the Object Type After Creating a Workload<a name="section5234830134613"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**  or  **Workload**  \>  **StatefulSets**.
2.  Click the name of the workload for which you will add a scheduling policy. On the workload details page, choose  **Scheduling Policies**  \>  **Add Simple Scheduling Policy**  \>  **Add Affinity Object**.
3.  Set  **Object Type**  to  **Workload**  and select the workloads to be deployed on the same node as the created workload. The created workload and the selected workloads will deployed on the same node.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >This method can be used to add, edit, or delete scheduling policies.  


