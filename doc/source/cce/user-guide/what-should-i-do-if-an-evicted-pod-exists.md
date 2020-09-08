# What Should I Do If An Evicted Pod Exists?<a name="cce_faq_00209"></a>

Pod actions are classified into the following two types:

-   kube-controller-manager periodically checks the status of all nodes. If a node is in the NotReady state for a period of time, all pods on the node are evicted.
-   kubelet periodically checks the memory and disk resources of the node. If the resources are insufficient, pods are evicted based on the priority. Check results will be recorded in kubelet logs of the node. You can run the following command to search for the information:

    ```
    cat /var/paas/sys/log/kubernetes/kubelet.log | grep -i Evicted -C3
    ```


After a pod is evicted and scheduled to a new node, if pods in that node are also being evicted, the pod will be evicted again. Pods may be evicted repeatedly.

If the eviction is triggered by kube-controller-manager, a pod in the Terminating state is left. It is automatically deleted only after the node where the container is located is restored. If the node has been deleted or cannot be restored due to other reasons, you can forcibly delete the pod.

If the eviction is triggered by kubelet, a pod in the Evicted state is left. It is only used for subsequent fault locating and can be directly deleted.

**Common issues:**

Why is an evicted container frequently scheduled to the original node?

Answer: A node evicts a container based on the node resource usage. The evicted container is scheduled based on the allocated node resources. Eviction and scheduling are based on different rules. Therefore, an evicted container may be scheduled to the original node again.

This problem can be solved by properly allocating resources to each container.

