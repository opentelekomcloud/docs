# Using Kubernetes In-Cluster DNS<a name="cce_01_0133"></a>

## Overview to Workload's DNS Configuration<a name="section119521837203315"></a>

Every Kubernetes cluster has a built-in DNS add-on \(Kube-DNS or CoreDNS\) to provide domain name resolution for workloads in the cluster. When handling a high concurrency of DNS queries, Kube-DNS/CoreDNS may encounter a performance bottleneck, that is, it may fail occasionally to fulfill DNS queries. There are cases when Kubernetes workloads initiate unnecessary DNS queries. This makes DNS overloaded if there are many concurrent DNS queries. Tuning DNS configuration for workloads will reduce the risks of DNS query failures to some extent.

For more information about the DNS, see  [CoreDNS \(System Resource Add-on, Mandatory\)](coredns-(system-resource-add-on-mandatory).md)  or  [Configuring High Availability of kube-dns/CoreDNS Using kubectl](configuring-high-availability-of-kube-dns-coredns-using-kubectl.md).

**Configuration Options in the DNS Resolver Configuration File for Linux Operating Systems**

Run the  **cat /etc/resolv.conf**  command on a Linux node or container to view the DNS resolver configuration file. The following is an example DNS resolver configuration of a container in a Kubernetes cluster:

```
nameserver 10.247.x.x
search default.svc.cluster.local svc.cluster.local cluster.local
options ndots:5
```

**Configuration Options**

-   **nameserver**: an IP address list of a name server that the resolver will query. If this parameter is set to 10.247.x.x, the resolver will query the Kube-DNS/CoreDNS. If this parameter is set to another IP address, the resolver will query a public cloud DNS or on-premises DNS server.
-   **search**: a search list for host-name lookup. When a domain name cannot be resolved, DNS queries will be attempted combining the domain name with each domain in the search list in turn until a match is found or all domains in the search list are tried. For CCE clusters, the search list is currently limited to three domains per container. When resolving a nonexistent domain name, eight DNS queries will be initiated because each domain in the search list will be queried, one for IPv4 and the other for IPv6.
-   **options**: options that allow certain internal resolver variables to be modified. Common options include timeout, attempts, and ndots. The options  **ndots:5**  means that if a domain name has fewer than 5 dots \(.\), DNS queries will be attempted by combining the domain name with each domain in the search list in turn. If no match is found after all the domains in the search list are tried, the domain name is then used for DNS query. If the domain name has 5 or more than 5 dots, it will be tried first for DNS query. In case that the domain name cannot be resolved, DNS queries will be attempted by combining the domain name with each domain in the search list in turn. For example, the domain name www.console.otc.t-systems.com has only 2 dots \(smaller than the value of ndots\), and therefore the sequence of DNS queries is as follows: www.console.otc.t-systems.default.svc.cluster.local, www.console.otc.t-systems.com.svc.cluster.local, www.console.otc.t-systems.com.cluster.local and www.console.otc.t-systems.com. This means that at least seven DNS queries will be initiated before the domain name is resolved into an IP address. It is clear that when many unnecessary DNS queries will be initiated to access an external domain name. There is room for improvement in workload's DNS configuration.

