# Workload<a name="cce_01_0046"></a>

-   **[Overview](overview.md)**  
A  workload  is an abstract model of a group of pods in Kubernetes. Kubernetes classify workloads into  Deployments,  StatefulSets,  DaemonSets,  jobs, and  cron jobs.
-   **[Creating a Deployment](creating-a-deployment.md)**  
Deployments are workloads \(for example, Nginx\) that do not store any data or status.
-   **[Creating a StatefulSet](creating-a-statefulset.md)**  
StatefulSets  are a type of workloads whose data or status is stored while they are running. For example, MySQL is a StatefulSet because it needs to store new data.
-   **[Creating a Job](creating-a-job.md)**  
A  job  is executed only once immediately after being deployed. Before creating a workload, you can execute a job to upload an  image  to the  image repository.
-   **[Creating a Cron Job](creating-a-cron-job.md)**  
A  cron job  is a  short-lived job  that runs at a specified time. You can perform  time synchronization  for all active nodes at a fixed time point.
-   **[Managing a Deployment](managing-a-deployment.md)**  
After a Deployment is created, you can scale, upgrade, monitor, roll back, or delete the Deployment, as well as edit its YAML file.
-   **[Managing a StatefulSet](managing-a-statefulset.md)**  
After a StatefulSet is created, you can upgrade, scale, monitor, or delete it, as well as edit its YAML file and view its logs.
-   **[Scaling a Workload](scaling-a-workload.md)**  
After  scaling policies  are defined, instances can be automatically added or deleted based on resource changes, fixed time, and fixed periods. This reduces manual resource adjustment to cope with service changes and peak pressure, helping you save resources and labor costs.
-   **[Using a Third-Party Image](using-a-third-party-image.md)**  


