# Workload-Node Affinity<a name="cce_01_0225"></a>

## Using the CCE Console<a name="section186032460457"></a>

1.  When  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md), in the  **Scheduling Policies**  area on the  **Configure Advanced Settings**  page, choose  **Workload-Node Affinity and Anti-affinity**  \>  **Affinity with Nodes**  \>  **Add**.
2.  Select the node on which you want to deploy the workload, and click  **OK**.

    If you select multiple nodes, the system automatically chooses one of them during workload deployment.


## Using kubectl<a name="section711574271117"></a>

This section uses an Nginx workload as an example to describe how to create a workload using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

When  [Using kubectl to Create a Deployment](creating-a-deployment.md#section155246177178)  or  [Using kubectl to Create a StatefulSet](creating-a-statefulset.md#section113441881214), configure workload-node affinity. The following is an example YAML file for workload-node affinity.

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
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: nodeName          #node's label key
                operator: In
                values:
                - test-node-1          #node's label value
```

## Setting the Object Type After Creating a Workload<a name="section15605646144516"></a>

1.  Log in to the CCE console. In the navigation pane, choose** Workloads**  \>  **Deployments**  or  **Workload**  \>  **StatefulSets**.
2.  Click the name of the workload for which you will add a scheduling policy. On the workload details page, choose  **Scheduling Policies**  \>  **Add Simple Scheduling Policy**  \>  **Add Affinity Object**.
3.  Set  **Object Type**  to  **Node**  and select the node where the workload is to be deployed. The workload will be deployed on the selected node.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >This method can be used to add, edit, or delete scheduling policies.  


