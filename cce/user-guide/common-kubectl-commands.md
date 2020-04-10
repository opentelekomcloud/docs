# Common kubectl Commands<a name="cce_01_0139"></a>

## Getting Started<a name="section18967103615461"></a>

**get**

The  **get**  command displays one or many resources of a cluster.

This command prints a table of the most important information about all resources, including cluster nodes, running pods, replication controllers, and services.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>A cluster can have multiple namespaces. If no namespace is specified, this command will run with the  **--namespace=default**  flag.  

Examples:

To list all pods with detailed information:

```
kubectl get po -o wide
```

To display pods in all namespaces:

```
kubectl get po --all-namespaces
```

To list labels of pods in all namespaces:

```
kubectl get po --show-labels
```

To list all namespaces of the node:

```
kubectl get namespace
```

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>To list information of other nodes, run this command with the  **-s**  flag. To list a specified type of resources, add the resource type to this command, for example,  **kubectl get rc**,  **kubectl get svc**,  **kubectl get nodes**, and  **kubectl get deploy**.  

To list a pod with a specified name in YAML output format:

```
kubectl get po <podname> -o yaml
```

To list a pod with a specified name in JSON output format:

```
kubectl get po <podname> -o json
```

```
kubectl get po rc-nginx-2-btv4j -o=custom-columns=LABELS:.metadata.labels.app
```

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>**LABELS**  indicates a comma separated list of user-defined column titles.  **metadata.labels.app**  indicates the data to be listed in either YAML or JSON output format.  

**create**

The  **create**  command creates a cluster resource from a file or input.

If there is already a resource descriptor \(a YAML or JSON file\), you can create the resource from the file by running the following command:

```
kubectl create -f filename
```

**expose**

The  **expose**  command exposes a resource as a new Kubernetes service. Possible resources include a pod, replication controller, service, and deployment.

```
kubectl expose deployment deployname --port=81 --type=NodePort --target-port=80 --name=service-name
```

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The example command creates a service of NodePort type for the deployment with the name specified in  **deployname**. The service will serve on port 81 specified in  **-port**  and connect to the containers on port 80 specified in  **-target-port**. More specifically, the service is reachable at <cluster-internal IP address\>:<port\>, and containers are reachable at <node IP address\>:<target-port\>.  

**run**

Examples:

To run a particular image in the cluster:

```
kubectl run deployname --image=nginx:latest
```

To run a particular image using a specified command:

```
kubectl run deployname -image=busybox --command -- ping baidu.com
```

**set**

The  **set**  command configures object resources.

Example:

To change the image of a deployment with the name specified in  **deployname**  to image 1.0:

```
kubectl set image deploy deployname containername=containername:1.0
```

**edit**

The  **edit**  command edits a resource from the default editor.

Examples:

To update a pod:

```
kubectl edit po po-nginx-btv4j
```

The example command yields the same effect as the following command:

```
kubectl get po po-nginx-btv4j -o yaml >> /tmp/nginx-tmp.yaml
vim /tmp/nginx-tmp.yaml
/*do some changes here */
kubectl replace -f /tmp/nginx-tmp.yaml
```

**explain**

The  **explain**  command gets documentation for a resource.

Example:

To get documentation of pods or services:

```
kubectl explain pods,svc
```

**delete**

The  **delete**  command deletes resources by resource name or label.

Example:

To delete a pod with minimal delay:

```
kubectl delete po podname --now 
```

```
kubectl delete -f nginx.yaml
kubectl delete deployment deployname
```

## Deployment Commands<a name="section122665712261"></a>

**rolling-update\***

**rolling-update**  is a very important command. It updates a running service with zero downtime. Pods are incrementally replaced by new ones. One pod is updated at a time. The old pod is deleted only after the new pod is up. New pods must be distinct from old pods by name, version, and label. Otherwise, an error message will be reported.

```
kubectl rolling-update poname -f newfilename
kubectl rolling-update poname -image=image:v2
```

If any problem occurs during the rolling update, run the command with the  **-rollback**  flag to abort the rolling update and revert to the previous pod.

```
kubectl rolling-update poname -rollback
```

**rollout**

The  **rollout**  command manages the rollout of a resource.

Examples:

To check the rollout status of a particular deployment:

```
kubectl rollout status deployment/deployname
```

To view the rollout history of a particular deployment:

```
kubectl rollout history deployment/deployname
```

To roll back to the previous deployment: \(by default, a resource is rolled back to the previous version\)

```
kubectl rollout undo deployment/test-nginx
```

**scale**

The  **scale**  command sets a new size for a resource by adjusting the number of resource replicas.

```
kubectl scale deployment deployname --replicas=newnumber
```

**autoscale**

The  **autoscale**  command automatically chooses and sets the number of pods. This command specifies the range for the number of pod replicas maintained by a replication controller. If there are too many pods, the replication controller terminates the extra pods. If there are too few, the replication controller starts more pods.

```
kubectl autoscale deployment deployname --min=minnumber --max=maxnumber
```

## Cluster Management Commands<a name="section286451412289"></a>

**cordon, drain, uncordon\***

If a node to be upgraded is running many pods or is already down, perform the following steps to prepare the node for maintenance:

1.  Run the  **cordon**  command to mark a node as unschedulable. This means that new pods will not be scheduled onto the node.

    ```
    kubectl cordon nodename
    ```

2.  Run the  **drain**  command to smoothly migrate the running pods from the node to another node.

    ```
    kubectl drain newnodename
    ```

