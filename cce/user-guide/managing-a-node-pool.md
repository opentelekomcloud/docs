# Managing a Node Pool<a name="cce_01_0222"></a>

## Configuration Management<a name="section17534155232712"></a>

To facilitate the management of Kubernetes parameters in a cluster, the cloud provides the configuration function. This function allows you to perform in-depth configuration on core components. For details, see  [kubelet](https://v1-15.docs.kubernetes.io/docs/reference/command-line-tools-reference/kubelet)  and  [docker](https://docs.docker.com/engine/reference/commandline/dockerd).

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>-   This function is available only for clusters of v1.15 or later.  
>-   The default node pool DefaultPool does not support this type of configuration.  

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pools**.
2.  In the upper right corner of the displayed page, select a cluster to filter node pools by cluster.
3.  Click  **Configuration**  next to the node pool name.
4.  Change the values of the following Kubernetes parameters based on service requirements:

    **Table  1**  Kubernetes parameters

    <a name="table1754618559276"></a>
    <table><thead align="left"><tr id="row8546105514277"><th class="cellrowborder" valign="top" width="23.577642235776423%" id="mcps1.2.5.1.1"><p id="p16546145517275"><a name="p16546145517275"></a><a name="p16546145517275"></a>Component</p>
    </th>
    <th class="cellrowborder" valign="top" width="31.86681331866813%" id="mcps1.2.5.1.2"><p id="p45466555279"><a name="p45466555279"></a><a name="p45466555279"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="32.966703329667034%" id="mcps1.2.5.1.3"><p id="p35461855162712"><a name="p35461855162712"></a><a name="p35461855162712"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="11.58884111588841%" id="mcps1.2.5.1.4"><p id="p1754619556274"><a name="p1754619556274"></a><a name="p1754619556274"></a>Default Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row12546165518278"><td class="cellrowborder" rowspan="2" valign="top" width="23.577642235776423%" headers="mcps1.2.5.1.1 "><p id="p5546195519271"><a name="p5546195519271"></a><a name="p5546195519271"></a>docker</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.86681331866813%" headers="mcps1.2.5.1.2 "><p id="p8547185582715"><a name="p8547185582715"></a><a name="p8547185582715"></a>native-umask</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.966703329667034%" headers="mcps1.2.5.1.3 "><p id="p1454745582719"><a name="p1454745582719"></a><a name="p1454745582719"></a>`--exec-opt native.umask</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.58884111588841%" headers="mcps1.2.5.1.4 "><p id="p195471555122713"><a name="p195471555122713"></a><a name="p195471555122713"></a>normal</p>
    </td>
    </tr>
    <tr id="row254765502711"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1154745572715"><a name="p1154745572715"></a><a name="p1154745572715"></a>docker-base-size</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p19547175582714"><a name="p19547175582714"></a><a name="p19547175582714"></a>`--storage-opts dm.basesize</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p17547135513275"><a name="p17547135513275"></a><a name="p17547135513275"></a>10G</p>
    </td>
    </tr>
    <tr id="row17272192410524"><td class="cellrowborder" rowspan="2" valign="top" width="23.577642235776423%" headers="mcps1.2.5.1.1 "><p id="p52321759115212"><a name="p52321759115212"></a><a name="p52321759115212"></a>kube-proxy</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.86681331866813%" headers="mcps1.2.5.1.2 "><p id="p327372415219"><a name="p327372415219"></a><a name="p327372415219"></a>conntrack-min</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.966703329667034%" headers="mcps1.2.5.1.3 "><p id="p1127332413527"><a name="p1127332413527"></a><a name="p1127332413527"></a>sysctl -w net.nf_conntrack_max</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.58884111588841%" headers="mcps1.2.5.1.4 "><p id="p132731424185214"><a name="p132731424185214"></a><a name="p132731424185214"></a>131072</p>
    </td>
    </tr>
    <tr id="row569134712527"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p869147195216"><a name="p869147195216"></a><a name="p869147195216"></a>conntrack-tcp-timeout-close-wait</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p134717327114"><a name="p134717327114"></a><a name="p134717327114"></a>sysctl -w net.netfilter.nf_conntrack_tcp_timeout_clouse_wait</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p4691347175214"><a name="p4691347175214"></a><a name="p4691347175214"></a>1h0m0s</p>
    </td>
    </tr>
    <tr id="row175476554277"><td class="cellrowborder" rowspan="6" valign="top" width="23.577642235776423%" headers="mcps1.2.5.1.1 "><p id="p1654715558278"><a name="p1654715558278"></a><a name="p1654715558278"></a>kubelet</p>
    </td>
    <td class="cellrowborder" valign="top" width="31.86681331866813%" headers="mcps1.2.5.1.2 "><p id="p1954785552717"><a name="p1954785552717"></a><a name="p1954785552717"></a>cpu-manager-policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="32.966703329667034%" headers="mcps1.2.5.1.3 "><p id="p12547145518272"><a name="p12547145518272"></a><a name="p12547145518272"></a>`--cpu-manager-policy</p>
    </td>
    <td class="cellrowborder" valign="top" width="11.58884111588841%" headers="mcps1.2.5.1.4 "><p id="p5547165517270"><a name="p5547165517270"></a><a name="p5547165517270"></a>none</p>
    </td>
    </tr>
    <tr id="row15547755132711"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p10547555162713"><a name="p10547555162713"></a><a name="p10547555162713"></a>kube-api-qps</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p65471955172712"><a name="p65471955172712"></a><a name="p65471955172712"></a>QPS communicating with kube-apiserver.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p19547185513271"><a name="p19547185513271"></a><a name="p19547185513271"></a>100</p>
    </td>
    </tr>
    <tr id="row9547135514272"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p13547155511276"><a name="p13547155511276"></a><a name="p13547155511276"></a>kube-api-burst</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p65477552279"><a name="p65477552279"></a><a name="p65477552279"></a>Burst communicating with kube-apiserver.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p654795512278"><a name="p654795512278"></a><a name="p654795512278"></a>100</p>
    </td>
    </tr>
    <tr id="row135471551272"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1754745511277"><a name="p1754745511277"></a><a name="p1754745511277"></a>max-pods</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p7547555162714"><a name="p7547555162714"></a><a name="p7547555162714"></a>Maximum number of pods managed by kubelet.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p19547455162713"><a name="p19547455162713"></a><a name="p19547455162713"></a>110</p>
    </td>
    </tr>
    <tr id="row34291238195413"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1142903815544"><a name="p1142903815544"></a><a name="p1142903815544"></a>with-local-dns</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p153025513395"><a name="p153025513395"></a><a name="p153025513395"></a>Whether to use the local IP address as the ClusterDNS of the node.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p134291238105413"><a name="p134291238105413"></a><a name="p134291238105413"></a>false</p>
    </td>
    </tr>
    <tr id="row18828113575414"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p182816355546"><a name="p182816355546"></a><a name="p182816355546"></a>allowed-unsafe-sysctls</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p168293359548"><a name="p168293359548"></a><a name="p168293359548"></a>Insecure system configuration allowed.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1482918356544"><a name="p1482918356544"></a><a name="p1482918356544"></a>[]</p>
    </td>
    </tr>
    </tbody>
    </table>

5.  Click  **OK**.

## Editing a Node Pool<a name="section359343125016"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pools**.
2.  In the upper right corner of the displayed page, select a cluster to filter node pools by cluster.
3.  Click  **Edit**  next to the name of the node pool you will edit. In the  **Edit Node Pool**  dialog box, edit the following parameters:

    **Table  2**  Editing node pool parameters

    <a name="table16321825732"></a>
    <table><thead align="left"><tr id="row173212251235"><th class="cellrowborder" valign="top" width="28.000000000000004%" id="mcps1.2.3.1.1"><p id="p43211725338"><a name="p43211725338"></a><a name="p43211725338"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="72%" id="mcps1.2.3.1.2"><p id="p0322102516320"><a name="p0322102516320"></a><a name="p0322102516320"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row163229255313"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p1232219251339"><a name="p1232219251339"></a><a name="p1232219251339"></a>Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p129475498531"><a name="p129475498531"></a><a name="p129475498531"></a>Name of the node pool.</p>
    </td>
    </tr>
    <tr id="row6334727910"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p233592498"><a name="p233592498"></a><a name="p233592498"></a>Nodes</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p149431649155313"><a name="p149431649155313"></a><a name="p149431649155313"></a>Modify the number of nodes based on service requirements.</p>
    </td>
    </tr>
    <tr id="row111551253912"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p51551451293"><a name="p51551451293"></a><a name="p51551451293"></a>Autoscaler</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p20736112217461"><a name="p20736112217461"></a><a name="p20736112217461"></a>By default, autoscaler is disabled.</p>
    <p id="p1965815358257"><a name="p1965815358257"></a><a name="p1965815358257"></a>After you enable autoscaler by clicking After you enable autoscaler by clicking <a name="image2271132994219"></a><a name="image2271132994219"></a><span><img id="image2271132994219" src="figures/icon-autoscaler-disabled-3.png"></span>, nodes in the node pool are automatically created or deleted based on service requirements.</p>
    <a name="ul63223620274"></a><a name="ul63223620274"></a><ul id="ul63223620274"><li><strong id="b98562832611"><a name="b98562832611"></a><a name="b98562832611"></a>Maximum Nodes</strong> and <strong id="b4541113102617"><a name="b4541113102617"></a><a name="b4541113102617"></a>Minimum Nodes</strong>: You can set the maximum and minimum number of nodes to ensure that the number of nodes to be scaled is within a proper range.</li></ul>
    <a name="ul15733045165119"></a><a name="ul15733045165119"></a><ul id="ul15733045165119"><li><strong id="b16822104144015"><a name="b16822104144015"></a><a name="b16822104144015"></a>Priority</strong>: You can set the priority of auto scaling between node pools based on service requirements. If the value is set to <strong id="b48229418409"><a name="b48229418409"></a><a name="b48229418409"></a>0</strong>, scaling is performed based on the minimum resource waste principle.</li><li><strong id="b13822114119406"><a name="b13822114119406"></a><a name="b13822114119406"></a>Scale-In Cooling Interval</strong>: Set this parameter in the unit of minute. This field indicates the period during which the nodes added in the current node pool cannot be scaled in.</li></ul>
    <p id="p12614171015488"><a name="p12614171015488"></a><a name="p12614171015488"></a>If the <strong id="b18191718101819"><a name="b18191718101819"></a><a name="b18191718101819"></a>Autoscaler</strong> field is set to on, install the <a href="autoscaler.md">autoscaler add-on</a> to use the autoscaler feature.</p>
    </td>
    </tr>
    <tr id="row1535723154615"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p1834102910536"><a name="p1834102910536"></a><a name="p1834102910536"></a>Taints</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><a name="ul1414103745816"></a><a name="ul1414103745816"></a><ul id="ul1414103745816"><li>This field is left blank by default. Taints allow nodes to repel a set of pods. You can add a maximum of 10 taints for each node pool. Each taint contains the following parameters:<a name="ul17274222121015"></a><a name="ul17274222121015"></a><ul id="ul17274222121015"><li><strong id="b138225358187"><a name="b138225358187"></a><a name="b138225358187"></a>Key</strong>: A key must contain 1 to 63 characters starting with a letter or digit. Only letters, digits, hyphens (-), underscores (_), and periods (.) are allowed. A DNS subdomain name can be used as the prefix of a key.</li><li><strong id="b172009380180"><a name="b172009380180"></a><a name="b172009380180"></a>Value</strong>: A value must start with a letter or digit and can contain a maximum of 63 characters, including letters, digits, hyphens (-), underscores (_), and periods (.).</li><li><strong id="b20244184015182"><a name="b20244184015182"></a><a name="b20244184015182"></a>Effect</strong>: Available options are <strong id="b19246154041816"><a name="b19246154041816"></a><a name="b19246154041816"></a>NoSchedule</strong>, <strong id="b824764019183"><a name="b824764019183"></a><a name="b824764019183"></a>PreferNoSchedule</strong>, and <strong id="b624994001818"><a name="b624994001818"></a><a name="b624994001818"></a>NoExecute</strong>.</li></ul>
    <div class="notice" id="note77443231113"><a name="note77443231113"></a><a name="note77443231113"></a><span class="noticetitle"> NOTICE: </span><div class="noticebody"><a name="ul104271158181515"></a><a name="ul104271158181515"></a><ul id="ul104271158181515"><li>If taints are used, you must configure tolerations in the YAML files of pods. Otherwise, scale-up may fail or pods cannot be scheduled onto the added nodes.</li><li>Taints cannot be modified after configuration. Incorrect taints may cause a scale-up failure or prevent pods from being scheduled onto the added nodes.</li></ul>
    </div></div>
    </li></ul>
    </td>
    </tr>
    <tr id="row133224252315"><td class="cellrowborder" valign="top" width="28.000000000000004%" headers="mcps1.2.3.1.1 "><p id="p13807203616539"><a name="p13807203616539"></a><a name="p13807203616539"></a>K8S Labels</p>
    </td>
    <td class="cellrowborder" valign="top" width="72%" headers="mcps1.2.3.1.2 "><p id="p425074311536"><a name="p425074311536"></a><a name="p425074311536"></a>K8S labels are key/value pairs that are attached to objects, such as pods. Labels are intended to be used to specify identifying attributes of objects that are meaningful and relevant to users, but do not directly imply semantics to the core system. For more information, see <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/" target="_blank" rel="noopener noreferrer">Labels and Selectors</a>.</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  After the configuration is complete, click  **Save**.

    In the node pool list, the node pool status is  **Scaling**. After the status changes to  **Complete**, the node pool parameters are edited successfully.


## Copying a Node Pool<a name="section550619571556"></a>

You can copy the configuration of an existing node pool to create a new node pool on the CCE console.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pools**.
2.  In the upper right corner of the displayed page, select a cluster to filter node pools by cluster.
3.  Choose  **More \> Copy**  next to a node pool name to copy the node pool.
4.  The configuration of the selected node pool is replicated to the Create Node Pool page. You can edit the configuration as required and click  **Next: Confirm**.
5.  On the  **Confirm**  page, confirm the node pool configuration and click  **Create Now**. Then, a new node pool is created based on the edited configuration.

## Migrating a Node<a name="section442531421517"></a>

You can migrate a node from a node pool to the default node pool in the same cluster. Currently, a node in the default node pool cannot be migrated to another node pool.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pools**.
2.  In the upper right corner of the displayed page, select a cluster to filter node pools by cluster.
3.  Click  **More**\>  **Migrate**  next to the name of the node pool.
4.  In the dialog box displayed, select the destination node pool and the node to be migrated.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   Check whether the disk specifications of the node to be migrated are the same as those of the destination node pool.  
    >-   After node migration, original resources tags, Kubernetes tags, and taints will be retained, and new tags and taints from the destination node pool will be added.  

5.  Click  **OK**.

## Deleting a Node Pool<a name="section135941731115017"></a>

Deleting a node pool will delete nodes in the pool. Pods on these nodes will be automatically migrated to available nodes in other node pools. If pods in the node pool have a specific node selector and none of the other nodes in the cluster satisfies the node selector, the pods will become unschedulable.

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Node Pools**.
2.  In the upper right corner of the displayed page, select a cluster to filter node pools by cluster.
3.  Choose  **More \> Delete**  next to a node pool name to delete the node pool.
4.  Read the precautions in the  **Delete Node Pool**  dialog box.
5.  Enter  **DELETE**  in the text box and click  **Yes**  to confirm that you want to continue the deletion.

    **Figure  1**  Deleting a Node Pool<a name="fig12491145671314"></a>  
    ![](figures/deleting-a-node-pool.png "deleting-a-node-pool")


