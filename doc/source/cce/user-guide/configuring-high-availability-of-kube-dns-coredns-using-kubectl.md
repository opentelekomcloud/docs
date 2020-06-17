# Configuring High Availability of kube-dns/CoreDNS Using kubectl<a name="cce_01_0162"></a>

Use the Kubernetes command line tool \(kubectl\) to configure  high-availability  of kube-dns/CoreDNS.

kube-dns/CoreDNS provides the Domain Name Service \(DNS\) for clusters. It is advised to configure multiple kube-dns/CoreDNS for a cluster. If there is only one kube-dns/CoreDNS in a cluster, the entire cluster will not run properly once the kube-dns/CoreDNS is down.

>![](/images/icon-note.gif) **NOTE:**   
>-   By default, CCE clusters of Kubernetes v1.11 and later versions have CoreDNS installed.  
>-   For more information about the DNS, see  [CoreDNS \(System Resource Add-on, Mandatory\)](coredns-(system-resource-add-on-mandatory).md)  or  [Using Kubernetes In-Cluster DNS](using-kubernetes-in-cluster-dns.md).  

This section takes VM clusters as an example. The operations for bare metal clusters are the same.

## Preparation<a name="s749b044f6e864a919f0c0616cfad1dab"></a>

The cluster is accessible from a public network, or the cluster and the client are in the same VPC.

## Procedure<a name="s6797453bdad1452db7d603668deda069"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Clusters**, and click  **Kubectl**  under the cluster to be connected.
2.  Set the API access mode for the cluster.
3.  Configure the kubectl.

    After the kubectl is successfully configured, you can use it to manually configure high availability of kube-dns/CoreDNS.

4.  Log in to the client.
5.  Edit the deployment configuration file of kube-dns/CoreDNS.

    The following uses the CoreDNS as an example:

    **kubectl edit deployment coredns -n kube-system**

    Change the value of  **replicas**  in the  **spec**  section in the deployment configuration file to the number of kube-dns/CoreDNS instances required.

    Example:

    ```
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      annotations:
        deployment.kubernetes.io/revision: "1"
      creationTimestamp: 2019-02-11T09:36:04Z
      generation: 1
      labels:
        app: coredns
        kubernetes-app: coredns
        kubernetes.io/cluster-service: "true"
        kubernetes.io/name: CoreDNS
        release: cceaddon-coredns
      name: coredns
      namespace: kube-system
      resourceVersion: "1927"
      selfLink: /apis/extensions/v1beta1/namespaces/kube-system/deployments/coredns
      uid: 737b9296-2de0-11e9-b629-fa163e7fb882
    spec:
      progressDeadlineSeconds: 600
      replicas: 2
      revisionHistoryLimit: 10
      selector:
        matchLabels:
          app: coredns
          kubernetes-app: coredns
      strategy:
        rollingUpdate:
          maxSurge: 10%
          maxUnavailable: 0
        type: RollingUpdate
      template:
        metadata:
          annotations:
            checksum/config: 3095a9b4028195e7e0b8b22c550bf183d0b7a8a7eba20808b36081d0b39f8b81
    ```


