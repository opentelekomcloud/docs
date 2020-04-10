# Layer 7 Load Balancing \(Ingress\)<a name="cce_01_0094"></a>

Layer-7 load balancing uses enhanced load balancers. Compared with layer-4 load balancing, layer-7 load balancing additionally supports Uniform Resource Identifier \(URI\) configurations and  distributes access traffic  to services based on URIs. In addition, different functions are implemented based on various URIs.

The access address is in the format of <IP address of the  load balancer\>:<access port\>/defined URI, for example,  **10.117.117.117:80/helloworld**.

You can configure load balancers of public and private networks to implement layer-7 route forwarding on public networks and private networks \(intra-VPC networks\).

## Preparation<a name="section2042610683912"></a>

An  elastic load balancer  has been created on the management console.

1.  Log in to the management console and choose  **Network**  \>  **Elastic Load Balancing**  from the service list.
2.  Click  **Create Enhanced Load Balancer**  in the upper right corner. 

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The LoadBalancer access type allows workloads to be accessed from public networks through ELB. This access type has the following restrictions:  
>-   It is recommended that automatically created load balancers not be used by other resources. Otherwise, these load balancers cannot be completely deleted, causing residual resources.  
>-   Do not change the listener name for the load balancer in use. Otherwise, the load balancer cannot be accessed.  
>-   Do not add custom forwarding rules for the listener of the load balancer that is being used. As these forwarding rules are not added to the ingress for management on the  **Network**  page, they will be deleted when the ingress is updated.  

## Setting the Access Type on the Console<a name="section744117150366"></a>

You can set the service access type when creating a workload on the CCE console. The ingress-test workload is used as an example.

