# Creating a Topic<a name="EN-US_TOPIC_0085216039"></a>

## Scenarios<a name="en-us_topic_0043961401_section5231877317314"></a>

A topic is a specific type of event in which messages are published and to which end users subscribe for notifications. It serves as a message sending channel, where publishers and subscribers can interact with each other.

In this topic, you can create a topic that belongs to you.

## Creating a Topic<a name="section1076552614204"></a>

1.  Log in to the management console.
2.  In the upper left corner, select a region and a project.
3.  Under  **Application**, select  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Topics**.

    The  **Topics**  page is displayed.

5.  Click  **Create Topic**.

    The  **Create Topic**  dialog box is displayed.

    **Figure  1**  Create Topic<a name="fig677272615204"></a>  
    ![](figures/create-topic.png "create-topic")

6.  Enter a topic name and display name \(topic description\).

    **Table  1**  Parameters required for creating a topic

    <a name="table2780162682018"></a>
    <table><thead align="left"><tr id="row11780182617204"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.3.1.1"><p id="p147801826132010"><a name="p147801826132010"></a><a name="p147801826132010"></a><strong id="en-us_topic_0043394871_b4942326616041"><a name="en-us_topic_0043394871_b4942326616041"></a><a name="en-us_topic_0043394871_b4942326616041"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79%" id="mcps1.2.3.1.2"><p id="p2780142692015"><a name="p2780142692015"></a><a name="p2780142692015"></a><strong id="en-us_topic_0043394871_b4386163916041"><a name="en-us_topic_0043394871_b4386163916041"></a><a name="en-us_topic_0043394871_b4386163916041"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row10787102682020"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p1778702662011"><a name="p1778702662011"></a><a name="p1778702662011"></a>Topic Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p6787192642019"><a name="p6787192642019"></a><a name="p6787192642019"></a>Specifies the topic name, which</p>
    <a name="ul177876268209"></a><a name="ul177876268209"></a><ul id="ul177876268209"><li>Contains only upper or lower case letters, digits, hyphens (-), and underscores (_) and must start with a letter or a digit.</li><li>Is a string of 1 to 255 characters.</li><li>Must be unique and cannot be modified once the topic is created.</li></ul>
    </td>
    </tr>
    <tr id="row207882266206"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p478862602016"><a name="p478862602016"></a><a name="p478862602016"></a>Display Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p2078972611207"><a name="p2078972611207"></a><a name="p2078972611207"></a>Specifies the message sender name, which must be less than 192 bytes.</p>
    <div class="note" id="note6789326122019"><a name="note6789326122019"></a><a name="note6789326122019"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p187891526172015"><a name="p187891526172015"></a><a name="p187891526172015"></a>After you specify a display name, the sender in email messages will be presented as <em id="i1573597911"><a name="i1573597911"></a><a name="i1573597911"></a>Display name</em><strong id="b791130249"><a name="b791130249"></a><a name="b791130249"></a>&lt;username@example.com&gt;</strong>. Otherwise, the sender will be <strong id="b4249103"><a name="b4249103"></a><a name="b4249103"></a>username@example.com</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row1078920269206"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p18789122662014"><a name="p18789122662014"></a><a name="p18789122662014"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p137907264203"><a name="p137907264203"></a><a name="p137907264203"></a>Tags identify cloud resources so that they can be categorized easily and searched quickly.</p>
    <a name="ul6790126172016"></a><a name="ul6790126172016"></a><ul id="ul6790126172016"><li>You can enter a maximum of 36 and 43 characters for <strong id="b29249928818232"><a name="b29249928818232"></a><a name="b29249928818232"></a>Key</strong> and <strong id="b84235270618241"><a name="b84235270618241"></a><a name="b84235270618241"></a>Value</strong>, respectively. Both <strong id="b84235270618049"><a name="b84235270618049"></a><a name="b84235270618049"></a>Key</strong> and <strong id="b8423527061838"><a name="b8423527061838"></a><a name="b8423527061838"></a>Value</strong> cannot start or end with a space and cannot contain any of the following characters: is equal to (=), asterisk (*), is less than (&lt;), is greater than (&gt;), backslash (\), comma (,), delimiter (|), and slash (/).</li><li>Each topic supports up to 10 tags.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK.**

    The topic you created is displayed in the topic list.

    After a topic is created, the system generates a topic uniform resource name \(URN\), which uniquely identifies the topic and cannot be changed.

8.  Click a topic name to view the topic details and the total number of topic subscriptions.

## Follow-up Operations<a name="section18957020115719"></a>

After creating a topic, you need to  [add subscriptions](adding-subscriptions.md). After the subscriptions have been confirmed, alarm notifications can be sent to the subscribers via SMS messages or emails.

