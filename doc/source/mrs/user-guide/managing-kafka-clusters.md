# Managing Kafka Clusters<a name="EN-US_TOPIC_0221415081"></a>

Kafka cluster management includes the following:

-   [Adding a Cluster on the KafkaManager Web UI](#section8713185103014)
-   [Updating Cluster Parameters](#section776745110472)
-   [Deleting a Cluster on the KafkaManager Web UI](#section656918369521)

## Adding a Cluster on the KafkaManager Web UI<a name="section8713185103014"></a>

After a Kafka cluster is created for the first time, a default Kafka cluster named  **my-cluster**  is created on the KafkaManager web UI. You can also add Kafka clusters that have been created on the MRS management console on the KafkaManager web UI to manage multiple Kafka clusters.

1.  Log in to the KafkaManager web UI.
2.  In the upper part of the page, choose  **Cluster**  \>  **Add Cluster**.

    **Figure  1**  Adding a cluster<a name="fig06211347173620"></a>  
    ![](figures/adding-a-cluster.png "adding-a-cluster")

3.  Set the cluster parameters. For the following parameters, refer to their example values. Retain the default values for other parameters.

    **Table  1**  Cluster parameters to be modified

    <a name="table19287112011164"></a>
    <table><thead align="left"><tr id="row142881620161613"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.1"><p id="p428832019167"><a name="p428832019167"></a><a name="p428832019167"></a><strong id="en-us_topic_0043021173_b8423527061470"><a name="en-us_topic_0043021173_b8423527061470"></a><a name="en-us_topic_0043021173_b8423527061470"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.2"><p id="p1728811208167"><a name="p1728811208167"></a><a name="p1728811208167"></a>Example Value</p>
    </th>
    <th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.2.4.1.3"><p id="p16288152012163"><a name="p16288152012163"></a><a name="p16288152012163"></a><strong id="b842352706134712"><a name="b842352706134712"></a><a name="b842352706134712"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row1328842018161"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p112881820151615"><a name="p112881820151615"></a><a name="p112881820151615"></a>Cluster Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p15288820191616"><a name="p15288820191616"></a><a name="p15288820191616"></a>mrs-demo</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p4288192015161"><a name="p4288192015161"></a><a name="p4288192015161"></a>Name of the cluster to be added on the KafkaManager web UI</p>
    </td>
    </tr>
    <tr id="row428816206164"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p1528819204161"><a name="p1528819204161"></a><a name="p1528819204161"></a>Cluster Zookeeper Hosts</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p569618424174"><a name="p569618424174"></a><a name="p569618424174"></a>zk1_ip:zk1_port, zk2_ip:zk2_port/kafka</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p62881220171610"><a name="p62881220171610"></a><a name="p62881220171610"></a>ZooKeeper address of the cluster to be added</p>
    </td>
    </tr>
    <tr id="row192882020131615"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p2288520111616"><a name="p2288520111616"></a><a name="p2288520111616"></a>Kafka Version</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1128892081611"><a name="p1128892081611"></a><a name="p1128892081611"></a>1.1.0</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p072102521813"><a name="p072102521813"></a><a name="p072102521813"></a>Kafka version of the cluster to be added. The default value is <strong id="b11192144825119"><a name="b11192144825119"></a><a name="b11192144825119"></a>1.1.0</strong>.</p>
    </td>
    </tr>
    <tr id="row1225617469305"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p102561146143014"><a name="p102561146143014"></a><a name="p102561146143014"></a>Enable JMX Polling (Set JMX_PORT env variable before starting kafka server)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p0256546113015"><a name="p0256546113015"></a><a name="p0256546113015"></a>Selected</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14256134613010"><a name="p14256134613010"></a><a name="p14256134613010"></a>-</p>
    </td>
    </tr>
    <tr id="row162881620111612"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p034693182215"><a name="p034693182215"></a><a name="p034693182215"></a>Poll consumer information (Not recommended for large # of consumers)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p144891512219"><a name="p144891512219"></a><a name="p144891512219"></a>Selected</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p19289720161616"><a name="p19289720161616"></a><a name="p19289720161616"></a>-</p>
    </td>
    </tr>
    <tr id="row228922016166"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p634693202212"><a name="p634693202212"></a><a name="p634693202212"></a>Enable Active OffsetCache (Not recommended for large # of consumers)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p1048715519225"><a name="p1048715519225"></a><a name="p1048715519225"></a>Selected</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p14289182017162"><a name="p14289182017162"></a><a name="p14289182017162"></a>-</p>
    </td>
    </tr>
    <tr id="row79341058112113"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p14935115817216"><a name="p14935115817216"></a><a name="p14935115817216"></a>Display Broker and Topic Size (only works after applying this patch)</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p10935458102110"><a name="p10935458102110"></a><a name="p10935458102110"></a>Selected</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><p id="p1693585822118"><a name="p1693585822118"></a><a name="p1693585822118"></a>-</p>
    </td>
    </tr>
    <tr id="row201616212229"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.1 "><p id="p10288182011169"><a name="p10288182011169"></a><a name="p10288182011169"></a>Security Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.2 "><p id="p162881620171616"><a name="p162881620171616"></a><a name="p162881620171616"></a>PLAINTEXT</p>
    </td>
    <td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.2.4.1.3 "><a name="ul1533223923116"></a><a name="ul1533223923116"></a><ul id="ul1533223923116"><li>For a Kafka cluster with Kerberos authentication enabled, select <strong id="b17110738195410"><a name="b17110738195410"></a><a name="b17110738195410"></a>SASL_PLAINTEXT</strong>.</li><li>For a Kafka cluster with Kerberos authentication disabled, select <strong id="b816372418559"><a name="b816372418559"></a><a name="b816372418559"></a>PLAINTEXT</strong>.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

4.  Click  **Save**.

## Updating Cluster Parameters<a name="section776745110472"></a>

1.  Log in to the KafkaManager web UI.
2.  Click  **Modify**  in the  **Operations**  column of the cluster.

    **Figure  2**  Updating cluster parameters<a name="fig6644193915811"></a>  
    ![](figures/updating-cluster-parameters.png "updating-cluster-parameters")

3.  Go to the cluster configuration page and modify cluster parameters.

## Deleting a Cluster on the KafkaManager Web UI<a name="section656918369521"></a>

1.  Log in to the KafkaManager web UI.
2.  Click  **Disable**  in the  **Operations**  column of the cluster.

    **Figure  3**  Disabling the cluster<a name="fig148908447119"></a>  
    ![](figures/disabling-the-cluster.png "disabling-the-cluster")

3.  When  **Delete**  or  **Enable**  is displayed in the  **Operations**  column on the cluster list page, click  **Delete**  to delete the cluster. You can also click  **Enable**  to enable the cluster.

    **Figure  4**  Enabling or deleting the cluster<a name="fig1388733119417"></a>  
    ![](figures/enabling-or-deleting-the-cluster.png "enabling-or-deleting-the-cluster")