1.  Create a workload. For details, see  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md).
    -   If you have set the access type NodePort during workload creation, go to  [3](#li45981923161059).
    -   If the access type is not set during workload creation, go to  [2](#li248013365354).

2.  <a name="li248013365354"></a>\(Optional\) Set the access type NodePort.
    1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Network**.
    2.  On the  **Services**  tab page, click  **Create Service**. In the  **Select Type**  dialog box, select  **Node access \(node port\)**.
        -   **Service Name**: can be the same as the workload name.
        -   **Cluster Name**: Select the cluster for which you want to add a service.
        -   **Namespace**: Select a namespace for which you want to add a service.
        -   **Workload**: Click  **Select Workload**, select the name of the workload for which the access type NodePort is to be configured, and click  **OK**.
        -   **Service Affinity**
            -   **Cluster level**: External traffic is routed to all nodes in the cluster while masking clients' source IP addresses.
            -   **Node level**: External traffic is routed to the node where the workload targeted by the service is located, without masking clients' source IP addresses.

        -   **Port Settings**
            -   **Protocol**: Select a protocol used by the service.
            -   **Container Port**: a port on which the workload in the container image listens. The Nginx workload listens on port 80.
            -   **Access Port**: Specify a port to which container port will be mapped when the node's private IP address is used for accessing the workload. The port number range is 30000–32767. You are advised to select  **Automatically generated**.
                -   **Automatically generated**: The system automatically assigns a port number.
                -   **Specified port**: Specify a fixed node port. The port number range is 30000–32767. Ensure that the port is unique in a cluster.


    3.  Click  **Create**. The access type NodePort is successfully set.

3.  <a name="li45981923161059"></a>Add an ingress service.
    1.  In the navigation pane, choose  **Resource Management**  \>  **Network**.
    2.  On the  **Ingresses**  tab page, click  **Create Ingress**.
        -   **Ingress Name**: Specifies the name of an ingress, for example,  **ingress-demo**.
        -   **Cluster Name**: Select the cluster to which the ingress is to be added.
        -   **Namespace**: Select the namespace to which the ingress is to be added.
        -   **Elastic Load Balancer**: A load balancer automatically distributes Internet access traffic to multiple nodes running the workload. The selected or created load balancer must be in the same VPC as the current cluster, and it must match the load balancer type \(private or public network\).
            -   **Public network**: You can select an existing public network load balancer or have the system automatically create a new public network load balancer.

                If you have the system automatically create a public network load balancer, you can click  **Change Configuration**  to modify its name, EIP type, billing mode, and bandwidth.

            -   **Private network**: You can select an existing private network load balancer or have the system automatically create a new private network load balancer.

        -   **External Port**: Port number that is open to the ELB service address. The port number can be specified randomly.
        -   **Front-End Protocol**:  **HTTP**  and  **HTTPS**  are available. If you select HTTPS, select a key certificate accordingly. For details about the certificate format, see  [Certificate Format](https://docs.otc.t-systems.com/en-us/usermanual/elb/en-us_topic_0092382555.html).

            >![](public_sys-resources/icon-note.gif) **NOTE:**   
            >-   The key certificate  **ingress-test-secret.yaml**  is required only when HTTPS is selected. For details on how to create a key, see  [Creating a Secret](creating-a-secret.md).  
            >-   If there is already an HTTPS ingress for the chosen port on the load balancer, the certificate of the new HTTPS ingress must be the same as the certificate of the existing ingress. This means that a listener has only one certificate. If two certificates, each with a different ingress, are added to the same listener of the same load balancer, only the earliest certificate takes effect on the load balancer.  

        -   **Domain Name**: optional. It indicates the actual domain name. You are expected to buy the domain name and complete ICP filing for it. Ensure that the domain name can resolve the service address of the selected load balancer. If a domain name rule is configured, the domain name must always be used for access.
        -   **Route Configuration**
            -   **Route Matching Rule**:  **Prefix match**,  **Exact match**, and  **Regular expression**  are available.
                -   **Prefix match**: If the URL is set to  **/healthz**, the URL that meets the prefix can be accessed. For example, /healthz/v1 and /healthz/v2.
                -   **Exact match**: Only the URL that is the same as the specified URL can be accessed. For example, if the URL is set to  **/healthz**, only /healthz can be accessed.
                -   **Regular expression**: The URL rule can be set, for example,  **/\[A-Za-z0-9\_.-\]+/test**. All URLs that comply with this rule can be accessed, for example,  **/abcA9/test**  and  **/v1-Ab/test**. Two regular expression standards are supported: POSIX and Perl.

            -   **Mapping URL**: Access path to be registered, for example,  **/healthz**.
            -   **Service Name**: Select the service whose ingress is to be added. The service access type is intra-VPC access.
            -   **Service Port**: a port on which the container in the container image listens. For example, the defaultbackend application listens on port 8080 \(container port\).


4.  Click  **Create**.

    After the creation is complete, you can view the created ingress in the ingress list.

5.  Access the /healthz interface of the workload \(for example, defaultbackend\).

    Method 1: By using a load balancer's IP address \(The domain name cannot be configured for LoadBalancer services.\)

    1.  Obtain the access address of the /healthz interface of defaultbackend. The access address is in the format of <load balancer's IP address\>:<external port\><mapping URL\>. For example, 10.154.73.151:80/healthz.
    2.  Enter the URL of the /healthz interface, for example, http://10.154.73.151:80/healthz, in the address box of the browser to access the workload.

        **Figure  1**  Accessing the /healthz interface of defaultbackend<a name="fig17115192714367"></a>  
        ![](figures/accessing-the-healthz-interface-of-defaultbackend.png "accessing-the-healthz-interface-of-defaultbackend")

    Method 2: By using a domain name

    The following uses the domain name ingress.com configured in the ingress as an example.

    1.  Obtain the domain name and access address \(IP address and port number\) of the /iamwangbo interface of the ingress-demo.
    2.  Configure the <IP address in the access address\> <domain name\> in the  **C:\\Windows\\System32\\drivers\\etc\\hosts**  file on the local host.
    3.  Enter the http://<domain name\>:<access port\>/<mapping URL\> in the address box of the browser. For example, http://ingress.com:81/iamwangbo.


## Setting the Access Type Using kubectl<a name="section1944313158364"></a>

This section uses an Nginx workload as an example to describe how to implement ingress access using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

1.  Log in to the ECS on which the kubectl has been configured. For details, see  [Logging In to a Linux ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0013771089.html).
2.  Create the  **ingress-test-deployment.yaml**,  **ingress-test-svc.yaml**,  **ingress-test-ingress.yaml**, and  **ingress-test-secret.yaml**  files.

    The file names are user-defined.  **ingress-test-deployment.yaml**,  **ingress-test-svc.yaml**,  **ingress-test-ingress.yaml**, and  **ingress-test-secret.yaml**  are merely example file names.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   The key certificate  **ingress-test-secret.yam**l is required only when HTTPS is selected. For details on how to create a key, see  [Creating a Secret](creating-a-secret.md).  
    >-   If there is already an HTTPS ingress for the chosen port on the load balancer, the certificate of the new HTTPS ingress must be the same as the certificate of the existing ingress.  

    **vi ingress-test-deployment.yaml**

    ```
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: ingress-test-deployment
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: ingress-test-deployment
      strategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            app: ingress-test-deployment
        spec:
          containers:
            # Third-party public image. You can obtain the address by referring to the description or use your own image.
          - image: ingress  
            imagePullPolicy: Always
            name: ingress
            imagePullSecrets:
            - name: default-secret
    ```

    **vi ingress-test-svc.yaml**

    ```
    apiVersion: v1 
    kind: Service 
    metadata: 
      labels: 
        app: ingress-test-svc
      name: ingress-test-svc
    spec: 
      ports: 
      - name: service0 
        port: 8888
        protocol: TCP 
        targetPort: 8888       #If multiple ports need to be set, fill in the following information in sequence:
      - name: service1 
        port: 8081 
        protocol: TCP 
        targetPort: 8081
      selector: 
        app: ingress-test-deployment
      type:  NodePort
    ```

    **Table  1**  Key parameters

    <a name="table1819001615355"></a>
    <table><thead align="left"><tr id="row1519121663519"><th class="cellrowborder" valign="top" width="30.316968303169684%" id="mcps1.2.4.1.1"><p id="p18191161619356"><a name="p18191161619356"></a><a name="p18191161619356"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.088191180881914%" id="mcps1.2.4.1.2"><p id="p1191141613357"><a name="p1191141613357"></a><a name="p1191141613357"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.594840515948405%" id="mcps1.2.4.1.3"><p id="p1919116161353"><a name="p1919116161353"></a><a name="p1919116161353"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15191171618357"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="p5788113218236"><a name="p5788113218236"></a><a name="p5788113218236"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.088191180881914%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615000_p54093956"><a name="en-us_topic_0079615000_p54093956"></a><a name="en-us_topic_0079615000_p54093956"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p167881320237"><a name="p167881320237"></a><a name="p167881320237"></a>Access port mapped to the cluster-internal IP address. The value ranges from 1 to 65535.</p>
    </td>
    </tr>
    <tr id="row81941516153513"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615000_p11039195"><a name="en-us_topic_0079615000_p11039195"></a><a name="en-us_topic_0079615000_p11039195"></a>protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.088191180881914%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615000_p17699892"><a name="en-us_topic_0079615000_p17699892"></a><a name="en-us_topic_0079615000_p17699892"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p835181810259"><a name="p835181810259"></a><a name="p835181810259"></a>IP protocol used by the port. The value can be <strong id="b11597432782"><a name="b11597432782"></a><a name="b11597432782"></a>TCP</strong> or <strong id="b1361120321816"><a name="b1361120321816"></a><a name="b1361120321816"></a>UDP</strong>.</p>
    </td>
    </tr>
    <tr id="row201957167350"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0079615000_p53639231"><a name="en-us_topic_0079615000_p53639231"></a><a name="en-us_topic_0079615000_p53639231"></a>targetPort</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.088191180881914%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615000_p8117426"><a name="en-us_topic_0079615000_p8117426"></a><a name="en-us_topic_0079615000_p8117426"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p1262218433513"><a name="p1262218433513"></a><a name="p1262218433513"></a>Container port on which the application listens. The value ranges from 1 to 65535.</p>
    </td>
    </tr>
    <tr id="row02694357138"><td class="cellrowborder" valign="top" width="30.316968303169684%" headers="mcps1.2.4.1.1 "><p id="p6716134816295"><a name="p6716134816295"></a><a name="p6716134816295"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.088191180881914%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0079615000_p18968549"><a name="en-us_topic_0079615000_p18968549"></a><a name="en-us_topic_0079615000_p18968549"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p13717148202913"><a name="p13717148202913"></a><a name="p13717148202913"></a>Uses the NodePort access type to connect to the load balancer. NodePort indicates the private IP address of a node.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **vi ingress-test-ingress.yaml**

    -   Automatically creating load balancer

        ```
        apiVersion: extensions/v1beta1 
        kind: Ingress 
        metadata: 
          annotations: 
            kubernetes.io/elb.subnet-id: 29a0567e-96f1-4227-91cc-64f54d0b064d
            kubernetes.io/elb.autocreate: "{\"type\":\"public\",\"bandwidth_name\":\"cce-bandwidth-1551163379627\",\"bandwidth_chargemode\":\"bandwidth\",\"bandwidth_size\":5,\"bandwidth_sharetype\":\"PER\",\"eip_type\":\"5_bgp\",\"name\":\"james\"}"
            kubernetes.io/elb.port: "80"
            kubernetes.io/ingress.class: cce
          name: ingress-test-ingress
        spec:
          tls:
          - secretName: ingress-test-secret
          rules: 
          - http: 
              paths: 
              - backend: 
                  serviceName: ingress-test-svc
                  servicePort: 8888
                property:
                  ingress.beta.kubernetes.io/url-match-mode: EQUAL_TO
                path: "/healthz"
            host: ingress.com
        ```

    -   Using existing load balancer

        ```
        apiVersion: extensions/v1beta1 
        kind: Ingress 
        metadata: 
          annotations: 
            kubernetes.io/elb.id: f7891f9a-49f2-4ee2-b1ae-f019cd84eb4f
            kubernetes.io/elb.ip: 192.168.0.39
            kubernetes.io/elb.subnet-id: 29a0567e-96f1-4227-91cc-64f54d0b064d
            kubernetes.io/elb.port: "80"
            kubernetes.io/ingress.class: cce
          name: ingress-test-ingress
        spec:
          tls:
          - secretName: ingress-test-secret
          rules: 
          - http: 
              paths: 
              - backend: 
                  serviceName: ingress-test-svc
                  servicePort: 8888
                property:
                  ingress.beta.kubernetes.io/url-match-mode: EQUAL_TO
                path: "/healthz"
            host: ingress.com
        ```

        **Table  2**  Key parameters

        <a name="table1732315519222"></a>
        <table><thead align="left"><tr id="row43239510228"><th class="cellrowborder" valign="top" width="29.727027297270276%" id="mcps1.2.4.1.1"><p id="p3323185142214"><a name="p3323185142214"></a><a name="p3323185142214"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="18.678132186781323%" id="mcps1.2.4.1.2"><p id="p1632315162219"><a name="p1632315162219"></a><a name="p1632315162219"></a>Type</p>
        </th>
        <th class="cellrowborder" valign="top" width="51.594840515948405%" id="mcps1.2.4.1.3"><p id="p2323105202212"><a name="p2323105202212"></a><a name="p2323105202212"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row1932315519221"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p11323551220"><a name="p11323551220"></a><a name="p11323551220"></a>kubernetes.io/elb.id</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p43232502212"><a name="p43232502212"></a><a name="p43232502212"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p1532419502210"><a name="p1532419502210"></a><a name="p1532419502210"></a>Optional. This parameter is mandatory if an existing load balancer is used.</p>
        <p id="p1832435142216"><a name="p1832435142216"></a><a name="p1832435142216"></a>It indicates the ID of an enhanced load balancer.</p>
        </td>
        </tr>
        <tr id="row19324185132210"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p143241054227"><a name="p143241054227"></a><a name="p143241054227"></a>kubernetes.io/elb.ip</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p63241755223"><a name="p63241755223"></a><a name="p63241755223"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p1232410519221"><a name="p1232410519221"></a><a name="p1232410519221"></a>Optional. Do not specify this parameter if an enhanced load balancer will be automatically created.</p>
        <p id="p123246513225"><a name="p123246513225"></a><a name="p123246513225"></a>This parameter indicates the service address of an enhanced load balancer. The value can be the public IP address of a public network load balancer or the private IP address of a private network load balancer.</p>
        </td>
        </tr>
        <tr id="row113242512217"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p1332415102211"><a name="p1332415102211"></a><a name="p1332415102211"></a>kubernetes.io/elb.subnet-id</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p16324185192216"><a name="p16324185192216"></a><a name="p16324185192216"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p6324185202213"><a name="p6324185202213"></a><a name="p6324185202213"></a>Optional. This parameter is mandatory only if a load balancer will be automatically created. For clusters of v1.11.7-r2 or later, this parameter can be left unspecified.</p>
        </td>
        </tr>
        <tr id="row14324115112219"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p163241552218"><a name="p163241552218"></a><a name="p163241552218"></a>kubernetes.io/elb.autocreate</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p163247517229"><a name="p163247517229"></a><a name="p163247517229"></a><a href="#table19417184671919">elb.autocreate</a> object</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p03246532210"><a name="p03246532210"></a><a name="p03246532210"></a>Optional. This parameter is mandatory if a public network load balancer will be automatically created. Set this parameter to the EIP of the enhanced load balancer that is automatically created. This parameter is also mandatory if a private network load balancer will be automatically created.</p>
        <p id="p13324858222"><a name="p13324858222"></a><a name="p13324858222"></a><strong id="b122043194200"><a name="b122043194200"></a><a name="b122043194200"></a>Example:</strong></p>
        <a name="ul16324853220"></a><a name="ul16324853220"></a><ul id="ul16324853220"><li>Value for a public network load balancer that is automatically created: "{\"type\":\"public\",\"bandwidth_name\":\"cce-bandwidth-1551163379627\",\"bandwidth_chargemode\":\"bandwidth\",\"bandwidth_size\":5,\"bandwidth_sharetype\":\"PER\",\"eip_type\":\"5_bgp\",\"name\":\"james\"}"</li><li>Value for a private network load balancer that is automatically created: "{\"type\":\"inner\"}"</li></ul>
        </td>
        </tr>
        <tr id="row332514515229"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p232519512211"><a name="p232519512211"></a><a name="p232519512211"></a>kubernetes.io/elb.port</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p173251458226"><a name="p173251458226"></a><a name="p173251458226"></a>Integer</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p93251554223"><a name="p93251554223"></a><a name="p93251554223"></a>Mandatory. External port registered with the address of the LoadBalancer service.</p>
        </td>
        </tr>
        <tr id="row1432518511224"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p1432565182214"><a name="p1432565182214"></a><a name="p1432565182214"></a>kubernetes.io/ingress.class</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p1232514542215"><a name="p1232514542215"></a><a name="p1232514542215"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p13251456223"><a name="p13251456223"></a><a name="p13251456223"></a>By default, <strong id="b1435202252315"><a name="b1435202252315"></a><a name="b1435202252315"></a>cce</strong> indicates that an enhanced load balancer will be used, and <strong id="b18131115472313"><a name="b18131115472313"></a><a name="b18131115472313"></a>nginx</strong> indicates that the nginx-ingress add-on will be enabled. This parameter is mandatory when an ingress is created by calling the API.</p>
        </td>
        </tr>
        <tr id="row143251551229"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p18325951228"><a name="p18325951228"></a><a name="p18325951228"></a>tls</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p1832513582216"><a name="p1832513582216"></a><a name="p1832513582216"></a>Array of strings</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p53262562220"><a name="p53262562220"></a><a name="p53262562220"></a>Optional. This parameter is mandatory if the front-end protocol is HTTPS.</p>
        </td>
        </tr>
        <tr id="row6326185152213"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p5326145202219"><a name="p5326145202219"></a><a name="p5326145202219"></a>secretName</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p5326135162216"><a name="p5326135162216"></a><a name="p5326135162216"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p1732645172213"><a name="p1732645172213"></a><a name="p1732645172213"></a>Optional. This parameter is required when HTTPS is used. Set this parameter to the name of the created key certificate.</p>
        </td>
        </tr>
        <tr id="row33265552211"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p1432685102213"><a name="p1432685102213"></a><a name="p1432685102213"></a>serviceName</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p1632617511229"><a name="p1632617511229"></a><a name="p1632617511229"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p17326135102219"><a name="p17326135102219"></a><a name="p17326135102219"></a>Name of the ingress-test-svc.yaml service.</p>
        </td>
        </tr>
        <tr id="row1232616516229"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p16326052225"><a name="p16326052225"></a><a name="p16326052225"></a>servicePort</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p23264582215"><a name="p23264582215"></a><a name="p23264582215"></a>Integer</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p53261152221"><a name="p53261152221"></a><a name="p53261152221"></a>Container port, that is, targetPort in the ingress-test-svc.yaml.</p>
        </td>
        </tr>
        <tr id="row1732620510228"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p12326195152216"><a name="p12326195152216"></a><a name="p12326195152216"></a>ingress.beta.kubernetes.io/url-match-mode</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p1232675172211"><a name="p1232675172211"></a><a name="p1232675172211"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p16327755228"><a name="p16327755228"></a><a name="p16327755228"></a>Route matching policy. The options are <strong id="b349312417285"><a name="b349312417285"></a><a name="b349312417285"></a>EQUAL_TO</strong> (exact matching), <strong id="b1764564632813"><a name="b1764564632813"></a><a name="b1764564632813"></a>STARTS_WITH</strong> (prefix matching), and <strong id="b37813537287"><a name="b37813537287"></a><a name="b37813537287"></a>REGEX</strong> (regular expression matching).</p>
        </td>
        </tr>
        <tr id="row19327205202214"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p83279511221"><a name="p83279511221"></a><a name="p83279511221"></a>path</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p932711582211"><a name="p932711582211"></a><a name="p932711582211"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p173278515229"><a name="p173278515229"></a><a name="p173278515229"></a>User-defined route.</p>
        </td>
        </tr>
        <tr id="row16327451221"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p832714513227"><a name="p832714513227"></a><a name="p832714513227"></a>host</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p1532718517223"><a name="p1532718517223"></a><a name="p1532718517223"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p53272572218"><a name="p53272572218"></a><a name="p53272572218"></a>Optional. This parameter specifies the domain name.</p>
        </td>
        </tr>
        </tbody>
        </table>

        **Table  3**  elb.autocreate parameters

        <a name="table19417184671919"></a>
        <table><thead align="left"><tr id="row14418174611912"><th class="cellrowborder" valign="top" width="29.727027297270276%" id="mcps1.2.4.1.1"><p id="p1141924611199"><a name="p1141924611199"></a><a name="p1141924611199"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="18.678132186781323%" id="mcps1.2.4.1.2"><p id="p1641911466191"><a name="p1641911466191"></a><a name="p1641911466191"></a>Type</p>
        </th>
        <th class="cellrowborder" valign="top" width="51.594840515948405%" id="mcps1.2.4.1.3"><p id="p1941920463197"><a name="p1941920463197"></a><a name="p1941920463197"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row194191846181915"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p152321411112318"><a name="p152321411112318"></a><a name="p152321411112318"></a>name</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p7419646171920"><a name="p7419646171920"></a><a name="p7419646171920"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p87791494919"><a name="p87791494919"></a><a name="p87791494919"></a>Name of the load balancer that is automatically created.</p>
        <p id="p9912132016296"><a name="p9912132016296"></a><a name="p9912132016296"></a>The value is a string of 1 to 64 characters that consist of letters, digits, underscores (_), and hyphens (-).</p>
        </td>
        </tr>
        <tr id="row142064681919"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p20862285225"><a name="p20862285225"></a><a name="p20862285225"></a>type</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p8420746101918"><a name="p8420746101918"></a><a name="p8420746101918"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p4703183013491"><a name="p4703183013491"></a><a name="p4703183013491"></a>Network type of the load balancer.</p>
        <a name="ul152311045124913"></a><a name="ul152311045124913"></a><ul id="ul152311045124913"><li><strong id="b83121327103010"><a name="b83121327103010"></a><a name="b83121327103010"></a>public</strong>: public network load balancer.</li><li><strong id="b9790229123010"><a name="b9790229123010"></a><a name="b9790229123010"></a>inner</strong>: private network load balancer.</li></ul>
        </td>
        </tr>
        <tr id="row194201046151910"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p128042817221"><a name="p128042817221"></a><a name="p128042817221"></a>bandwidth_name</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p1142084619195"><a name="p1142084619195"></a><a name="p1142084619195"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p6964103318220"><a name="p6964103318220"></a><a name="p6964103318220"></a>Bandwidth name. The default value is <strong id="b20740133311301"><a name="b20740133311301"></a><a name="b20740133311301"></a>cce-bandwidth-******</strong>.</p>
        <p id="p1236952875020"><a name="p1236952875020"></a><a name="p1236952875020"></a>The value is a string of 1 to 64 characters that consist of letters, digits, underscores (_), hyphens (-), and periods (.).</p>
        </td>
        </tr>
        <tr id="row942194619199"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p77502811221"><a name="p77502811221"></a><a name="p77502811221"></a>bandwidth_chargemode</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p11421446191914"><a name="p11421446191914"></a><a name="p11421446191914"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p3178181495216"><a name="p3178181495216"></a><a name="p3178181495216"></a>Bandwidth billing mode.</p>
        <a name="ul567215235528"></a><a name="ul567215235528"></a><ul id="ul567215235528"><li><strong id="b0118194493018"><a name="b0118194493018"></a><a name="b0118194493018"></a>bandwidth</strong>: billed by bandwidth.</li><li><strong id="b568054619301"><a name="b568054619301"></a><a name="b568054619301"></a>traffic</strong>: billed by traffic.</li></ul>
        </td>
        </tr>
        <tr id="row124211046101910"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p187492819229"><a name="p187492819229"></a><a name="p187492819229"></a>bandwidth_size</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p114229463196"><a name="p114229463196"></a><a name="p114229463196"></a>Integer</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p12958233152218"><a name="p12958233152218"></a><a name="p12958233152218"></a>Bandwidth size. Set this parameter based on the bandwidth range supported by the region. For details, see the <strong id="b65971949163614"><a name="b65971949163614"></a><a name="b65971949163614"></a>size</strong> field in <strong id="b1859764983610"><a name="b1859764983610"></a><a name="b1859764983610"></a>Table 4 Description of the bandwidth field</strong> in <a href="https://docs.otc.t-systems.com/en-us/api/vpc/en-us_topic_0020090596.html" target="_blank" rel="noopener noreferrer">Assigning an EIP</a>.</p>
        </td>
        </tr>
        <tr id="row1942224601917"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p16731228202214"><a name="p16731228202214"></a><a name="p16731228202214"></a>bandwidth_sharetype</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p84221246111913"><a name="p84221246111913"></a><a name="p84221246111913"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p188864421731"><a name="p188864421731"></a><a name="p188864421731"></a>Bandwidth sharing mode.</p>
        <a name="ul51872412"></a><a name="ul51872412"></a><ul id="ul51872412"><li><strong id="b168441719143117"><a name="b168441719143117"></a><a name="b168441719143117"></a>PER</strong>: dedicated bandwidth.</li><li><strong id="b1669953416312"><a name="b1669953416312"></a><a name="b1669953416312"></a>WHOLE</strong>: shared bandwidth.</li></ul>
        </td>
        </tr>
        <tr id="row1242219461193"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="p1972102872220"><a name="p1972102872220"></a><a name="p1972102872220"></a>eip_type</p>
        </td>
        <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="p132201811174611"><a name="p132201811174611"></a><a name="p132201811174611"></a>String</p>
        </td>
        <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="p11956103372218"><a name="p11956103372218"></a><a name="p11956103372218"></a>EIP type. Set this parameter based on the EIP types supported by ELB. For details, see the <strong id="b1465120586363"><a name="b1465120586363"></a><a name="b1465120586363"></a>type</strong> field in <strong id="b1565116582363"><a name="b1565116582363"></a><a name="b1565116582363"></a>Table 3 Description of the publicip field</strong> in <a href="https://docs.otc.t-systems.com/en-us/api/vpc/en-us_topic_0020090596.html" target="_blank" rel="noopener noreferrer">Assigning an EIP</a>.</p>
        </td>
        </tr>
        </tbody>
        </table>

        **vi ingress-test-secret.yaml**

        ```
        apiVersion: v1
        data:
          tls.crt: LS0******tLS0tCg==
          tls.key: LS0tL******0tLS0K
        kind: Secret
        metadata:
          annotations:
            description: test for ingressTLS secrets
          name: ingress-test-secret
          namespace: default
        type: IngressTLS
        ```

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >In the preceding command output,  **tls.crt**  and  **tls.key**  are only examples. Replace them with the actual keys.  


3.  Create a workload.

    **kubectl create -f  ingress-test-deployment.yaml**

    If the following information is displayed, the workload is being created.

    ```
    deployment "ingress-test-deployment" created
    ```

    **kubectl get po**

    If information similar to the following is displayed, the workload has been created successfully.

    ```
    NAME                            READY     STATUS             RESTARTS   AGE
    ingress-test-1627801589-r64pk   1/1       Running            0          6s
    ```

4.  Create a secret.

    **kubectl create -f  **ingress-test-secret.yaml****

    If information similar to the following is displayed, the secret is being created.

    ```
    secret "ingress-test-secret" created
    ```

    **kubectl get secrets**

    If information similar to the following is displayed, the secret has been created successfully.

    ```
    NAME                         TYPE                                  DATA      AGE
    dash-dashboard               Opaque                                0         7d
    dash-dashboard-token-f2nbk   kubernetes.io/service-account-token   3         7d
    default-secret               kubernetes.io/dockerconfigjson        1         8d
    default-token-wfn4l          kubernetes.io/service-account-token   3         8d
    paas.elb                     cfe/secure-opaque                     2         8d
    ingress-test-secret          IngressTLS                            2         13s
    ```

5.  Create a service.

    **kubectl create -f ingress-test-svc.yaml**

    If information similar to the following is displayed, the service has been created.

    ```
    service "ingress-test-svc" created
    ```

    **kubectl get svc**

    If information similar to the following is displayed, the service has been created successfully.

    ```
    NAME            TYPE          CLUSTER-IP        EXTERNAL-IP   PORT(S)          AGE
    ingress-test    NodePort      10.247.189.207    <none>       8080:30532/TCP   5s
    kubernetes      ClusterIP     10.247.0.1        <none>        443/TCP          3d
    ```

    **kubectl create -f ingress-test-ingress.yaml**

    If information similar to the following is displayed, the service has been created.

    ```
    ingress "ingress-test-ingress" created
    ```

    **kubectl get ingress**

    If information similar to the following is displayed, the ingress service has been created successfully and the workload is accessible.

    ```
    NAME             HOSTS     ADDRESS          PORTS   AGE
    ingress-test     *         10.154.76.63     80      10s
    ```

6.  Enter  **http://10.154.76.63/healthz**  in the address box of the browser.

    **10.154.76.63**  indicates the IP address of the unified load balancer.

    **Figure  2**  Accessing healthz<a name="fig1526153112115"></a>  
    ![](figures/accessing-healthz.png "accessing-healthz")


## Updating an Ingress<a name="section1071722525415"></a>

After adding an ingress, you can update its port, domain name, and route configuration. The procedure is as follows:

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Network**. On the  **Ingresses**  tab page, filter ingresses by cluster and namespace, and click  **Update**  for the ingress to be updated.
2.  On the  **Update Ingress**  page, set the following parameters as follows:
    -   **External Port**: Port number that is open to the ELB service address. The port number can be specified randomly.
    -   **Domain Name**: optional. It indicates the actual domain name. You are expected to buy the domain name and complete ICP filing for it. Ensure that the domain name can resolve the service address of the selected load balancer. If a domain name rule is configured, the domain name must always be used for access.
    -   **Route Configuration**: You can click  **Add Ingress Rule**  to add a rule.
        -   **Route Matching Rule**:  **Prefix match**,  **Exact match**, and  **Regular expression**  are available.
            -   **Prefix match**: If the URL is set to  **/healthz**, the URL that meets the prefix can be accessed. For example, /healthz/v1 and /healthz/v2.
            -   **Exact match**: Only the URL that is the same as the specified URL can be accessed. For example, if the URL is set to  **/healthz**, only /healthz can be accessed.
            -   **Regular expression**: The URL rule can be set, for example,  **/\[A-Za-z0-9\_.-\]+/test**. All URLs that comply with this rule can be accessed, for example,  **/abcA9/test**  and  **/v1-Ab/test**. Two regular expression standards are supported: POSIX and Perl.

        -   **Mapping URL**: Access path to be registered, for example: /healthz.
        -   **Service Name**: Select the service whose ingress is to be added. The service access type is intra-VPC access.
        -   **Service Port**: a port on which the container in the container image listens. For example, the defaultbackend workload listens on port 8080 \(container port\).

3.  Click  **Submit**. The ingress will be updated for the workload.

