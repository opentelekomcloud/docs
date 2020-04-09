# Network Policy<a name="cce_01_0059"></a>

CCE has enhanced the  Kubernetes-based  network policy  function, allowing network isolation in a  cluster  by configuring network policies. This means that a  firewall  can be set between  instances  \(pods\).

## What Are Network Policies?<a name="section322222112010"></a>

As the service logic becomes increasingly complex, many applications require network calls between modules. Traditional external firewalls or application-based firewalls cannot meet the requirements. Network policies are urgently needed between modules, service logic layers, or functional teams in a large cluster.

CCE has enhanced the Kubernetes-based network policy function, allowing network isolation in a cluster by configuring network policies. This means that a firewall can be set between instances \(pods\).

For example, to make a payment system accessible only to specified components for security purposes, you can configure network policies.

## Precautions<a name="section146088501667"></a>

-   Network policies are not supported in the VPC Router network model.
-   If no network policies have been configured for a workload, such as  **workload1**, other workloads in the same cluster can access  **workload1**.

## Creating a Network Policy<a name="section19894131402011"></a>

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Network**. On the  **Network Policies**  tab page, click  **Create Network Policy**.
    -   **Network Policy Name**: Specify a network policy name.
    -   **Cluster Name**: Select a cluster to which the network policy belongs.
    -   **Namespace**: Select a namespace in which the network policy is applied.
    -   **Workload**

        Click  **Select Workload**. In the dialog box that is displayed, select a workload for which the network policy is to be created, for example,  **workload1**. Then click  **OK**.

    -   **Rules**: Click  **Add Rule**, set the parameters listed in  [Table 1](#table26919378234), and click  **OK**.

        **Table  1**  Parameters for adding a rule

        <a name="table26919378234"></a>
        <table><thead align="left"><tr id="row117013742315"><th class="cellrowborder" valign="top" width="29.21%" id="mcps1.2.3.1.1"><p id="p10701937122312"><a name="p10701937122312"></a><a name="p10701937122312"></a>Parameter</p>
        </th>
        <th class="cellrowborder" valign="top" width="70.78999999999999%" id="mcps1.2.3.1.2"><p id="p1970937162314"><a name="p1970937162314"></a><a name="p1970937162314"></a>Description</p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row17073752310"><td class="cellrowborder" valign="top" width="29.21%" headers="mcps1.2.3.1.1 "><p id="p1770337122315"><a name="p1770337122315"></a><a name="p1770337122315"></a>Direction</p>
        </td>
        <td class="cellrowborder" valign="top" width="70.78999999999999%" headers="mcps1.2.3.1.2 "><p id="p19701374230"><a name="p19701374230"></a><a name="p19701374230"></a>Only <strong id="b33045118549"><a name="b33045118549"></a><a name="b33045118549"></a>Inbound</strong> is supported, indicating that the whitelisted workloads access the current workload (<strong id="b5304112541"><a name="b5304112541"></a><a name="b5304112541"></a>workload1</strong> in this example).</p>
        </td>
        </tr>
        <tr id="row0706372237"><td class="cellrowborder" valign="top" width="29.21%" headers="mcps1.2.3.1.1 "><p id="p1871103711232"><a name="p1871103711232"></a><a name="p1871103711232"></a>Protocol</p>
        </td>
        <td class="cellrowborder" valign="top" width="70.78999999999999%" headers="mcps1.2.3.1.2 "><p id="p77123712230"><a name="p77123712230"></a><a name="p77123712230"></a>Select a protocol used for workload access.</p>
        </td>
        </tr>
        <tr id="row141931728132819"><td class="cellrowborder" valign="top" width="29.21%" headers="mcps1.2.3.1.1 "><p id="p18193102819285"><a name="p18193102819285"></a><a name="p18193102819285"></a>Destination Container Port</p>
        </td>
        <td class="cellrowborder" valign="top" width="70.78999999999999%" headers="mcps1.2.3.1.2 "><p id="p219311287289"><a name="p219311287289"></a><a name="p219311287289"></a>Specify a port on which the workload in the container image listens. The Nginx workload listens on port 80.</p>
        <p id="p37005549297"><a name="p37005549297"></a><a name="p37005549297"></a>If no container port is specified, all ports can be accessed by default.</p>
        </td>
        </tr>
        <tr id="row10711637182318"><td class="cellrowborder" valign="top" width="29.21%" headers="mcps1.2.3.1.1 "><p id="p107120375238"><a name="p107120375238"></a><a name="p107120375238"></a>Whitelisted Workloads</p>
        </td>
        <td class="cellrowborder" valign="top" width="70.78999999999999%" headers="mcps1.2.3.1.2 "><p id="p157183711231"><a name="p157183711231"></a><a name="p157183711231"></a>Select other workloads that can access the current workload. These workloads will access the current workload at the destination container port.</p>
        <a name="ul28102117259"></a><a name="ul28102117259"></a><ul id="ul28102117259"><li><strong id="b20221455143919"><a name="b20221455143919"></a><a name="b20221455143919"></a>Namespace</strong>: All workloads in the selected namespace are added to the whitelist. That is, all workloads in the namespace can access workload A.</li><li><strong id="b6341557153910"><a name="b6341557153910"></a><a name="b6341557153910"></a>Workload</strong>: The selected workload can access workload A. Only other workloads in the same namespace as workload A can be selected.</li></ul>
        </td>
        </tr>
        </tbody>
        </table>

2.  Click  **Create**.
3.  Repeat the preceding steps to add more network policies for the current workload when other ports need to be accessed by some workloads.

    After the network policies are created, only the specified workloads or workloads in the specified namespaces can access the current workload.


## Configuring a Namespace-level Network Policy<a name="section7606272113"></a>

You can configure a namespace-level network policy by enabling network isolation.

By default,  **Network Isolation**  is disabled for  namespaces. For example, if network isolation is off for namespace  **default**,  **all pods in the current cluster**  can access the  **pods in namespace default**.

To prevent other pods from accessing the pods in namespace  **default**, perform the following steps:

1.  Log in to the CCE console. In the navigation pane, choose  **Resource Management**  \>  **Namespaces**.
2.  In the same row as the namespace \(for example,  **default**\) for which you will create a network policy, enable network isolation

    After network isolation is enabled, pods in namespace  **default**  can access each other but they cannot be accessed by pods in other namespaces.

    **Figure  1**  Namespace-level network policy<a name="fig13427151918417"></a>  
    ![](figures/namespace-level-network-policy-1.png "namespace-level-network-policy-1")


