# CoreDNS \(System Resource Add-on, Mandatory\)<a name="cce_01_0129"></a>

## Introduction<a name="section25311744154917"></a>

The CoreDNS add-on is a DNS server that provides domain name resolution services for Kubernetes clusters. CoreDNS chains plug-ins to provide additional features.

CoreDNS is an open-source software and has been a part of CNCF. coredns provides a means for cloud services to discover each other in cloud-native deployments. CoreDNS chains plug-ins. Each plug-in provides a particular DNS function. You can integrate CoreDNS with only the plug-ins you need to make CoreDNS fast, efficient, and flexible. When used in a Kubernetes cluster, CoreDNS can automatically discover services in the cluster and provide domain name resolution for these services. By working with DNS server, CoreDNS can resolve external domain names for workloads in a cluster. Kubernetes v1.11 and later back CoreDNS as the official default DNS for all clusters going forward.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>-   By default, CoreDNS is installed in clusters of Kubernetes v1.11 and later.
>-   Whenever there is an update or bug fix to CoreDNS, you only need to install or upgrade CoreDNS instead of upgrading or creating the cluster.
>    For details, see  [Using Kubernetes In-Cluster DNS](using-kubernetes-in-cluster-dns.md)  or  [Configuring High Availability of kube-dns/CoreDNS Using kubectl](configuring-high-availability-of-kube-dns-coredns-using-kubectl.md).

## Installing the Add-on<a name="section776571919194"></a>

By default, CoreDNS is installed in CCE clusters of Kubernetes v1.11 and later.

