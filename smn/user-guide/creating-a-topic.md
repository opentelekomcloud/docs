# Creating a Topic<a name="en-us_topic_0043961401"></a>

## Scenario<a name="section5231877317314"></a>

A topic is a specified event to publish messages and subscribe to notifications. It serves as a message sending channel, where publishers and subscribers can interact with each other.

## To Create a Topic<a name="section141512514421"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application**  category, click  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Topics**.

    The  **Topics**  page is displayed.

5.  Click  **Create Topic**.

    The  **Create Topic**  box is displayed.

    **Figure  1**  Create Topic<a name="fig63880443104346"></a>  
    ![](figures/create-topic.png "create-topic")

6.  Enter a topic name and display name.

    **Table  1**  Information required for creating a topic

    <a name="en-us_topic_0043394871_table9567729153632"></a>
    <table><thead align="left"><tr id="en-us_topic_0043394871_row46643153153632"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.3.1.1"><p id="en-us_topic_0043394871_p45773798153632"><a name="en-us_topic_0043394871_p45773798153632"></a><a name="en-us_topic_0043394871_p45773798153632"></a><strong id="en-us_topic_0043394871_b4942326616041"><a name="en-us_topic_0043394871_b4942326616041"></a><a name="en-us_topic_0043394871_b4942326616041"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79%" id="mcps1.2.3.1.2"><p id="en-us_topic_0043394871_p16690171153632"><a name="en-us_topic_0043394871_p16690171153632"></a><a name="en-us_topic_0043394871_p16690171153632"></a><strong id="en-us_topic_0043394871_b4386163916041"><a name="en-us_topic_0043394871_b4386163916041"></a><a name="en-us_topic_0043394871_b4386163916041"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043394871_row15993813153632"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043394871_p41631540153632"><a name="en-us_topic_0043394871_p41631540153632"></a><a name="en-us_topic_0043394871_p41631540153632"></a>Topic Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043394871_p44258107153632"><a name="en-us_topic_0043394871_p44258107153632"></a><a name="en-us_topic_0043394871_p44258107153632"></a>Topic name, which:</p>
    <a name="en-us_topic_0043394871_ul40971925153757"></a><a name="en-us_topic_0043394871_ul40971925153757"></a><ul id="en-us_topic_0043394871_ul40971925153757"><li>Contains only letters, numerals, hyphens (-), and underscores (_) and starts with a letter or numeral.</li><li>Is a string of 1 to 255 characters.</li><li>Must be unique and cannot be modified once the topic is created.</li></ul>
    </td>
    </tr>
    <tr id="row1798615142421"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p1025213190423"><a name="p1025213190423"></a><a name="p1025213190423"></a>Display Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p1881782917426"><a name="p1881782917426"></a><a name="p1881782917426"></a>Message sender name, which must be less than 192 bytes.</p>
    <div class="note" id="note13186621175918"><a name="note13186621175918"></a><a name="note13186621175918"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p0186821165916"><a name="p0186821165916"></a><a name="p0186821165916"></a>After you specify a display name, the sender in email messages will be presented as <em id="i1306384680"><a name="i1306384680"></a><a name="i1306384680"></a>Display name</em><strong id="b1698617597"><a name="b1698617597"></a><a name="b1698617597"></a>&lt;username@example.com&gt;</strong>. Otherwise, the sender will be <strong id="b1444431809"><a name="b1444431809"></a><a name="b1444431809"></a>username@example.com</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="row101210019315"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="p0121302312"><a name="p0121302312"></a><a name="p0121302312"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="p712190143113"><a name="p712190143113"></a><a name="p712190143113"></a>Tags consist of keys and values. They identify cloud resources so that you can easily categorize and search for your resources.</p>
    <a name="ul584116317458"></a><a name="ul584116317458"></a><ul id="ul584116317458"><li>A key or value is composed of letters, numerals, special characters -_@ and cannot start or end with a space. A key contains 36 characters at most, and a value contains 43 characters at most.</li><li>You can add up to 10 tags for each topic.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK.**

    The topic you created is displayed in the topic list. The system generates a topic URN, which is the unique resource identifier of the topic and cannot be changed.

8.  Click the name of the topic to view its details, including the subscriptions, URN, and display name.

