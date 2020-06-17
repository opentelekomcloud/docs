# Workload-Node Anti-Affinity<a name="cce_01_0226"></a>

## Using the CCE Console<a name="section122391413184616"></a>

1.  When  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md), in the  **Scheduling Policies**  area on the  **Configure Advanced Settings**  page, choose  **Workload-Node Affinity and Anti-affinity**  \>  **Anti-affinity with Nodes**  \>  **Add**.
2.  Select the node on which the workload is ineligible to be deployed, and click  **OK**.

    If you select multiple nodes, the workload will not be deployed on these nodes.


## Using kubectl<a name="section1361482522712"></a>

This section uses Nginx as an example to describe how to create a workload using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

When  [Using kubectl to Create a Deployment](creating-a-deployment.md#section155246177178)  or  [Using kubectl to Create a StatefulSet](creating-a-statefulset.md#section113441881214), configure workload-node anti-affinity. The following is an example YAML file for workload-node anti-affinity.

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
                  operator: NotIn        #Indicates that the workload will not be deployed on the node.
                  values:
                - test-node-1          #node's label value
```

## Setting the Object Type After Creating a Workload<a name="section02391513134618"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**  or  **Workload**  \>  **StatefulSets**.
2.  Click the name of the workload for which you will add a scheduling policy. On the workload details page, choose  **Scheduling Policies**  \>  **Add Simple Scheduling Policy**  \>  **Add Anti-affinity Object**.
3.  Set  **Object Type**  to  **Node**  and select the node on which the workload is ineligible to be deployed. The workload will be constrained from being deployed on the selected node.

    >![](/images/icon-note.gif) **NOTE:**   
    >This method can be used to add, edit, or delete scheduling policies.  


