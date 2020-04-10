# Introduction<a name="cce_01_0191"></a>

CCE uses Kubernetes Helm, a package manager, to simplify deployment and management of packages \(also called charts\). A chart is a collection of files that describe a related set of Kubernetes resources. The use of charts handles all the complexity in Kubernetes resource installation and management, making it possible to achieve unified resource scheduling and management.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>Helm is a tool for packaging Kubernetes applications. For more information, see  [Helm documentation](https://helm.sh/).  

Custom charts simplify workload deployment.

This section describes how to create a workload using a custom chart. You can use multiple methods to create an orchestration chart on the CCE console.

## Constraints<a name="section148624339590"></a>

-   A user can upload a maximum of 20 charts.
-   A chart with multiple versions consumes the same amount of portion of chart quota.

