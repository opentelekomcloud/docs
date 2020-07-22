# What Should I Do If the OOM Killer Is Triggered When a Container Uses Memory Resources More Than Limited?<a name="cce_faq_00002"></a>

If a node has sufficient memory resources, a container on this node can use more memory resources than requested, but no more than limited. If the memory allocated to a container exceeds the upper limit, the container is stopped first. If the container continuously uses memory resources more than limited, the container is terminated. If a stopped container is allowed to be restarted, kubelet will restart it, but other types of run errors will occur.

## Scenario 1<a name="en-us_topic_0242566259_section084113417487"></a>

The node's memory has reached the memory limit reserved for the node. As a result, OOM killer is triggered.

**Solution**

You can either scale up the node or migrate the pods on the node to other nodes.

## Scenario 2<a name="en-us_topic_0242566259_section1190644417499"></a>

The upper limit of resources configured for the pod is too small. When the actual usage exceeds the limit, OOM killer is triggered.

**Solution**

Set a higher upper limit for the workload.

## Example<a name="en-us_topic_0242566259_section991734310316"></a>

A pod will be created and allocated memory that exceeds the limit. As shown in the following configuration file of the pod, the pod requests 50 MB memory and the memory limit is set to 100 MB.

Example YAML file \(memory-request-limit-2.yaml\):

```
apiVersion: v1
kind: Pod
metadata:
  name: memory-demo-2
spec:
  containers:
  - name: memory-demo-2-ctr
    image: vish/stress
    resources:
      requests:
        memory: 50Mi
      limits:
        memory: "100Mi"
    args:
    - -mem-total
    - 250Mi
    - -mem-alloc-size
    - 10Mi
    - -mem-alloc-sleep
    - 1s
```

The  **args**  parameters indicate that the container attempts to allocate 250 MB memory, which exceeds the pod's upper limit \(100 MB\).

Creating a pod:

```
kubectl create -f https://k8s.io/docs/tasks/configure-pod-container/memory-request-limit-2.yaml --namespace=mem-example 
```

Viewing the details about the pod:

```
kubectl get pod memory-demo-2 --namespace=mem-example 
```

In this stage, the container may be running or be killed. If the container is not killed, repeat the previous command until the container is killed.

```
NAME            READY     STATUS      RESTARTS   AGE 
memory-demo-2   0/1       OOMKilled   1          24s
```

Viewing detailed information about the container:

```
kubectl get pod memory-demo-2 --output=yaml --namespace=mem-example 
```

This output indicates that the container is killed because the memory limit is exceeded.

```
lastState:
   terminated:
     containerID: docker://7aae52677a4542917c23b10fb56fcb2434c2e8427bc956065183c1879cc0dbd2
     exitCode: 137
     finishedAt: 2020-02-20T17:35:12Z
     reason: OOMKilled
     startedAt: null
```

In this example, the container can be automatically restarted. Therefore, kubelet will start it again. You can run the following command several times to see how the container is killed and started:

```
kubectl get pod memory-demo-2 --namespace=mem-example
```

The preceding command output indicates how the container is killed and started back and forth:

```
stevepe@sperry-1:~/steveperry-53.github.io$ kubectl get pod memory-demo-2 --namespace=mem-example 
NAME            READY     STATUS      RESTARTS   AGE 
memory-demo-2   0/1       OOMKilled   1          37s
stevepe@sperry-1:~/steveperry-53.github.io$ kubectl get pod memory-demo-2 --namespace=mem-example 
NAME            READY     STATUS    RESTARTS   AGE 
memory-demo-2   1/1       Running   2          40s
```

Viewing the historical information of the pod:

```
kubectl describe pod memory-demo-2 --namespace=mem-example 
```

The following command output indicates that the pod is repeatedly killed and started.

```
... Normal  Created   Created container with id 66a3a20aa7980e61be4922780bf9d24d1a1d8b7395c09861225b0eba1b1f8511 
... Warning BackOff   Back-off restarting failed container
```

