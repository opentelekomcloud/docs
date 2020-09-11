# Workload-AZ Affinity<a name="cce_01_0228"></a>

## Using the CCE Console<a name="section1243114616439"></a>

1.  When  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md), in the  **Scheduling Policies**  area on the  **Configure Advanced Settings**  page, click  ![](figures/icon-monitoring.png)  next to  **Workload-AZ Affinity and Anti-affinity**  \>  **Affinity with AZs**.
2.  Select the AZ in which you want to deploy the workload.

    The created workload will be deployed in the selected AZ.


## Using kubectl<a name="section4201420133117"></a>

This section uses an Nginx workload as an example to describe how to create a workload using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

When  [Using kubectl to Create a Deployment](creating-a-deployment.md#section155246177178)  or  [Using kubectl to Create a StatefulSet](creating-a-statefulset.md#section113441881214), configure workload-AZ affinity. The following is an example YAML file for workload-AZ affinity.

```
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: az-in-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: az-in-deployment
  strategy:
    type: RollingUpdate
  template:
    metadata:
      labels:
        app: az-in-deployment
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
              - key: failure-domain.beta.kubernetes.io/zone #node's label key
                operator: In        
                values:
                - az1                              # node's key value
```

## Setting the Object Type After Creating a Workload<a name="section19244104614316"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**  or  **Workload**  \>  **StatefulSets**.
2.  Click the name of the workload for which you will add a scheduling policy. On the workload details page, choose  **Scheduling Policies**  \>  **Add Simple Scheduling Policy**  \>  **Add Affinity Object**.
3.  Set  **Object Type**  to  **Availability Zone**, and select the AZ in which the workload is eligible to be deployed. The workload will be deployed in the selected AZ.

    >![](/images/icon-note.gif) **NOTE:**   
    >This method can be used to add, edit, or delete scheduling policies.  