If CoreDNS is not installed in a cluster, perform the following steps to install it:

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Marketplace**  tag page, click  **Install Add-on**  under  **coredns**.
2.  On the  **Install Add-on**  page, select the cluster and the add-on version, and click  **Next: Configuration**.
3.  In the  **Configure Specifications**  step, set parameters listed in  [Table 1](#table924319911495).

    **Table  1**  coredns add-on parameters

    <a name="table924319911495"></a>
    <table><thead align="left"><tr id="row42442974913"><th class="cellrowborder" valign="top" width="24%" id="mcps1.2.3.1.1"><p id="p17244793496"><a name="p17244793496"></a><a name="p17244793496"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="76%" id="mcps1.2.3.1.2"><p id="p42441596495"><a name="p42441596495"></a><a name="p42441596495"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1137014404511"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p11370134095120"><a name="p11370134095120"></a><a name="p11370134095120"></a>Add-on Specifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p937064085113"><a name="p937064085113"></a><a name="p937064085113"></a>Concurrent domain name resolution ability. Select add-on specifications that best fit you needs.</p>
    </td>
    </tr>
    <tr id="row83701240105118"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p3370040165116"><a name="p3370040165116"></a><a name="p3370040165116"></a>Instances</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p93701640145120"><a name="p93701640145120"></a><a name="p93701640145120"></a>Number of instances that will be created to match the selected add-on specifications. The number cannot be modified.</p>
    </td>
    </tr>
    <tr id="row4370840165119"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p937054045117"><a name="p937054045117"></a><a name="p937054045117"></a>Container</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p1437014065110"><a name="p1437014065110"></a><a name="p1437014065110"></a>CPU and memory quotas of the container allowed for the selected add-on specifications. The quotas cannot be modified.</p>
    </td>
    </tr>
    <tr id="row12370940175116"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p237044095117"><a name="p237044095117"></a><a name="p237044095117"></a>Notes</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p1493852310547"><a name="p1493852310547"></a><a name="p1493852310547"></a>Add-on precautions. Read the precautions before you proceed with the step.</p>
    </td>
    </tr>
    <tr id="row53701440125116"><td class="cellrowborder" valign="top" width="24%" headers="mcps1.2.3.1.1 "><p id="p8370124035118"><a name="p8370124035118"></a><a name="p8370124035118"></a>sub domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="76%" headers="mcps1.2.3.1.2 "><p id="p1837104015118"><a name="p1837104015118"></a><a name="p1837104015118"></a>A domain name server for a user-defined domain name. The format is a key-value pair. The key is a suffix of DNS domain name, and the value is one or more DNS IP addresses. For example, <strong id="b1715325674614"><a name="b1715325674614"></a><a name="b1715325674614"></a>acme.local -- 1.2.3.4,6.7.8.9</strong> means that DNS requests with the <strong id="b1115419566461"><a name="b1115419566461"></a><a name="b1115419566461"></a>.acme.local</strong> suffix are forwarded to a DNS listening at 1.2.3.4,6.7.8.9.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  After the preceding configurations are complete, click  **Install**.

    When the installation is complete, an instance of the add-on is installed on each node in the cluster.


## Configuring the Stub Domain for CoreDNS<a name="section5202157467"></a>

Cluster administrators can modify the ConfigMap for the CoreDNS Corefile to change how service discovery works. coredns has the ability to configure stub domains using the proxy plug-in.

Assume that a cluster administrator has a Consul DNS server located at 10.150.0.1 and all Consul names have the suffix  **.consul.local**. To configure Consul in coredns, the cluster administrator needs to write the following information in the coredns ConfigMap:

```
consul.local:5353 {
        errors
        cache 30
        proxy . 10.150.0.1
    }
```

ConfigMap after modification:

```
apiVersion: v1
data:
  Corefile: |-
    .:5353 {
        cache 30
        errors
        health
        kubernetes cluster.local in-addr.arpa ip6.arpa {
          pods insecure
          upstream /etc/resolv.conf
          fallthrough in-addr.arpa ip6.arpa
        }
        loadbalance round_robin
        prometheus 0.0.0.0:9153
        proxy . /etc/resolv.conf
        reload
    }

    consul.local:5353 {
        errors
        cache 30
        proxy . 10.150.0.1
    }
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
```

## How Does Domain Name Resolution Work in Kubernetes?<a name="section1860523212152"></a>

DNS policies can be set on a per-pod basis. Currently, Kubernetes supports four types of DNS policies:  **Default**,  **ClusterFirst**,  **ClusterFirstWithHostNet**, and  **None**. For details, see  [https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/). These policies are specified in the  **dnsPolicy**  field in the pod-specific.

-   **Default**: Pods inherit the name resolution configuration from the node that the pods run on. The custom upstream DNS server and the stub domain cannot be used together with this policy.
-   **ClusterFirst**: Any DNS query that does not match the configured cluster domain suffix, such as  **www.kubernetes.io**, is forwarded to the upstream name server inherited from the node. Cluster administrators may have extra stub domains and upstream DNS servers configured.
-   **ClusterFirstWithHostNet**: For pods running with hostNetwork, set its DNS policy  **ClusterFirstWithHostNet**.
-   **None**: It allows a pod to ignore DNS settings from the Kubernetes environment. All DNS settings are supposed to be provided using the  **dnsPolicy**  field in the pod-specific.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>-   Clusters of Kubernetes v1.10 and later support  **Default**,  **ClusterFirst**,  **ClusterFirstWithHostNet**, and  **None**. Clusters earlier than Kubernetes v1.10 support only  **Default**,  **ClusterFirst**, and  **ClusterFirstWithHostNet**.
>-   **Default**  is not the default DNS policy. If  **dnsPolicy**  is not explicitly specified,  **ClusterFirst**  is used.

**Routing**

**Without stub domain configurations**: Any query that does not match the configured cluster domain suffix, such as  **www.kubernetes.io**, is forwarded to the upstream DNS server inherited from the node.

**With stub domain configurations**: If stub domains and upstream DNS servers are configured, DNS queries are routed according to the following flow:

1.  The query is first sent to the DNS caching layer in coredns.
2.  From the caching layer, the suffix of the request is examined and then forwarded to the appropriate DNS, based on the following cases:
    -   Names with the cluster suffix, for example,  **.cluster.local**: The request is sent to coredns.

    -   Names with the stub domain suffix, for example,  **.acme.local**: The request is sent to the configured custom DNS resolver, listening for example at 1.2.3.4.
    -   Names that do not match the suffix \(for example,  **widget.com**\): The request is forwarded to the upstream DNS.


**Figure  1**  Routing<a name="fig7582181514118"></a>  
![](figures/routing.png "routing")

## Upgrading the Add-on<a name="section19566181513486"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Instance**  tab page, select the cluster and click  **Upgrade**  under  **coredns**.

    >![](public_sys-resources/icon-note.gif) **NOTE:** 
    >-   If the  **Upgrade**  button is unavailable, the current add-on is already up-to-date and no upgrade is required.
    >-   When the upgrade is complete, the original coredns version on cluster nodes will be replaced by the latest version.

2.  On the  **Basic Information**  page, select the add-on version and click  **Next: Configuration**.
3.  Configure the parameters listed in  [Table 2](#table1410658238). After the configuration is complete, click  **Upgrade**  to upgrade the coredns add-on.

    **Table  2**  Parameters for installing coredns

    <a name="table1410658238"></a>
    <table><thead align="left"><tr id="row10111254234"><th class="cellrowborder" valign="top" width="21.240000000000002%" id="mcps1.2.3.1.1"><p id="p1711053236"><a name="p1711053236"></a><a name="p1711053236"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="78.75999999999999%" id="mcps1.2.3.1.2"><p id="p10119522319"><a name="p10119522319"></a><a name="p10119522319"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1611957237"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.3.1.1 "><p id="p16111158235"><a name="p16111158235"></a><a name="p16111158235"></a>Add-on Specifications</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.75999999999999%" headers="mcps1.2.3.1.2 "><p id="p71111552319"><a name="p71111552319"></a><a name="p71111552319"></a>Concurrent domain name resolution ability. Select add-on specifications that best fit you needs.</p>
    </td>
    </tr>
    <tr id="row15111555233"><td class="cellrowborder" valign="top" width="21.240000000000002%" headers="mcps1.2.3.1.1 "><p id="p121114510237"><a name="p121114510237"></a><a name="p121114510237"></a>stub domain</p>
    </td>
    <td class="cellrowborder" valign="top" width="78.75999999999999%" headers="mcps1.2.3.1.2 "><p id="p2111453233"><a name="p2111453233"></a><a name="p2111453233"></a>A domain name server for a user-defined domain name. The format is a key-value pair. The key is a suffix of DNS domain name, and the value is one or more DNS IP addresses. For example, <strong id="b06297122457"><a name="b06297122457"></a><a name="b06297122457"></a>acme.local -- 1.2.3.4,6.7.8.9</strong> means that DNS requests with the <strong id="b1576053012450"><a name="b1576053012450"></a><a name="b1576053012450"></a>.acme.local</strong> suffix are forwarded to a DNS listening at 1.2.3.4,6.7.8.9.</p>
    </td>
    </tr>
    </tbody>
    </table>


## Uninstalling the Add-on<a name="section7582615184814"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Add-ons**. On the  **Add-on Instance**  tab page, select the cluster and click  **Uninstall**  under  **coredns**.
2.  In the dialog box that is displayed, click  **Yes**  to uninstall the add-on.

