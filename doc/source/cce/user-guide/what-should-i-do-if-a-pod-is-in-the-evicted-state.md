# What Should I Do If a Pod Is in the Evicted State?<a name="cce_faq_00199"></a>

## Problem<a name="en-us_topic_0242566258_section19742165464710"></a>

Workload pods in the cluster fail and are being redeployed constantly.

After the following command is run, the command output shows that many pods are in the evicted state.

```
kubectl get pods
```

## Possible Cause<a name="en-us_topic_0242566258_section1752181225011"></a>

When a node is abnormal, Kubernetes evicts pods on the node. This problem is often caused by insufficient resources.

## Solution<a name="en-us_topic_0242566258_section127261381585"></a>

Check resource usage and locate the fault.

Run the following command to delete the evicted pods:

```
kubectl get pods | grep Evicted | awk '{print $1}' | xargs kubectl delete pod 
```

## Reference<a name="en-us_topic_0242566258_section125827455817"></a>

[Kubelet does not delete evicted pods](https://github.com/kubernetes/kubernetes/issues/55051)