>![](/images/icon-note.gif) **NOTE:**   
>For more information about configuration options in the resolver configuration file used by Linux operating systems, visit  [http://man7.org/linux/man-pages/man5/resolv.conf.5.html](http://man7.org/linux/man-pages/man5/resolv.conf.5.html).  

-   **Configuration Options in the DNS Configuration File for Applications in Kubernetes Clusters**

    As explained earlier, applications may initiate unnecessary DNS queries in some scenarios. Kubernetes provides DNS-related configuration options for applications. The use of application's DNS configuration can effectively reduce unnecessary DNS queries in certain scenarios and improve service concurrency. In application configuration, there are two DNS-related fields:  **dnsPolicy**  and  **dnsConfig**.

    **dnsPolicy**

    The  **dnsPolicy**  field is used to configure a DNS policy for an application. The default value is  **ClusterFirst**. The DNS parameters in  **dnsConfig**  will be merged to the DNS file generated according to  **dnsPolicy**. The merge rules are later explained in  **dnsConfig**  description. Currently,  **dnsPolicy**  supports the following four values:

    -   ClusterFirst: CCE cluster's Kube-DNS/CoreDNS, which is cascaded with a public cloud DNS by default, is used for workloads. Containers can resolve both the cluster-internal domain names registered by the service and the external domain names exposed to public networks. The search list \(**search**  option\) and  **ndots: 5**  are present in the DNS configuration file. Therefore, when accessing an external domain name and a long cluster-internal domain name \(for example, kubernetes.default.svc.cluster.local\), the search list will usually be traversed first, resulting in at least six invalid DNS queries. The issue of invalid DNS queries disappears only when a short cluster-internal domain name \(for example, kubernetes\) is being accessed.
    -   **ClusterFirstWithHostNet**: By default, the DNS configuration file that the kubelet's  **--resolv-conf**  flag points to is configured for workloads running with hostNetwork, that is, a public cloud DNS is used for CCE clusters. If  **dnsPolicy**  is set to  **ClusterFirstWithHostNet**, Kube-DNS/CoreDNS is used for workloads, and container's DNS configuration file is the same as  **ClusterFirst**, eliminating the problem of invalid DNS queries.
    -   **Default**: Container's DNS configuration file is the DNS configuration file that the kubelet's  **--resolv-conf**  flag points to. In this case, a public cloud DNS is used for CCE clusters. Both  **search**  and  **options**  fields are left unspecified. This configuration can only resolve the external domain names registered with the Internet, and not cluster-internal domain names. This configuration is free from the issue of invalid DNS queries.
    -   **None**: This value is introduced since Kubernetes v1.9 \(Beta in v1.10\). If  **dnsPolicy**  is set to  **None**, the  **dnsConfig**  field must be specified because all DNS settings are supposed to be provided using the  **dnsConfig**  field.

    **dnsConfig**

    The  **dnsConfig**  field is used to configure DNS parameters for workloads. The configured parameters are merged to the DNS configuration file generated according to  **dnsPolicy**. If  **dnsPolicy**  is set to  **None**, the workload's DNS configuration file is specified by the  **dnsConfig**  field. If  **dnsPolicy**  is not set to  **None**, the DNS parameters configured in  **dnsConfig**  are added to the DNS configuration file generated according to  **dnsPolicy**.

    -   **nameservers**: a list of IP addresses that will be used as DNS servers. If workload's  **dnsPolicy**  is set to  **None**, the list must contain at least one IP address, otherwise this property is optional. The servers listed will be combined to the nameservers generated from the specified DNS policy in  **dnsPolicy**  with duplicate addresses removed.
    -   **searches**: a list of DNS search domains for hostname lookup in the Pod. This property is optional. When specified, the provided list will be merged into the search domain names generated from the chosen DNS policy in  **dnsPolicy**. Duplicate domain names are removed. Kubernetes allows for at most 6 search domains.
    -   **options**: an optional list of objects where each object may have a name property \(required\) and a value property \(optional\). The contents in this property will be merged to the options generated from the specified DNS policy in  **dnsPolicy**. Duplicate entries are removed.


## Configuration Examples<a name="section12309936102318"></a>

The following example describes how to configure DNS for workloads.

-   **Use Case 1: Using Kube-DNS/CoreDNS Built in Kubernetes Clusters**

    **Scenario**

    Kubernetes in-cluster Kube-DNS/CoreDNS is applicable to resolving only cluster-internal domain names or cluster-internal domain names + external domain names. This is the default DNS for workloads.

    **Example:**

    ```
    apiVersion: v1
    kind: Pod
    metadata:
      namespace: default
      name: dns-example
    spec:
      containers:
      - name: test
        image: nginx
      dnsPolicy: ClusterFirst
    ```

    Container's DNS configuration file:

    ```
    nameserver 10.247.3.10
    search default.svc.cluster.local svc.cluster.local cluster.local
    options ndots:5
    ```

-   **Use Case 2: Using a Public Cloud DNS**

    **Scenario**

    A public cloud DNS cannot resolve cluster-internal domain names and therefore is applicable to the scenario where workloads access only external domain names registered with the Internet.

    **Example:**

    ```
    apiVersion: v1
    kind: Pod
    metadata:
      namespace: default
      name: dns-example
    spec:
      containers:
      - name: test
        image: nginx
      dnsPolicy: Default//The DNS configuration file that the kubelet's --resolv-conf flag points to is used. In this case, a public cloud DNS is used for CCE clusters.
    ```

    Container's DNS configuration file:

    ```
    nameserver 10.125.x.x
    ```

-   **Use Case 3: Using Kube-DNS/CoreDNS for Workloads Running with hostNetwork**

    **Scenario**

    By default, a public cloud DNS is used for workloads running with hostNetwork. If workloads need to use Kube-DNS/CoreDNS, set dnsPolicy to ClusterFirstWithHostNet.

    **Example:**

    ```
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: nginx
    spec:
      template:
        metadata:
          labels:
            app: nginx
        spec:
          hostNetwork: true
          dnsPolicy: ClusterFirstWithHostNet
          containers:
          - name: nginx
            image: nginx:1.7.9
            ports:
            - containerPort: 80
    ```

    Container's DNS configuration file:

    ```
    nameserver 10.247.3.10
    search default.svc.cluster.local svc.cluster.local cluster.local
    options ndots:5
    ```

-   **Use Case 4: Customizing Application's DNS Configuration**

    **Scenario**

    You can flexibly customize the DNS configuration file for applications. Using  **dnsPolicy**  and  **dnsConfig**  together can address almost all scenarios, including the scenarios in which an on-premises DNS will be used, multiple DNSs will be cascaded, and DNS configuration options will be modified.

    **Example 1: Using Your On-Premises DNS**

    _Set  **dnsPolicy**  to  **None**  so application's DNS configuration file is generated based on  **dnsConfig**._

    ```
    apiVersion: v1
    kind: Pod
    metadata:
      namespace: default
      name: dns-example
    spec:
      containers:
      - name: test
        image: nginx
      dnsPolicy: "None"
      dnsConfig:
        nameservers:
        - 10.2.3.4 //IP address of your on-premises DNS
        searches:
        - ns1.svc.cluster.local
        - my.dns.search.suffix
        options:
        - name: ndots
          value: "2"
        - name: timeout
          value: "3"
    ```

    Container's DNS configuration file:

    ```
    nameserver 10.2.3.4
    search ns1.svc.cluster.local my.dns.search.suffix
    options timeout:3 ndots:2
    ```

    **Example 2: Modifying the ndots Option in the DNS Configuration File to Reduce Invalid DNS Queries**

    Set  **dnsPolicy**  to a value other than  **None**  so the DNS parameters configured in  **dnsConfig**  are added to the DNS configuration file generated based on  **dnsPolicy**.

    ```
    apiVersion: v1
    kind: Pod
    metadata:
      namespace: default
      name: dns-example
    spec:
      containers:
      - name: test
        image: nginx
      dnsPolicy: "ClusterFirst"
      dnsConfig:
        options:
        - name: ndots
          value: "2" //Changes the ndots:5 option in the DNS configuration file generated based on the ClusterFirst policy to ndots:2.
    ```

    Container's DNS configuration file:

    ```
    nameserver 10.247.3.10
    search default.svc.cluster.local svc.cluster.local cluster.local
    options ndots:2
    ```


