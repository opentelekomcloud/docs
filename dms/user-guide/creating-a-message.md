# Creating a Message<a name="EN-US_TOPIC_0143117093"></a>

## Scenario<a name="section31665688"></a>

Messages can be sent to a chosen queue.

The size of each message, including the message body and attributes, cannot exceed 512 KB. The body includes the message content and a few bytes of additional JSON information.

If the Kafka SDK is used to create messages, the maximum size of a single message is 10 MB. If the DMS console is used to create messages, the maximum size of a single message is 512 KB.

## Prerequisites<a name="section16555740"></a>

A queue has been created.

## Procedure<a name="section0152726182917"></a>

1.  Log in to the management console.
2.  Click  ![](figures/project.png)  in the upper left corner to select a region and a project.
3.  Click  **Service List**, and choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
4.  In the navigation pane, choose Queue Manager.
5.  Open the  **Create Message**  dialog box using either of the methods:
    -   Method 1

        In the queue list, click  **Create Message**  in the same row as the queue to which messages will be sent.

    -   Method 2
        1.  Click the name of the queue to which messages will be sent.
        2.  Click  **Create Message**  in the upper right corner of the queue details page.

6.  Specify parameters as shown in  [Table 1](#table9868824195830).

    If you want to add attributes, specify  **Name**  and  **Value**, and then click  **Add**.

    **Table  1**  Parameter description

    <a name="table9868824195830"></a>
    <table><thead align="left"><tr id="row6064333195830"><th class="cellrowborder" valign="top" width="22.37%" id="mcps1.2.3.1.1"><p id="p58822814195830"><a name="p58822814195830"></a><a name="p58822814195830"></a>Parameter</p>
    </th>
    <th class="cellrowborder" valign="top" width="77.63%" id="mcps1.2.3.1.2"><p id="p67027522195830"><a name="p67027522195830"></a><a name="p67027522195830"></a>Description</p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row66376790195830"><td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.2.3.1.1 "><p id="p7810911195830"><a name="p7810911195830"></a><a name="p7810911195830"></a>Message Body</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.63%" headers="mcps1.2.3.1.2 "><p id="p28704089195830"><a name="p28704089195830"></a><a name="p28704089195830"></a>Body of the message to be sent.</p>
    <p id="p1887110705915"><a name="p1887110705915"></a><a name="p1887110705915"></a>When using the DMS console to send messages, characters that are reserved in the JSON format will be escaped in the message body content. For example, "it's not you, it's me" would be escaped to \"it's not you, it's me\".</p>
    </td>
    </tr>
    <tr id="row57010216195830"><td class="cellrowborder" valign="top" width="22.37%" headers="mcps1.2.3.1.1 "><p id="p54424782195830"><a name="p54424782195830"></a><a name="p54424782195830"></a>Message Attributes</p>
    </td>
    <td class="cellrowborder" valign="top" width="77.63%" headers="mcps1.2.3.1.2 "><p id="p3821334318"><a name="p3821334318"></a><a name="p3821334318"></a>Attribute of a message, which is composed of the name and value in the key-value format. Attributes are not part of the message body but are sent and retrieved along with it.</p>
    <p id="p15839125192016"><a name="p15839125192016"></a><a name="p15839125192016"></a>Attribute names are mandatory and must be unique in the same message.</p>
    <p id="p587323983813"><a name="p587323983813"></a><a name="p587323983813"></a>If you enter attribute names or values on the DMS console, spaces are allowed in attribute names and values, but not before and after them. For example, in DMS, "   ab c   " is converted to "ab c".</p>
    <div class="note" id="note27751511123111"><a name="note27751511123111"></a><a name="note27751511123111"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p7776181118317"><a name="p7776181118317"></a><a name="p7776181118317"></a>If you use APIs to access DMS, spaces are allowed in, before, and after attribute names and values.</p>
    </div></div>
    <p id="p5442945172011"><a name="p5442945172011"></a><a name="p5442945172011"></a>Message attributes are supplementary to the message body and can be sent and retrieved along with it. You can specify multiple message attributes, as long as the size of the message remains within 512 KB.</p>
    <p id="p2900171304519"><a name="p2900171304519"></a><a name="p2900171304519"></a>Only messages in standard queues have attributes. Messages in Kafka queues do not have attributes.</p>
    </td>
    </tr>
    </tbody>
    </table>

    Successfully added attributes will be displayed in the list. To delete an attribute, click  **Delete**  in the same row as the attribute.

7.  Click  **OK**.

    In the queue list, the value of  **Messages**  for the chosen queue will increment by one.

    In the consumer group list of the chosen queue, the value of  **Messages Available**  for those consumer groups will also increment by one if consumer groups exist for the queue.


