# How Do I Use kubectl to Set the Workload Access Type to LoadBalancer \(ELB\)?<a name="cce_faq_00099"></a>

This section uses the Nginx workload as an example to describe how to set the workload access type to  **LoadBalancer \(ELB\)**.

## Prerequisites<a name="en-us_topic_0242566244_section7807122171"></a>

-   An ELB has been created.
-   You have connected an Elastic Cloud Server \(ECS\) to the cluster by running the kubectl command. For details, see  [Connecting to a CCE Cluster Using kubectl or web-terminal](connecting-to-a-kubernetes-cluster-using-kubectl.md).

## Procedure<a name="en-us_topic_0242566244_section1341315116296"></a>

1.  Log in to the  ECS  on which the  kubectl  has been configured.
2.  Create and edit the  **nginx-deployment.yaml**  and  **nginx-elb-svc.yaml**  files.

    The file names are user-defined.  **nginx-deployment.yaml**  and  **nginx-elb-svc.yaml**  are merely example file names.

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

    **vi nginx-elb-svc.yaml**

    >![](/images/icon-note.gif) **NOTE:** 
    >Before enabling session stickness, ensure that the following conditions are met:
    >-   The workload protocol is TCP.
    >-   Anti-affinity has been configured between pods of the workload. That is, all pods of the workload are deployed on different nodes.

    -   Automatically creating load balancer

        ```
        apiVersion: v1 
        kind: Service 
        metadata: 
          annotations:   
            kubernetes.io/elb.class: union
            kubernetes.io/session-affinity-mode: SOURCE_IP
            kubernetes.io/elb.subnet-id: 5083f225-9bf8-48fa-9c8b-67bd9693c4c0
            kubernetes.io/elb.enterpriseID: debb7ae2-6d2f-4e6c-a0aa-1ccafd92b8eb
            kubernetes.io/elb.autocreate: '{"type":"public","bandwidth_name":"cce-bandwidth-1551163379627","bandwidth_chargemode":"traffic","bandwidth_size":5,"bandwidth_sharetype":"PER","eip_type":"5_bgp","name":"james"}'
          labels: 
            app: nginx 
          name: nginx 
        spec: 
          externalTrafficPolicy: Local
          ports: 
          - name: service0 
            port: 80
            protocol: TCP 
            targetPort: 80
          selector: 
            app: nginx 
          type: LoadBalancer
        ```

    -   Using existing load balancer

        ```
        apiVersion: v1 
        kind: Service 
        metadata: 
          annotations:   
            kubernetes.io/elb.class: union
            kubernetes.io/session-affinity-mode: SOURCE_IP
            kubernetes.io/elb.id: 3c7caa5a-a641-4bff-801a-feace27424b6
            kubernetes.io/elb.subnet-id: 5083f225-9bf8-48fa-9c8b-67bd9693c4c0
          labels: 
            app: nginx 
          name: nginx 
        spec: 
          loadBalancerIP: 10.78.42.242
          externalTrafficPolicy: Local
          ports: 
          - name: service0 
            port: 80
            protocol: TCP 
            targetPort: 80
          selector: 
            app: nginx 
          type: LoadBalancer
        ```

    **Table  1**  Key parameters

    <a name="en-us_topic_0242566244_table1756816623818"></a>
    <table><thead align="left"><tr id="en-us_topic_0242566244_row185681764384"><th class="cellrowborder" valign="top" width="34.28657134286571%" id="mcps1.2.4.1.1"><p id="en-us_topic_0242566244_p1956846183813"><a name="en-us_topic_0242566244_p1956846183813"></a><a name="en-us_topic_0242566244_p1956846183813"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="14.118588141185882%" id="mcps1.2.4.1.2"><p id="en-us_topic_0242566244_p65680613389"><a name="en-us_topic_0242566244_p65680613389"></a><a name="en-us_topic_0242566244_p65680613389"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.594840515948405%" id="mcps1.2.4.1.3"><p id="en-us_topic_0242566244_p9568069386"><a name="en-us_topic_0242566244_p9568069386"></a><a name="en-us_topic_0242566244_p9568069386"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0242566244_row1556817623815"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p20568669388"><a name="en-us_topic_0242566244_p20568669388"></a><a name="en-us_topic_0242566244_p20568669388"></a>kubernetes.io/elb.class</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p656812617387"><a name="en-us_topic_0242566244_p656812617387"></a><a name="en-us_topic_0242566244_p656812617387"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p15568169382"><a name="en-us_topic_0242566244_p15568169382"></a><a name="en-us_topic_0242566244_p15568169382"></a>Mandatory and must be set to <span class="uicontrol" id="en-us_topic_0242566244_uicontrol1956876133814"><a name="en-us_topic_0242566244_uicontrol1956876133814"></a><a name="en-us_topic_0242566244_uicontrol1956876133814"></a><b>union</b></span> if an enhanced load balancer is in use.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row205681669387"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p756876143810"><a name="en-us_topic_0242566244_p756876143810"></a><a name="en-us_topic_0242566244_p756876143810"></a>kubernetes.io/session-affinity-mode</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p175681461388"><a name="en-us_topic_0242566244_p175681461388"></a><a name="en-us_topic_0242566244_p175681461388"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p75681623817"><a name="en-us_topic_0242566244_p75681623817"></a><a name="en-us_topic_0242566244_p75681623817"></a>Optional. If session stickness is enabled, add this parameter.</p>
    <p id="en-us_topic_0242566244_p65689616388"><a name="en-us_topic_0242566244_p65689616388"></a><a name="en-us_topic_0242566244_p65689616388"></a>The value <strong id="en-us_topic_0242566244_b1756818693818"><a name="en-us_topic_0242566244_b1756818693818"></a><a name="en-us_topic_0242566244_b1756818693818"></a>SOURCE_IP</strong> indicates that listeners ensure session stickiness based on source IP addresses.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row9568961384"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p45696617387"><a name="en-us_topic_0242566244_p45696617387"></a><a name="en-us_topic_0242566244_p45696617387"></a>kubernetes.io/elb.id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p15569116193818"><a name="en-us_topic_0242566244_p15569116193818"></a><a name="en-us_topic_0242566244_p15569116193818"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p956910616386"><a name="en-us_topic_0242566244_p956910616386"></a><a name="en-us_topic_0242566244_p956910616386"></a>Optional. This parameter is mandatory if an existing load balancer is used.</p>
    <p id="en-us_topic_0242566244_p14569126183813"><a name="en-us_topic_0242566244_p14569126183813"></a><a name="en-us_topic_0242566244_p14569126183813"></a>It indicates the ID of an enhanced load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row1256996173815"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p1856966113810"><a name="en-us_topic_0242566244_p1856966113810"></a><a name="en-us_topic_0242566244_p1856966113810"></a>kubernetes.io/elb.subnet-id</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p205698683810"><a name="en-us_topic_0242566244_p205698683810"></a><a name="en-us_topic_0242566244_p205698683810"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p165691364381"><a name="en-us_topic_0242566244_p165691364381"></a><a name="en-us_topic_0242566244_p165691364381"></a>Optional. This parameter is mandatory only if a load balancer will be automatically created. For clusters of v1.11.7-r0 or later, this parameter can be left unspecified.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row1156996123817"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p65698614383"><a name="en-us_topic_0242566244_p65698614383"></a><a name="en-us_topic_0242566244_p65698614383"></a>kubernetes.io/elb.enterpriseID</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p75692653813"><a name="en-us_topic_0242566244_p75692653813"></a><a name="en-us_topic_0242566244_p75692653813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p956956173816"><a name="en-us_topic_0242566244_p956956173816"></a><a name="en-us_topic_0242566244_p956956173816"></a>Optional. This parameter is mandatory if a public/private network load balancer will be automatically created.</p>
    <p id="en-us_topic_0242566244_p18569960381"><a name="en-us_topic_0242566244_p18569960381"></a><a name="en-us_topic_0242566244_p18569960381"></a>This parameter indicates the name of the ELB enterprise project in which the ELB will be created.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row18569106123820"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p056915633818"><a name="en-us_topic_0242566244_p056915633818"></a><a name="en-us_topic_0242566244_p056915633818"></a>kubernetes.io/elb.autocreate</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p2569267388"><a name="en-us_topic_0242566244_p2569267388"></a><a name="en-us_topic_0242566244_p2569267388"></a><a href="#en-us_topic_0242566244_table957018613817">elb.autocreate</a> object</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p95697613811"><a name="en-us_topic_0242566244_p95697613811"></a><a name="en-us_topic_0242566244_p95697613811"></a>Optional. This parameter is mandatory if a public network load balancer will be automatically created. The system will create an enhanced load balancer and an EIP. This parameter is also mandatory if a private network load balancer will be automatically created. The system will create an enhanced load balancer.</p>
    <p id="en-us_topic_0242566244_p15690663813"><a name="en-us_topic_0242566244_p15690663813"></a><a name="en-us_topic_0242566244_p15690663813"></a><strong id="en-us_topic_0242566244_b95696653812"><a name="en-us_topic_0242566244_b95696653812"></a><a name="en-us_topic_0242566244_b95696653812"></a>Example:</strong></p>
    <a name="en-us_topic_0242566244_ul55694683814"></a><a name="en-us_topic_0242566244_ul55694683814"></a><ul id="en-us_topic_0242566244_ul55694683814"><li>Automatically created public network load balancer:<p id="en-us_topic_0242566244_p7569136133819"><a name="en-us_topic_0242566244_p7569136133819"></a><a name="en-us_topic_0242566244_p7569136133819"></a>{"type":"public","bandwidth_name":"cce-bandwidth-1551163379627","bandwidth_chargemode":"traffic","bandwidth_size":5,"bandwidth_sharetype":"PER","eip_type":"5_bgp","name":"james"}</p>
    </li><li>Automatically created private network load balancer:<p id="en-us_topic_0242566244_p18569196153818"><a name="en-us_topic_0242566244_p18569196153818"></a><a name="en-us_topic_0242566244_p18569196153818"></a>{"type":"inner", "name": "A-location-d-test"}</p>
    </li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row75691869386"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p1156913616382"><a name="en-us_topic_0242566244_p1156913616382"></a><a name="en-us_topic_0242566244_p1156913616382"></a>loadBalancerIP</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p1956911663819"><a name="en-us_topic_0242566244_p1956911663819"></a><a name="en-us_topic_0242566244_p1956911663819"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p85695653815"><a name="en-us_topic_0242566244_p85695653815"></a><a name="en-us_topic_0242566244_p85695653815"></a>Private IP address of a private network load balancer or public IP address of a public network load balancer.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row1756911673817"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p556920616384"><a name="en-us_topic_0242566244_p556920616384"></a><a name="en-us_topic_0242566244_p556920616384"></a>externalTrafficPolicy</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p14570136193813"><a name="en-us_topic_0242566244_p14570136193813"></a><a name="en-us_topic_0242566244_p14570136193813"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p14570969388"><a name="en-us_topic_0242566244_p14570969388"></a><a name="en-us_topic_0242566244_p14570969388"></a>Optional. If session stickness is enabled, add this parameter so requests are transferred to a fixed node. If a LoadBalancer service with this parameter set to <strong id="en-us_topic_0242566244_b0570063385"><a name="en-us_topic_0242566244_b0570063385"></a><a name="en-us_topic_0242566244_b0570063385"></a>Local</strong> is created for a workload, the workload can be accessed only when the client is installed on the same node as the server.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row13570126103813"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p85700613810"><a name="en-us_topic_0242566244_p85700613810"></a><a name="en-us_topic_0242566244_p85700613810"></a>port</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p1057012614389"><a name="en-us_topic_0242566244_p1057012614389"></a><a name="en-us_topic_0242566244_p1057012614389"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p105704617386"><a name="en-us_topic_0242566244_p105704617386"></a><a name="en-us_topic_0242566244_p105704617386"></a>Access port that is registered on the load balancer and mapped to the cluster-internal IP address.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row145704618381"><td class="cellrowborder" valign="top" width="34.28657134286571%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p157013613380"><a name="en-us_topic_0242566244_p157013613380"></a><a name="en-us_topic_0242566244_p157013613380"></a>targetPort</p>
    </td>
    <td class="cellrowborder" valign="top" width="14.118588141185882%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p4570106183814"><a name="en-us_topic_0242566244_p4570106183814"></a><a name="en-us_topic_0242566244_p4570106183814"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p45705673816"><a name="en-us_topic_0242566244_p45705673816"></a><a name="en-us_topic_0242566244_p45705673816"></a>Container port on the CCE console.</p>
    </td>
    </tr>
    </tbody>
    </table>

    **Table  2**  elb.autocreate parameters

    <a name="en-us_topic_0242566244_table957018613817"></a>
    <table><thead align="left"><tr id="en-us_topic_0242566244_row185701673815"><th class="cellrowborder" valign="top" width="29.727027297270276%" id="mcps1.2.4.1.1"><p id="en-us_topic_0242566244_p95708611389"><a name="en-us_topic_0242566244_p95708611389"></a><a name="en-us_topic_0242566244_p95708611389"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="18.678132186781323%" id="mcps1.2.4.1.2"><p id="en-us_topic_0242566244_p3570162382"><a name="en-us_topic_0242566244_p3570162382"></a><a name="en-us_topic_0242566244_p3570162382"></a>Type</p>
    </th>
    <th class="cellrowborder" valign="top" width="51.594840515948405%" id="mcps1.2.4.1.3"><p id="en-us_topic_0242566244_p1257018623812"><a name="en-us_topic_0242566244_p1257018623812"></a><a name="en-us_topic_0242566244_p1257018623812"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0242566244_row75705613388"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p1457013613388"><a name="en-us_topic_0242566244_p1457013613388"></a><a name="en-us_topic_0242566244_p1457013613388"></a>name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p257166133817"><a name="en-us_topic_0242566244_p257166133817"></a><a name="en-us_topic_0242566244_p257166133817"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p205711563381"><a name="en-us_topic_0242566244_p205711563381"></a><a name="en-us_topic_0242566244_p205711563381"></a>Name of the load balancer that is automatically created.</p>
    <p id="en-us_topic_0242566244_p35711269383"><a name="en-us_topic_0242566244_p35711269383"></a><a name="en-us_topic_0242566244_p35711269383"></a>The value is a string of 1 to 64 characters that consist of letters, digits, underscores (_), and hyphens (-).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row1957115693817"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p6571186193818"><a name="en-us_topic_0242566244_p6571186193818"></a><a name="en-us_topic_0242566244_p6571186193818"></a>type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p2057114614383"><a name="en-us_topic_0242566244_p2057114614383"></a><a name="en-us_topic_0242566244_p2057114614383"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p3571186173817"><a name="en-us_topic_0242566244_p3571186173817"></a><a name="en-us_topic_0242566244_p3571186173817"></a>Network type of the load balancer.</p>
    <a name="en-us_topic_0242566244_ul185711266384"></a><a name="en-us_topic_0242566244_ul185711266384"></a><ul id="en-us_topic_0242566244_ul185711266384"><li><strong id="en-us_topic_0242566244_b1057146133817"><a name="en-us_topic_0242566244_b1057146133817"></a><a name="en-us_topic_0242566244_b1057146133817"></a>public</strong>: public network load balancer.</li><li><strong id="en-us_topic_0242566244_b8571169389"><a name="en-us_topic_0242566244_b8571169389"></a><a name="en-us_topic_0242566244_b8571169389"></a>inner</strong>: private network load balancer.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row10571962388"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p657176133817"><a name="en-us_topic_0242566244_p657176133817"></a><a name="en-us_topic_0242566244_p657176133817"></a>bandwidth_name</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p155711268386"><a name="en-us_topic_0242566244_p155711268386"></a><a name="en-us_topic_0242566244_p155711268386"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p7571967384"><a name="en-us_topic_0242566244_p7571967384"></a><a name="en-us_topic_0242566244_p7571967384"></a>Bandwidth name. The default value is <strong id="en-us_topic_0242566244_b11571106203819"><a name="en-us_topic_0242566244_b11571106203819"></a><a name="en-us_topic_0242566244_b11571106203819"></a>cce-bandwidth-******</strong>.</p>
    <p id="en-us_topic_0242566244_p1757110643812"><a name="en-us_topic_0242566244_p1757110643812"></a><a name="en-us_topic_0242566244_p1757110643812"></a>The value is a string of 1 to 64 characters that consist of letters, digits, underscores (_), hyphens (-), and periods (.).</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row85712618386"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p11571061383"><a name="en-us_topic_0242566244_p11571061383"></a><a name="en-us_topic_0242566244_p11571061383"></a>bandwidth_chargemode</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p15571968380"><a name="en-us_topic_0242566244_p15571968380"></a><a name="en-us_topic_0242566244_p15571968380"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p4571462386"><a name="en-us_topic_0242566244_p4571462386"></a><a name="en-us_topic_0242566244_p4571462386"></a>Bandwidth billing mode.</p>
    <p id="en-us_topic_0242566244_p17993157195913"><a name="en-us_topic_0242566244_p17993157195913"></a><a name="en-us_topic_0242566244_p17993157195913"></a>The value is <strong id="en-us_topic_0242566244_b267410514014"><a name="en-us_topic_0242566244_b267410514014"></a><a name="en-us_topic_0242566244_b267410514014"></a>traffic</strong>, indicating that the billing is based on traffic.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row1257166183813"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p1457217643813"><a name="en-us_topic_0242566244_p1457217643813"></a><a name="en-us_topic_0242566244_p1457217643813"></a>bandwidth_size</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p135729603817"><a name="en-us_topic_0242566244_p135729603817"></a><a name="en-us_topic_0242566244_p135729603817"></a>Integer</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p057217613819"><a name="en-us_topic_0242566244_p057217613819"></a><a name="en-us_topic_0242566244_p057217613819"></a>Bandwidth size. Set this parameter based on the bandwidth range supported by the region.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row75722061380"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p155726633810"><a name="en-us_topic_0242566244_p155726633810"></a><a name="en-us_topic_0242566244_p155726633810"></a>bandwidth_sharetype</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p7572196153815"><a name="en-us_topic_0242566244_p7572196153815"></a><a name="en-us_topic_0242566244_p7572196153815"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p757220617386"><a name="en-us_topic_0242566244_p757220617386"></a><a name="en-us_topic_0242566244_p757220617386"></a>Bandwidth sharing mode.</p>
    <a name="en-us_topic_0242566244_ul1757217663812"></a><a name="en-us_topic_0242566244_ul1757217663812"></a><ul id="en-us_topic_0242566244_ul1757217663812"><li><strong id="en-us_topic_0242566244_b857211615382"><a name="en-us_topic_0242566244_b857211615382"></a><a name="en-us_topic_0242566244_b857211615382"></a>PER</strong>: dedicated bandwidth.</li><li><strong id="en-us_topic_0242566244_b857216693812"><a name="en-us_topic_0242566244_b857216693812"></a><a name="en-us_topic_0242566244_b857216693812"></a>WHOLE</strong>: shared bandwidth.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0242566244_row35720615383"><td class="cellrowborder" valign="top" width="29.727027297270276%" headers="mcps1.2.4.1.1 "><p id="en-us_topic_0242566244_p145721618380"><a name="en-us_topic_0242566244_p145721618380"></a><a name="en-us_topic_0242566244_p145721618380"></a>eip_type</p>
    </td>
    <td class="cellrowborder" valign="top" width="18.678132186781323%" headers="mcps1.2.4.1.2 "><p id="en-us_topic_0242566244_p18572368387"><a name="en-us_topic_0242566244_p18572368387"></a><a name="en-us_topic_0242566244_p18572368387"></a>String</p>
    </td>
    <td class="cellrowborder" valign="top" width="51.594840515948405%" headers="mcps1.2.4.1.3 "><p id="en-us_topic_0242566244_p1157366193818"><a name="en-us_topic_0242566244_p1157366193818"></a><a name="en-us_topic_0242566244_p1157366193818"></a>EIP type.</p>
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
    etcd-0                   0/1       ImagePullBackOff   0          1h
    icagent-m9dkt            0/0       Running            0          3d
    nginx-2601814895-c1xhw   1/1       Running            0          6s
    ```

4.  Create a service.

    **kubectl create -f nginx-elb-svc.yaml**

    If information similar to the following is displayed, the service has been created.

    ```
    service "nginx" created
    ```

    **kubectl get svc**

    If information similar to the following is displayed, the service access type has been set successfully, and the workload is accessible.

    ```
    NAME         TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
    etcd-svc     ClusterIP      None             <none>        3120/TCP       1h
    kubernetes   ClusterIP      10.247.0.1       <none>        443/TCP        3d
    nginx        LoadBalancer   10.247.130.196   10.78.42.242   80:31540/TCP   51s
    ```

5.  Enter the URL in the address box of the browser, for example,  **10.78.42.242:31540**.  **10.78.42.242**  indicates the IP address of the load balancer, and  **31540**  indicates the access port displayed on the CCE console.

    The Nginx is accessible.

    **Figure  1**  Accessing Nginx through load balancing \(2\)<a name="en-us_topic_0242566244_fig3593233113811"></a>  
    ![](figures/accessing-nginx-through-load-balancing-(2)-16.png "accessing-nginx-through-load-balancing-(2)-16")


