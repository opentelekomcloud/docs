# Publishing a Text Message<a name="en-us_topic_0043961403"></a>

## Scenario<a name="section3152890014563"></a>

After you publish a text message to a topic, SMN will deliver the message to all confirmed subscription endpoints in the topic.

## Prerequisites<a name="section30431634133546"></a>

Subscribers in the topic must have confirmed the subscription, or they will not be able to receive any messages.

## To Publish a Text Message<a name="section48379737125756"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application**  category, click  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Topics**.

    The  **Topics**  page is displayed.

5.  In the topic list, locate the topic to which you need to publish a message and click  **Publish Message**  under  **Operation**.
6.  Configure the required parameters according to  [Table 1](#table616755201736). The topic name is provided by default and cannot be changed.

    **Table  1**  Parameters required for publishing a message

    <a name="table616755201736"></a>
    <table><thead align="left"><tr id="row584325251736"><th class="cellrowborder" valign="top" width="30.259999999999998%" id="mcps1.2.3.1.1"><p id="p354141231736"><a name="p354141231736"></a><a name="p354141231736"></a><strong id="b593529816129"><a name="b593529816129"></a><a name="b593529816129"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="69.74000000000001%" id="mcps1.2.3.1.2"><p id="p470923481736"><a name="p470923481736"></a><a name="p470923481736"></a><strong id="b1099715916129"><a name="b1099715916129"></a><a name="b1099715916129"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row24022921736"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p603679291736"><a name="p603679291736"></a><a name="p603679291736"></a>Subject</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p519144811736"><a name="p519144811736"></a><a name="p519144811736"></a>(Optional) The message subject is a string of less than 512 bytes.</p>
    </td>
    </tr>
    <tr id="row645771531736"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p633668671736"><a name="p633668671736"></a><a name="p633668671736"></a>Message Format</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p16675104132026"><a name="p16675104132026"></a><a name="p16675104132026"></a>The message format can be <strong id="b842352706151447"><a name="b842352706151447"></a><a name="b842352706151447"></a>Text</strong>, <strong id="b842352706151510"><a name="b842352706151510"></a><a name="b842352706151510"></a>JSON</strong>, or <strong id="b84235270615161"><a name="b84235270615161"></a><a name="b84235270615161"></a>Template</strong>. In this context, you need to select <strong id="b1892485612159"><a name="b1892485612159"></a><a name="b1892485612159"></a>Text</strong>.</p>
    <a name="ul37120136132048"></a><a name="ul37120136132048"></a><ul id="ul37120136132048"><li><strong id="b84235270616514"><a name="b84235270616514"></a><a name="b84235270616514"></a>Text</strong>: common text message</li><li><strong id="b842352706165215"><a name="b842352706165215"></a><a name="b842352706165215"></a>JSON</strong>: JSON message</li><li><strong id="b3824744584352"><a name="b3824744584352"></a><a name="b3824744584352"></a>Template</strong>: template message. For details, see <a href="message-template-management.md">Message Template Management</a>.</li></ul>
    </td>
    </tr>
    <tr id="row45964848125529"><td class="cellrowborder" valign="top" width="30.259999999999998%" headers="mcps1.2.3.1.1 "><p id="p5280417412564"><a name="p5280417412564"></a><a name="p5280417412564"></a>Message</p>
    </td>
    <td class="cellrowborder" valign="top" width="69.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p55246607125529"><a name="p55246607125529"></a><a name="p55246607125529"></a>This is the message content, which cannot be left blank nor exceed 256 KB.</p>
    </td>
    </tr>
    </tbody>
    </table>

    The following figure shows an example text message.

    **Figure  1**  Text message example<a name="fig804716611238"></a>  
    ![](figures/text-message-example.png "text-message-example")

7.  Click  **OK**.

    SMN delivers your message to all subscription endpoints. For details about messages for different protocols, see  [Messages of Different Protocols](messages-of-different-protocols.md).


