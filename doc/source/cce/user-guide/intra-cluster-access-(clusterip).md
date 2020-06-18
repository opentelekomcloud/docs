# Intra-Cluster Access \(ClusterIP\)<a name="cce_01_0011"></a>

A workload is accessible to other workloads in the same cluster through the use of an internal domain name.

A cluster-internal domain name format is  _<User-defined service name\>_._<Namespace of the workload\>_**.svc.cluster.local:<port number\>**, for example,  **nginx.default.svc.cluster.local:80**.

[Figure 1](#fig192245420557)  shows the mapping relationships between access channels, container ports, and access ports.

**Figure  1**  Intra-cluster access \(ClusterIP\)<a name="fig192245420557"></a>  
![](figures/intra-cluster-access-(clusterip).png "intra-cluster-access-(clusterip)")

## Setting the Access Type on the Console<a name="section363413419562"></a>

You can set the service access type when creating a workload on the CCE console.

1.  In the  **Set Application Access**  step of  [Creating a Deployment](creating-a-deployment.md)  or  [Creating a StatefulSet](creating-a-statefulset.md), click  **Add Service**  and set the following parameters:
    -   **Access Type**: Select  **Intra-cluster access \(cluster IP\)**.
    -   **Service Name**: can be the same as the workload name.
    -   **Port Settings**
        -   **Protocol**: a protocol used by the service.
        -   **Container Port**: a port on which the workload listens. The nginx application listens on port 80.
        -   **Access Port**: a port mapped to the container port at the cluster-internal IP address. The workload can be accessed at <cluster-internal IP address\>:<access port\>. The port number range is 1–65535.

2.  <a name="li090492615184"></a>On the  **Add Service**  page, click  **OK**. On the workload creation page, click  **Next**. On the  **Configure Advanced Settings**  page, click  **Create**.
3.  <a name="li16964121448"></a>Click  **View Deployment Details**  or  **View StatefulSet Details**. On the  **Services**  tab page, obtain the access address, for example, 10.247.74.100:2.
4.  Log in to any node in the cluster where the workload is located. For details, see  [Logging In to a Linux ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0013771089.html).
5.  Run the  **curl**  command to verify whether access to the workload is successful. You can perform the verification by using the IP address or domain name.
    -   By using the IP address

        **curl **_10.247.74.100:2_

        10.247.74.100:2 is the access address obtained in  [Step 3](#li090492615184).

        If information similar to the following is displayed, the workload is accessible.

        ```
        <html>
        <head>
        <title>Welcome to nginx!</title>
        <style>
            body {
                width: 35em;
                margin: 0 auto;
                font-family: Tahoma, Verdana, Arial, sans-serif;
            }
        </style>
        </head>
        <body>
        <h1>Welcome to nginx!</h1>
        <p>If you see this page, the nginx web server is successfully installed and
        working. Further configuration is required.</p>
        
        <p>For online documentation and support please refer to
        <a href="http://nginx.org/">nginx.org</a>.<br/>
        Commercial support is available at
        <a href="http://nginx.com/">nginx.com</a>.</p>
        
        <p><em>Thank you for using nginx.</em></p>
        </body>
        </html>
        ```

    -   By using the domain name

        **curl** _nginx.default.svc.cluster.local:2_

        _nginx.default.svc.cluster.local_  is the domain name obtained in  [Step 3](#li16964121448).

        If information similar to the following is displayed, the workload is accessible.

        ```
        <html>
        <head>
        <title>Welcome to nginx!</title>
        <style>
            body {
                width: 35em;
                margin: 0 auto;
                font-family: Tahoma, Verdana, Arial, sans-serif;
            }
        </style>
        </head>
        <body>
        <h1>Welcome to nginx!</h1>
        <p>If you see this page, the nginx web server is successfully installed and
        working. Further configuration is required.</p>
        
        <p>For online documentation and support please refer to
        <a href="http://nginx.org/">nginx.org</a>.<br/>
        Commercial support is available at
        <a href="http://nginx.com/">nginx.com</a>.</p>
        
        <p><em>Thank you for using nginx.</em></p>
        </body>
        </html>
        ```



## Setting the Access Type Using kubectl<a name="section912410191053"></a>

You can run kubectl commands to set the service access type. This section uses an Nginx workload as an example to describe how to implement intra-cluster access using kubectl.

**Prerequisites**

The ECS where the kubectl client runs has been connected to your cluster. For details, see  [Connecting to a Kubernetes Cluster Using kubectl](connecting-to-a-kubernetes-cluster-using-kubectl.md).

**Procedure**

1.  Log in to the ECS on which the kubectl commands have been configured. For details, see  [Logging In to a Linux ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0013771089.html).
2.  Create and edit the  **nginx-deployment.yaml**  and  **nginx-clusterip-svc.yaml**  files.

    The file names are user-defined.  **nginx-deployment.yaml**  and  **nginx-clusterip-svc.yaml**  are merely example file names.

    **vi nginx-deployment.yaml**

    ```
    apiVersion: extensions/v1beta1
    kind: Deployment
    metadata:
      name: nginx
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: nginx
      strategy:
        type: RollingUpdate
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - image: nginx 
            imagePullPolicy: Always
            name: nginx
          imagePullSecrets:
          - name: default-secret
    ```

    **vi nginx-ClusterIp-svc.yaml**

    ```
    apiVersion: v1
    kind: Service
    metadata:
      labels:
        app: nginx
      name: nginx-clusterip
    spec:
      ports:
      - name: service0
        port: 2
        protocol: TCP
        targetPort: 80
      selector:
        app: nginx
      type: ClusterIP
    ```

    **Table  1**  Key parameters

    <a name="table56443210447"></a>
    <table><thead align="left"><tr id="row157011325448"><th class="cellrowborder" valign="top" width="19.009999999999998%" id="mcps1.2.4.1.1"><p id="p127013213445"><a name="p127013213445"></a><a name="p127013213445"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.43%" id="mcps1.2.4.1.2"><p id="p070113234410"><a name="p070113234410"></a><a name="p070113234410"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="62.56%" id="mcps1.2.4.1.3"><p id="p870832124415"><a name="p870832124415"></a><a name="p870832124415"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row19708321446"><td class="cellrowborder" valign="top" width="19.009999999999998%" headers="mcps1.2.4.1.1 "><p id="p2705327445"><a name="p2705327445"></a><a name="p2705327445"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.43%" headers="mcps1.2.4.1.2 "><p id="p37133244415"><a name="p37133244415"></a><a name="p37133244415"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.56%" headers="mcps1.2.4.1.3 "><p id="p164654108492"><a name="p164654108492"></a><a name="p164654108492"></a>Port at which the service is exposed, that is, the access port on the CCE console.</p>
    </td>
    </tr>
    <tr id="row13718321449"><td class="cellrowborder" valign="top" width="19.009999999999998%" headers="mcps1.2.4.1.1 "><p id="p971532194415"><a name="p971532194415"></a><a name="p971532194415"></a>targetPort</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.43%" headers="mcps1.2.4.1.2 "><p id="p127153274418"><a name="p127153274418"></a><a name="p127153274418"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.56%" headers="mcps1.2.4.1.3 "><p id="p571173210447"><a name="p571173210447"></a><a name="p571173210447"></a>Container port on the CCE console.</p>
    </td>
    </tr>
    <tr id="row1671532144412"><td class="cellrowborder" valign="top" width="19.009999999999998%" headers="mcps1.2.4.1.1 "><p id="p127115322447"><a name="p127115322447"></a><a name="p127115322447"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.43%" headers="mcps1.2.4.1.2 "><p id="p1147421514515"><a name="p1147421514515"></a><a name="p1147421514515"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="62.56%" headers="mcps1.2.4.1.3 "><p id="p1962118433512"><a name="p1962118433512"></a><a name="p1962118433512"></a>Access type on the CCE console. The options are as follows:</p>
    <a name="ul1735917148524"></a><a name="ul1735917148524"></a><ul id="ul1735917148524"><li>ClusterIP</li><li>NodePort</li><li>LoadBalancer</li></ul>
    <p id="p1262218433513"><a name="p1262218433513"></a><a name="p1262218433513"></a>The default value is <strong id="b4887183010483"><a name="b4887183010483"></a><a name="b4887183010483"></a>ClusterIP</strong>, indicating the cluster-internal IP address.</p>
    </td>
    </tr>
    </tbody>
    </table>

3.  Create a workload.

    **kubectl create -f nginx-deployment.yaml**

    If information similar to the following is displayed, the workload is being created.

    ```
    deployment "nginx" created
    ```

    **kubectl get po**

    If information similar to the following is displayed, the workload is running.

    ```
    NAME                     READY     STATUS             RESTARTS   AGE
    etcd-0                   0/1       ImagePullBackOff   0          27m
    icagent-m9dkt            0/0       Running            0          3d
    nginx-2601814895-znhbr   1/1       Running            0          15s
    ```

4.  Create a service.

    **kubectl create -f nginx-ClusterIp-svc.yaml**

    If information similar to the following is displayed, the service is being created.

    ```
    service "nginx-clusterip" created
    ```

    **kubectl get svc**

    If information similar to the following is displayed, the service has been created, and a cluster-internal IP address has been assigned to the service.

    ```
    NAME              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
    etcd-svc          ClusterIP   None             <none>        3120/TCP   30m
    kubernetes        ClusterIP   10.247.0.1       <none>        443/TCP    3d
    nginx-clusterip   ClusterIP   10.247.200.134   <none>        80/TCP     20s
    ```

5.  Log in to any node in the cluster where the workload is located. For details, see  [Logging In to a Linux ECS](https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0013771089.html).
6.  Run the  **curl**  command to check whether the workload is accessible. You can perform the verification by using the IP address or domain name.
    -   By using the  IP address

        **curl** _10.247.200.134__:2_

        If information similar to the following is displayed, the workload is accessible.

        ```
        <html>
        <head>
        <title>Welcome to nginx!</title>
        <style>
            body {
                width: 35em;
                margin: 0 auto;
                font-family: Tahoma, Verdana, Arial, sans-serif;
            }
        </style>
        </head>
        <body>
        <h1>Welcome to nginx!</h1>
        <p>If you see this page, the nginx web server is successfully installed and
        working. Further configuration is required.</p>
        
        <p>For online documentation and support please refer to
        <a href="http://nginx.org/">nginx.org</a>.<br/>
        Commercial support is available at
        <a href="http://nginx.com/">nginx.com</a>.</p>
        
        <p><em>Thank you for using nginx.</em></p>
        </body>
        </html>
        ```

    -   By using the  domain name

        **curl** _nginx-_**clusterip.default.svc.cluster.local:**_2_

        If information similar to the following is displayed, the workload is accessible.

        ```
        <html>
        <head>
        <title>Welcome to nginx!</title>
        <style>
            body {
                width: 35em;
                margin: 0 auto;
                font-family: Tahoma, Verdana, Arial, sans-serif;
            }
        </style>
        </head>
        <body>
        <h1>Welcome to nginx!</h1>
        <p>If you see this page, the nginx web server is successfully installed and
        working. Further configuration is required.</p>
        
        <p>For online documentation and support please refer to
        <a href="http://nginx.org/">nginx.org</a>.<br/>
        Commercial support is available at
        <a href="http://nginx.com/">nginx.com</a>.</p>
        
        <p><em>Thank you for using nginx.</em></p>
        </body>
        </html>
        ```



## Setting the Access Type After Creating a Workload on the Console<a name="section51925078171335"></a>

You can set the access type after creating a workload. This has no impact on the workload status and takes effect immediately. The procedure is as follows:

1.  Log in to the CCE console. In the navigation pane, choose  **Workloads**  \>  **Deployments**. On the workload list, click the name of the workload for which you will create a service.
2.  On the  **Services**  tab page, click  **Create Service**.
3.  On the  **Create Service**  page, select  **Intra-cluster access \(cluster IP\)**  from the  **Access Type**  drop-down list.
4.  Set intra-cluster access parameters.
    -   **Service Name**: can be the same as the workload name.
    -   **Cluster Name**: name of the cluster where the workload runs. The value is inherited from the workload creation page and cannot be changed.
    -   **Namespace**: namespace where the workload is located. The value is inherited from the workload creation page and cannot be changed.
    -   **Workload**: a workload for which you want to add a service.
    -   **Port Settings**
        -   **Protocol**: a protocol used by the service.
        -   **Container Port**: a port on which the workload listens. The nginx application listens on port 80.
        -   **Access Port**: a port mapped to the container port at the cluster-internal IP address. The workload can be accessed at <cluster-internal IP address\>:<access port\>. The port number range is 1–65535.

5.  Click  **Create**. The intra-cluster access service will be added for the workload.

## Updating a Service<a name="section170649161816"></a>

After adding a service, you can update the port configuration of the service. The procedure is as follows:

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Network**. On the  **Services**  tab page, click  **Update**  for the service to be updated.
2.  On the  **Update Service**  page, select  **Intra-cluster access \(cluster IP\)**  from the  **Access Type**  drop-down list.
3.  Update intra-cluster access parameters.
    -   **Cluster Name**: name of the cluster where the workload runs. The value is inherited from the workload creation page and cannot be changed.
    -   **Namespace**: namespace where the workload is located. The value is inherited from the workload creation page and cannot be changed.
    -   **Workload**: a workload for which you want to update the service. The value is inherited from the workload creation page and cannot be changed.
    -   **Port Settings**
        -   **Protocol**: a protocol used by the service.
        -   **Container Port**: a port on which the workload listens. The Nginx workload listens on port 80.
        -   **Access Port**: a port mapped to the container port at the cluster-internal IP address. The workload can be accessed at <cluster-internal IP address\>:<access port\>. The port number range is 1–65535.

4.  Click  **Update**. The service will be updated for the workload.

