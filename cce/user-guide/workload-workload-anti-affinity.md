# Workload-Workload Anti-Affinity<a name="cce_01_0227"></a>

## Using the CCE Console<a name="section189731748476"></a>

1.  When  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md), in the  **Scheduling Policies**  area on the  **Configure Advanced Settings**  page, choose  **Inter-Pod Affinity and Anti-affinity**  \>  **Anti-affinity with Pods**  \>  **Add**.
2.  Select the workloads to which you want to deploy the target workload on a different node, and click  **OK**.

    The workload to be created and the selected workloads will be deployed on different nodes.


## Using kubectl<a name="section1894310152317"></a>

This section uses Nginx as an example to describe how to create a workload using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

When  [Using kubectl to Create a Deployment](creating-a-deployment.md#section155246177178)  or  [Using kubectl to Create a StatefulSet](creating-a-statefulset.md#section113441881214), configure workload-workload anti-affinity. The following is an example YAML file for workload-workload anti-affinity.

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
                operator: NotIn        
                values:
                - test     #workload's label value
```

## Setting the Object Type After Creating a Workload<a name="section097418414472"></a>

1.  Log in to the CCE console. In the navigation pane, choose** Workloads**  \>  **Deployments**  or  **Workload**  \>  **StatefulSets**.
2.  Click the name of the workload for which you will add a scheduling policy. On the workload details page, choose  **Scheduling Policies**  \>  **Add Simple Scheduling Policy**  \>  **Add Anti-affinity Object**.
3.  Set  **Object Type**  to  **Workload**  and select the workloads to be deployed on a different node from the created workload. The created workload and the selected workloads will be deployed on different nodes.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >This method can be used to add, edit, or delete scheduling policies.  


