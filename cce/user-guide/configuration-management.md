# Configuration Management<a name="cce_01_0213"></a>

To facilitate the management of Kubernetes configuration parameters in a cluster, the cloud provides the configuration function. This function allows you to perform in-depth configuration on core components.

## Constraints<a name="section12438124825414"></a>

This function can be used only in clusters of v1.15 or later.

## Procedure<a name="section031621519364"></a>

1.  Log in to the CCE Console. In the navigation pane, choose  **Resource Management**  \>  **Clusters**.
2.  Choose  **More**  \>  **Configuration**.
3.  On the Configuration page on the right, change the values of the following Kubernetes parameters:

    **Table  1**  Kubernetes parameters

    <a name="table15912122874"></a>
    <table><thead align="left"><tr id="row1653411231576"><th class="cellrowborder" valign="top" width="28.38716128387161%" id="mcps1.2.5.1.1"><p id="p17534172319711"><a name="p17534172319711"></a><a name="p17534172319711"></a>Component</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.476952304769522%" id="mcps1.2.5.1.2"><p id="p15534152315714"><a name="p15534152315714"></a><a name="p15534152315714"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="30.416958304169583%" id="mcps1.2.5.1.3"><p id="p253411231373"><a name="p253411231373"></a><a name="p253411231373"></a>Description</p>
    </th>
    <th class="cellrowborder" valign="top" width="10.718928107189281%" id="mcps1.2.5.1.4"><p id="p953422311711"><a name="p953422311711"></a><a name="p953422311711"></a>Default Value</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row423504023719"><td class="cellrowborder" rowspan="5" valign="top" width="28.38716128387161%" headers="mcps1.2.5.1.1 "><p id="p162273403377"><a name="p162273403377"></a><a name="p162273403377"></a>kube-apiserver</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.476952304769522%" headers="mcps1.2.5.1.2 "><p id="p1722734019373"><a name="p1722734019373"></a><a name="p1722734019373"></a>default-not-ready-toleration-seconds</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.416958304169583%" headers="mcps1.2.5.1.3 "><p id="p1922774053719"><a name="p1922774053719"></a><a name="p1922774053719"></a>Default interval of the toleration for notReady:NoExecute.</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.718928107189281%" headers="mcps1.2.5.1.4 "><p id="p22341740123710"><a name="p22341740123710"></a><a name="p22341740123710"></a>300</p>
    </td>
    </tr>
    <tr id="row11235144013371"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1822764043720"><a name="p1822764043720"></a><a name="p1822764043720"></a>default-unreachable-toleration-seconds</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p18227040163720"><a name="p18227040163720"></a><a name="p18227040163720"></a>Default interval of the toleration for unreachable:NoExecute.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p16234134019372"><a name="p16234134019372"></a><a name="p16234134019372"></a>300</p>
    </td>
    </tr>
    <tr id="row112351240143715"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p192271440133715"><a name="p192271440133715"></a><a name="p192271440133715"></a>max-mutating-requests-inflight</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p16228740133718"><a name="p16228740133718"></a><a name="p16228740133718"></a>Maximum number of mutating requests in flight at a given time.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p8234184015372"><a name="p8234184015372"></a><a name="p8234184015372"></a>1000</p>
    </td>
    </tr>
    <tr id="row1235940123713"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2228240133716"><a name="p2228240133716"></a><a name="p2228240133716"></a>max-requests-inflight</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p202281040113720"><a name="p202281040113720"></a><a name="p202281040113720"></a>Maximum number of non-mutating requests in flight at a given time.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p62341140173713"><a name="p62341140173713"></a><a name="p62341140173713"></a>2000</p>
    </td>
    </tr>
    <tr id="row1022218002118"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1722314092113"><a name="p1722314092113"></a><a name="p1722314092113"></a>service-node-port-range</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p8682165221319"><a name="p8682165221319"></a><a name="p8682165221319"></a>Range of node port numbers.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p102239082112"><a name="p102239082112"></a><a name="p102239082112"></a>30000-32767</p>
    </td>
    </tr>
    <tr id="row423534010377"><td class="cellrowborder" rowspan="12" valign="top" width="28.38716128387161%" headers="mcps1.2.5.1.1 "><p id="p422844053719"><a name="p422844053719"></a><a name="p422844053719"></a>kube-controller-manager</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.476952304769522%" headers="mcps1.2.5.1.2 "><p id="p522864018376"><a name="p522864018376"></a><a name="p522864018376"></a>concurrent-deployment-syncs</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.416958304169583%" headers="mcps1.2.5.1.3 "><p id="p1228124011378"><a name="p1228124011378"></a><a name="p1228124011378"></a>Number of Deployments that are allowed to synchronize concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.718928107189281%" headers="mcps1.2.5.1.4 "><p id="p123454053712"><a name="p123454053712"></a><a name="p123454053712"></a>5</p>
    </td>
    </tr>
    <tr id="row11235540113710"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p15228184073716"><a name="p15228184073716"></a><a name="p15228184073716"></a>concurrent-endpoint-syncs</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p422811409376"><a name="p422811409376"></a><a name="p422811409376"></a>Number of endpoint synchronization operations that will be done concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p823414017374"><a name="p823414017374"></a><a name="p823414017374"></a>5</p>
    </td>
    </tr>
    <tr id="row19235134093716"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p13228134053714"><a name="p13228134053714"></a><a name="p13228134053714"></a>concurrent-gc-syncs</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p722824043718"><a name="p722824043718"></a><a name="p722824043718"></a>Number of garbage collector workers that are allowed to synchronize concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1323494063712"><a name="p1323494063712"></a><a name="p1323494063712"></a>20</p>
    </td>
    </tr>
    <tr id="row11235140113712"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p52283406378"><a name="p52283406378"></a><a name="p52283406378"></a>concurrent-namespace-syncs</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p12286409378"><a name="p12286409378"></a><a name="p12286409378"></a>Number of namespaces that are allowed to synchronize concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p923414013720"><a name="p923414013720"></a><a name="p923414013720"></a>10</p>
    </td>
    </tr>
    <tr id="row17235174063715"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p2022815406372"><a name="p2022815406372"></a><a name="p2022815406372"></a>concurrent-replicaset-syncs</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p022874011376"><a name="p022874011376"></a><a name="p022874011376"></a>Number of ReplicaSets that are allowed to synchronize concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p823424073716"><a name="p823424073716"></a><a name="p823424073716"></a>5</p>
    </td>
    </tr>
    <tr id="row32350405377"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p1522894003714"><a name="p1522894003714"></a><a name="p1522894003714"></a>concurrent-resource-quota-syncs</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1522812404375"><a name="p1522812404375"></a><a name="p1522812404375"></a>Number of resource quotas that are allowed to synchronize concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p192341740153715"><a name="p192341740153715"></a><a name="p192341740153715"></a>5</p>
    </td>
    </tr>
    <tr id="row14235184015375"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p10228540143713"><a name="p10228540143713"></a><a name="p10228540143713"></a>concurrent-service-syncs</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p222834053712"><a name="p222834053712"></a><a name="p222834053712"></a>Number of Services that are allowed to synchronize concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1223464053719"><a name="p1223464053719"></a><a name="p1223464053719"></a>10</p>
    </td>
    </tr>
    <tr id="row16235134063718"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p822814013379"><a name="p822814013379"></a><a name="p822814013379"></a>concurrent-serviceaccount-token-syncs</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p42281740193719"><a name="p42281740193719"></a><a name="p42281740193719"></a>Number of service account tokens that are allowed to synchronize concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p19234164016378"><a name="p19234164016378"></a><a name="p19234164016378"></a>5</p>
    </td>
    </tr>
    <tr id="row72351340183713"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p6228140163711"><a name="p6228140163711"></a><a name="p6228140163711"></a>concurrent-ttl-after-finished-syncs</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p122894014376"><a name="p122894014376"></a><a name="p122894014376"></a>Number of TTL-after-finished controller workers that are allowed to synchronize concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p32342404373"><a name="p32342404373"></a><a name="p32342404373"></a>5</p>
    </td>
    </tr>
    <tr id="row12235164083715"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p3228540123718"><a name="p3228540123718"></a><a name="p3228540123718"></a>concurrent_rc_syncs</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p4228134015370"><a name="p4228134015370"></a><a name="p4228134015370"></a>Number of replication controllers that are allowed to synchronize concurrently.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1223417404376"><a name="p1223417404376"></a><a name="p1223417404376"></a>5</p>
    </td>
    </tr>
    <tr id="row42356400377"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p142281940163719"><a name="p142281940163719"></a><a name="p142281940163719"></a>kube-api-qps</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p1122844083713"><a name="p1122844083713"></a><a name="p1122844083713"></a>QPS communicating with kube-apiserver.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p1234184013713"><a name="p1234184013713"></a><a name="p1234184013713"></a>100</p>
    </td>
    </tr>
    <tr id="row16235740153717"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p17228164083710"><a name="p17228164083710"></a><a name="p17228164083710"></a>kube-api-burst</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p6228184073713"><a name="p6228184073713"></a><a name="p6228184073713"></a>Burst communicating with kube-apiserver.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p162341040133718"><a name="p162341040133718"></a><a name="p162341040133718"></a>100</p>
    </td>
    </tr>
    <tr id="row8235140133713"><td class="cellrowborder" rowspan="2" valign="top" width="28.38716128387161%" headers="mcps1.2.5.1.1 "><p id="p6228640173715"><a name="p6228640173715"></a><a name="p6228640173715"></a>kube-scheduler</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.476952304769522%" headers="mcps1.2.5.1.2 "><p id="p2228164063715"><a name="p2228164063715"></a><a name="p2228164063715"></a>kube-api-qps</p>
    </td>
    <td class="cellrowborder" valign="top" width="30.416958304169583%" headers="mcps1.2.5.1.3 "><p id="p1322864013711"><a name="p1322864013711"></a><a name="p1322864013711"></a>QPS communicating with kube-apiserver.</p>
    </td>
    <td class="cellrowborder" valign="top" width="10.718928107189281%" headers="mcps1.2.5.1.4 "><p id="p10234144033710"><a name="p10234144033710"></a><a name="p10234144033710"></a>100</p>
    </td>
    </tr>
    <tr id="row1323515403372"><td class="cellrowborder" valign="top" headers="mcps1.2.5.1.1 "><p id="p722834053716"><a name="p722834053716"></a><a name="p722834053716"></a>kube-api-burst</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.2 "><p id="p7228240153710"><a name="p7228240153710"></a><a name="p7228240153710"></a>Burst communicating with kube-apiserver.</p>
    </td>
    <td class="cellrowborder" valign="top" headers="mcps1.2.5.1.3 "><p id="p11234154043711"><a name="p11234154043711"></a><a name="p11234154043711"></a>100</p>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **OK**.

## References<a name="section185642613239"></a>

-   [kube-apiserver](https://v1-15.docs.kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver)
-   [kube-controller-manager](https://v1-15.docs.kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager)
-   [kube-scheduler](https://v1-15.docs.kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler)

