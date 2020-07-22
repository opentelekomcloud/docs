# What Should I Do If Pods in the Terminating State Cannot Be Deleted?<a name="cce_faq_00210"></a>

## Symptom<a name="en-us_topic_0242566255_section6692125519183"></a>

When a node is in the Unavailable state, CCE migrates container pods on the node and sets the pods running on the node to the  **Terminating**  state.

After the node is restored, the pods in the  **Terminating**  state are automatically deleted.

Some pods are in the  **Terminating**  state occasionally.

![](figures/terminating.png)

The pods cannot be deleted by running the  **kubectl delete pods**  command.

```
kubectl delete pods httpd-app-6df58645c6-cxgcm
```

## Solution<a name="en-us_topic_0242566255_section321621711138"></a>

You can run the following command to forcibly delete the pods created in any ways:

```
kubectl delete pods <pod> --grace-period=0 --force
```

Therefore, you can run the following command to delete the pod  **httpd-app-6df58645c6-cxgcm**:

```
kubectl delete pods httpd-app-6df58645c6-cxgcm --grace-period=0 --force
```

