# Advanced Container Settings<a name="cce_01_0130"></a>

-   **[Setting Container Specifications](setting-container-specifications.md)**  
CCE allows you to set resource restrictions for added containers during workload creation. You can apply for and limit the CPU and memory used by each instance of the workload.
-   **[Setting Container Lifecycle Parameters](setting-container-lifecycle-parameters.md)**  
CCE provides  callback functions  for the lifecycle management of containerized workloads. For example, if you want a container to perform a certain operation before stopping, you can register a hook function.
-   **[Setting Container Startup Commands](setting-container-startup-commands.md)**  
When creating a workload, you can use an image to specify the processes running in the container.
-   **[Setting Health Check for a Container](setting-health-check-for-a-container.md)**  
Health check  regularly checks the health status of containers during container running. If the health check function is not configured, a pod cannot detect service exceptions or automatically restart the service to restore it. This will result in a situation where the pod status is normal but the service in the pod is abnormal.
-   **[Setting an Environment Variable](setting-an-environment-variable.md)**  
An  environment variable  is a variable set in the runtime environment of a container. Environment variables can be modified after the workload is deployed, providing flexibility for workloads.
-   **[Collecting Standard Output Logs of Containers](collecting-standard-output-logs-of-containers.md)**  
CCE allows you to configure policies for collecting, managing, and analyzing workload logs periodically to prevent logs from being over-sized.
-   **[Collecting Container Logs from Specified Paths](collecting-container-logs-from-specified-paths.md)**  
CCE allows you to configure policies for collecting, managing, and analyzing workload logs periodically to prevent logs from being over-sized.

