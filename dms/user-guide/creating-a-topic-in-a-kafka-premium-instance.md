# Creating a Topic in a Kafka Premium Instance<a name="EN-US_TOPIC_0143117242"></a>

After creating a Kafka premium instance, you must create a topic in the instance for creating and retrieving messages.

## Prerequisites<a name="section11712186286"></a>

-   A Kafka premium instance has been created.
-   The status of the Kafka premium instance is  **Running**.

## Procedure<a name="section0249155910409"></a>

1.  Log in to the management console.
2.  Choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
3.  In the navigation pane, choose  **Kafka Premium**.
4.  Click the name of a Kafka premium instance for which you want to create a topic.

    The instance details page is displayed.

5.  Click the  **Topic Management**  tab, and click  **Create Topic**.

    The  **Create Topic**  page is displayed.

6.  Specify the topic parameters listed in the following table.

    **Table  1**  Topic parameters

    <a name="table186364410350"></a>
    <table><thead align="left"><tr id="row66474473513"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p7641944173520"><a name="p7641944173520"></a><a name="p7641944173520"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p264154419353"><a name="p264154419353"></a><a name="p264154419353"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row8641444183514"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p12649444358"><a name="p12649444358"></a><a name="p12649444358"></a>Topic Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p886312445210"><a name="p886312445210"></a><a name="p886312445210"></a>When you create a topic, a default topic name is generated, which you can change as required. A topic name contains 4 to 64 characters. Only letters, digits, underscores (_), and hyphens (-) are allowed.</p>
    <p id="p19863142405214"><a name="p19863142405214"></a><a name="p19863142405214"></a>The topic name cannot be changed after a topic is created.</p>
    </td>
    </tr>
    <tr id="row196494414358"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p10641644103512"><a name="p10641644103512"></a><a name="p10641644103512"></a>Partitions</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1064194443517"><a name="p1064194443517"></a><a name="p1064194443517"></a>A larger number of partitions for a topic indicates more messages retrieved concurrently.</p>
    <p id="p515812152115"><a name="p515812152115"></a><a name="p515812152115"></a>If this parameter is set to <strong id="b67319136262"><a name="b67319136262"></a><a name="b67319136262"></a>1</strong>, messages will be retrieved in a FIFO order.</p>
    <p id="p14572074216"><a name="p14572074216"></a><a name="p14572074216"></a>Value range: 1 to 20</p>
    <p id="p49191315152018"><a name="p49191315152018"></a><a name="p49191315152018"></a>Default value: <strong id="b81014141505"><a name="b81014141505"></a><a name="b81014141505"></a>3</strong></p>
    </td>
    </tr>
    <tr id="row764164413519"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p2647442357"><a name="p2647442357"></a><a name="p2647442357"></a>Replicas</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p133039601910"><a name="p133039601910"></a><a name="p133039601910"></a>A higher number of replicas indicates higher reliability. Data is automatically backed up on each replica. After one Kafka broker becomes faulty, data is still available on other brokers.</p>
    <p id="p155911384258"><a name="p155911384258"></a><a name="p155911384258"></a>If this parameter is set to <strong id="b127623594269"><a name="b127623594269"></a><a name="b127623594269"></a>1</strong>, only one set of data is available.</p>
    <p id="p1420827152712"><a name="p1420827152712"></a><a name="p1420827152712"></a>Value range: 1 to 3</p>
    <p id="p74201827182717"><a name="p74201827182717"></a><a name="p74201827182717"></a>Default value: <strong id="b71501319501"><a name="b71501319501"></a><a name="b71501319501"></a>3</strong></p>
    </td>
    </tr>
    <tr id="row464194417358"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p136464453511"><a name="p136464453511"></a><a name="p136464453511"></a>Aging Time (h)</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p166412448357"><a name="p166412448357"></a><a name="p166412448357"></a>The number of hours for which messages will be preserved in a topic. Messages older than that period will be deleted and deleted messages are not retrievable to consumer groups.</p>
    <p id="p1367151412910"><a name="p1367151412910"></a><a name="p1367151412910"></a>Value range: 1 to 168</p>
    <p id="p885211915294"><a name="p885211915294"></a><a name="p885211915294"></a>Default value: <strong id="b4135223304"><a name="b4135223304"></a><a name="b4135223304"></a>72</strong></p>
    </td>
    </tr>
    <tr id="row24651137132"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p646518311134"><a name="p646518311134"></a><a name="p646518311134"></a>Synchronous Replication</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1744502415435"><a name="p1744502415435"></a><a name="p1744502415435"></a>A message is returned to the client only after the message creation request has been received and the message has been acknowledged by all replicas.</p>
    <p id="p188951712431"><a name="p188951712431"></a><a name="p188951712431"></a>After enabling synchronous replication, configure acks = –1 on the client for this function to take effect.</p>
    </td>
    </tr>
    <tr id="row564184403515"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p9641944123515"><a name="p9641944123515"></a><a name="p9641944123515"></a>Synchronous Flushing</p>
    </td>
    <td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1164144413516"><a name="p1164144413516"></a><a name="p1164144413516"></a>An indicator of whether a message is immediately flushed to disk once it is created.</p>
    <p id="p121511193711"><a name="p121511193711"></a><a name="p121511193711"></a>On: A message is immediately flushed to disk once it is created, featuring higher reliability.</p>
    <p id="p0289112616719"><a name="p0289112616719"></a><a name="p0289112616719"></a>Off: A message is stored in the memory instead of being immediately flushed to disk once it is created.</p>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK**.