3.  Perform maintenance operations on the node, such as upgrading the kernel and upgrading Docker.
4.  After node maintenance is completed, run the  **uncordon**  command to mark the node as schedulable.

    ```
    kubectl uncordon nodename
    ```


**cluster-info**

To display the add-ons running in the cluster:

```
kubectl cluster-info
```

To dump current cluster information to stdout:

```
kubectl cluster-info dump
```

**top\***

The  **top**  command displays resource \(CPU/memory/storage\) usage. This command requires Heapster to be correctly configured and working on the server.

**taint\***

The  **taint**  command updates the taints on one or more nodes.

**certificate\***

The  **certificate**  command modifies the certificate resources.

## Fault Diagnosis and Debugging Commands<a name="section2283324202914"></a>

**describe**

The  **describe**  command is similar to the  **get**  command. The difference is that the  **describe**  command shows details of a specific resource or group of resources, whereas the  **get**  command lists one or more resources in a cluster. The  **describe**  command does not support the  **-o**  flag. For resources of the same type, resource details are printed out in the same format.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If the information about a resource is queried, you can use the get command to obtain more detailed information. If you want to check the status of a specific resource, for example, to check if a pod is in the running state, run the  **describe**  command to show more detailed status information.  
>```  
>kubectl describe po <podname>  
>```  

**logs**

The  **logs**  command prints logs for a container in a pod or specified resource to stdout. To display logs in the tail -f mode, run this command with the  **-f**  flag.

```
kubectl logs -f podname
```

**exec**

The kubectl  **exec**  command is similar to the Docker  **exec**  command and executes a command in a container. If there are multiple containers in a pod, use the  **-c**  flag to choose a container.

```
kubectl exec -it podname bash
kubectl exec -it podname -c containername bash
```

**port-forward\***

The  **port-forward**  command forwards one or more local ports to a pod.

Example:

To listen on ports 5000 and 6000 locally, forwarding data to/from ports 5000 and 6000 in the pod:

```
kubectl port -forward podname 5000:6000
```

**proxy\***

The  **proxy**  command creates a proxy server between localhost and the Kubernetes API server.

Example:

To enable the HTTP Rest interface on the master node:

```
kubectl proxy -accept-hosts= '.*' -port=8001 -address= '0.0.0.0'
```

**cp**

The  **cp**  command copies files and directories to and from containers.

```
cp filename newfilename
```

**auth\***

The  **auth**  command inspects authorization.

**attach\***

The  **attach**  command is similar to the  **logs -f**  command and attaches to a process that is already running inside an existing container. To exit, run the  **ctrl-c**  command. If a pod contains multiple containers, to view the output of a specific container, use the  **-c**  flag preceded by podname to choose a container.

```
kubectl attach podname -c containername
```

## Advanced Commands<a name="section1870143812302"></a>

**replace**

The  **replace**  command updates or replaces an existing resource by attributes including the number of replicas, labels, image versions, and ports. You can directly modify the original YAML file and then run the  **replace**  command.

```
kubectl replace -f filename
```

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Resource names cannot be updated. After a pod label is updated, pods with the original label will fall out of the scope of the replication controller using the new label selector. The replication controller notices that some pods no longer match its new label selector and spun up a specified number of new pod replicas to replace original pods. By default, original pods with the original label are not deleted. In this case, if you run the  **get po**  command, you will find that the number of pods is doubled. The original pods are no longer controlled by the replication controller using the new label selector.  

**apply\***

The  **apply**  command provides a more strict control on resource updating than  **patch**  and  **edit**  commands. The  **apply**  command applies a configuration to a resource and maintains a set of configuration files in source control. Whenever there is an update, the configuration file is pushed to the server, and then the kubectl  **apply**  command applies the latest configuration to the resource. The Kubernetes compares the new configuration file with the original one and updates only the changed configuration instead of the whole file. The configuration that is not contained in the  **-f**  flag will remain unchanged. Unlike the  **replace**  command which deletes the resource and create a new one, the  **apply**  command directly updates the original resource. Similar to the git operation, the  **apply**  command adds an annotation to the resource to mark the current apply.

```
kubectl apply -f
```

**patch**

If you want to modify attributes of a running container without first deleting the container or using the  **replace**  command, the  **patch**  command is to the rescue. The  **patch**  command updates field\(s\) of a resource using strategic merge patch, a JSON merge patch, or a JSON patch. For example, to change a pod label from  **app=nginx1**  to  **app=nginx2**  while the pod is running, use the following command:

```
kubectl patch pod podname -p '{"metadata":{"lables":{"app":"nginx1"}}}'
```

**convent\***

The  **convert**  command converts configuration files between different API versions.

## Configuration Commands<a name="section20145838123111"></a>

**label**

The  **label**  command update labels on a resource.

```
kubectl label pods my-pod new-label=newlabel
```

**annotate**

The  **annotate**  command update annotations on a resource.

```
kubectl label pods my-pod icon-url=http://……
```

**completion**

The  **completion**  command provides autocompletion for shell.

## Other Commands<a name="section44619483210"></a>

**api-versions**

The  **api-versions**  command prints the supported API versions.

```
kubectl api-versions
```

**api-resources**

The  **api-resources**  command prints the supported API resources.

```
kubectl api-resources
```

**config\***

The  **config**  command modifies kubeconfig files. An example use case of this command is to configure authentication information in API calls.

**help**

The  **help**  command gets all command references.

**version**

The  **version**  command prints the client and server version information for the current context.

```
kubectl version
```

