# Workload-AZ Anti-Affinity<a name="cce_01_0229"></a>

## Using the CCE Console<a name="section13854613443"></a>

1.  When  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md), in the  **Scheduling Policies**  area on the  **Configure Advanced Settings**  page, click  ![](figures/icon-monitoring-9.png)  next to  **Workload-AZ Affinity and Anti-affinity**  \>  **Anti-affinity with AZs**.
2.  Select an AZ in which the workload is ineligible to be deployed.

    The created workload is not deployed on the selected AZ.


## Using kubectl<a name="section102822029173111"></a>

This section uses Nginx as an example to describe how to create a workload using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

When  [Using kubectl to Create a Deployment](creating-a-deployment.md#section155246177178)  or  [Using kubectl to Create a StatefulSet](creating-a-statefulset.md#section113441881214), configure workload-AZ anti-affinity. The following is an example YAML file for workload-AZ anti-affinity.

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
              - key: failure-domain.beta.kubernetes.io/zone       #node's label key   
                operator: NotIn        
                values:
                - az1                                   #node's key value
```

## Setting the Object Type After Creating a Workload<a name="section1914684415"></a>

1.  Log in to the CCE console. In the navigation pane, choose** Workloads**  \>  **Deployments**  or  **Workload**  \>  **StatefulSets**.
2.  Click the name of the workload for which you will add a scheduling policy. On the workload details page, choose  **Scheduling Policies**  \>  **Add Simple Scheduling Policy**  \>  **Add Anti-affinity Object**.
3.  Set  **Object Type**  to  **Availability Zone**  and select the AZ in which the workload is ineligible to be deployed. The workload will be constrained from being deployed in the selected AZ.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >This method can be used to add, edit, or delete scheduling policies.  


