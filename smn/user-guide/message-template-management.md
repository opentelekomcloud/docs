# Message Template Management<a name="en-us_topic_0043394889"></a>

## Scenario<a name="section3499028611828"></a>

Message templates contain fixed and changeable content and can be used to send messages quickly. When you publish a message using a template, you can specify values for variables in the template.

Message templates are grouped by template name. You can create templates for different protocols using the same template name. You must specify the default protocol in any template name, or the system will not allow you to publish messages using that template name. When sending messages using a template, SMN tries to match different types of subscribers to the template protocols. If there is no template for a specified protocol, SMN will use the default template to send messages to subscribers of that protocol.

This section describes how to publish messages using a template.

## To Create a Message Template<a name="section66624127194914"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application**  category, click  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Message Templates**.
5.  Click  **Create Message Template**.

    The  **Create Message Template**  box is displayed.

    **Figure  1**  Create Message Template<a name="fig18154514124448"></a>  
    ![](figures/create-message-template.png "create-message-template")

6.  Specify the template name, protocol, and content.

    **Table  1**  Parameters required for creating a message template

    <a name="table9567729153632"></a>
    <table><thead align="left"><tr id="row46643153153632"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.3.1.1"><p id="p45773798153632"><a name="p45773798153632"></a><a name="p45773798153632"></a><strong id="b633727016234"><a name="b633727016234"></a><a name="b633727016234"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80.25999999999999%" id="mcps1.2.3.1.2"><p id="p16690171153632"><a name="p16690171153632"></a><a name="p16690171153632"></a><strong id="b4355688916234"><a name="b4355688916234"></a><a name="b4355688916234"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="row15993813153632"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="p43710295164421"><a name="p43710295164421"></a><a name="p43710295164421"></a>Template Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p44258107153632"><a name="p44258107153632"></a><a name="p44258107153632"></a>Template name, which:</p>
    <a name="ul40971925153757"></a><a name="ul40971925153757"></a><ul id="ul40971925153757"><li>Contains letters, numerals, underscores (_), and hyphens (-) and starts with a letter or numeral.</li><li>Is a character string 1 to 64 bytes long.</li><li>Cannot be modified once the template is created.</li></ul>
    </td>
    </tr>
    <tr id="row62778644153632"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="p27643693164446"><a name="p27643693164446"></a><a name="p27643693164446"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p40584374104257"><a name="p40584374104257"></a><a name="p40584374104257"></a>Endpoint protocol of the template, which cannot be changed once the template is created</p>
    <p id="p43586774153632"><a name="p43586774153632"></a><a name="p43586774153632"></a>The value can be <strong id="b2108805878143347"><a name="b2108805878143347"></a><a name="b2108805878143347"></a>Default</strong>, <strong id="b1095921216143347"><a name="b1095921216143347"></a><a name="b1095921216143347"></a>SMS</strong>, <strong id="b218424467143347"><a name="b218424467143347"></a><a name="b218424467143347"></a>HTTP</strong>, <strong id="b1369851447143347"><a name="b1369851447143347"></a><a name="b1369851447143347"></a>HTTPS</strong>, <strong id="b84235270615203"><a name="b84235270615203"></a><a name="b84235270615203"></a>DMS</strong>, or <strong id="b1100015765143347"><a name="b1100015765143347"></a><a name="b1100015765143347"></a>Email</strong>.</p>
    <p id="p12468638104149"><a name="p12468638104149"></a><a name="p12468638104149"></a>If you do not specify a protocol, the <strong id="b842352706204357"><a name="b842352706204357"></a><a name="b842352706204357"></a>Default</strong> protocol is used.</p>
    </td>
    </tr>
    <tr id="row23418429162644"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="p32830814164510"><a name="p32830814164510"></a><a name="p32830814164510"></a>Content</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><p id="p5697748316413"><a name="p5697748316413"></a><a name="p5697748316413"></a>Template content</p>
    <p id="p29184378155831"><a name="p29184378155831"></a><a name="p29184378155831"></a>You can use variables as placeholders. Before you send messages using the template, SMN replaces the variables with the message content you specify. A variable is a string of up to 21 characters. It may contain upper- or lower-case letters, numerals, hyphens (-), underscores (_), and periods (.) and must start with a letter or numeral.</p>
    <p id="p40948298155833"><a name="p40948298155833"></a><a name="p40948298155833"></a>The message template must meet the following requirements:</p>
    <a name="ul24327004104111"></a><a name="ul24327004104111"></a><ul id="ul24327004104111"><li>The template supports plain text only.</li><li>The template content cannot be left blank and cannot exceed 256 KB.</li></ul>
    <a name="ul36563140155946"></a><a name="ul36563140155946"></a><ul id="ul36563140155946"><li>A template can contain up to 90 non-repeating variables or 256 variables counting the repeated ones. </li><li>When you send messages using a template, the message content you specify for each variable cannot exceed 1 KB.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    For example, the template information is as follows:

    -   **Template Name**:  **tem\_001**
    -   **Protocol**:  **Default**
    -   **Content**:  **The Arts and Crafts Exposition will be held from \{startdate\} through \{enddate\}. We sincerely invite you to join us.** 

        **Figure  2**  Create Message Template<a name="en-us_topic_0044170770_fig17426812318"></a>  
        ![](figures/create-message-template-0.png "create-message-template-0")

7.  Click  **OK**.

    The template you created is displayed in the template list.


## To Modify a Template<a name="section10611263152222"></a>

1.  Locate the template to be modified in the template list.
2.  Click  **Modify**  under  **Operation**  to change its content.

## To Delete a Template<a name="section14249229153134"></a>

1.  Locate the template to be deleted in the template list.
2.  Click  **Delete**  under  **Operation**.

