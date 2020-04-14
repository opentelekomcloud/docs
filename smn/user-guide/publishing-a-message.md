# Publishing a Message<a name="smn_ug_0004"></a>

After you learn the basic concepts in SMN, you can start to create a topic, add subscriptions to the topic, and publish messages on the SMN console or by calling RESTful APIs provided by SMN. For details about SMN APIs, see the  _Simple Message Notification API Reference_.

[Figure 1](#fig208091627152213)  shows the process to publish a message to a topic.

**Figure  1**  Process to publish a message<a name="fig208091627152213"></a>  
![](figures/process-to-publish-a-message.png "process-to-publish-a-message")

## Scenario<a name="section121666257522"></a>

If you need to send similar messages repeatedly, you can create a message template which contains fixed and changeable content. Every time you send messages using the template, you only have to replace changeable content. For example, your organization holds expositions regularly and needs to notify relevant people of the dates, you can create a message template containing date variables and other fixed content.

## Step 1. Create a Topic<a name="section1848118288254"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application**  category, click  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Topics**.

    The  **Topics**  page is displayed.

5.  Click  **Create Topic**.

    The  **Create Topic**  box is displayed.

    **Figure  2**  Create Topic<a name="en-us_topic_0043961401_fig63880443104346"></a>  
    ![](figures/create-topic.png "create-topic")

6.  Enter a topic name and display name.

    **Table  1**  Information required for creating a topic

    <a name="en-us_topic_0043961401_en-us_topic_0043394871_table9567729153632"></a>
    <table><thead align="left"><tr id="en-us_topic_0043961401_en-us_topic_0043394871_row46643153153632"><th class="cellrowborder" valign="top" width="21%" id="mcps1.2.3.1.1"><p id="en-us_topic_0043961401_en-us_topic_0043394871_p45773798153632"><a name="en-us_topic_0043961401_en-us_topic_0043394871_p45773798153632"></a><a name="en-us_topic_0043961401_en-us_topic_0043394871_p45773798153632"></a><strong id="en-us_topic_0043961401_en-us_topic_0043394871_b4942326616041"><a name="en-us_topic_0043961401_en-us_topic_0043394871_b4942326616041"></a><a name="en-us_topic_0043961401_en-us_topic_0043394871_b4942326616041"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="79%" id="mcps1.2.3.1.2"><p id="en-us_topic_0043961401_en-us_topic_0043394871_p16690171153632"><a name="en-us_topic_0043961401_en-us_topic_0043394871_p16690171153632"></a><a name="en-us_topic_0043961401_en-us_topic_0043394871_p16690171153632"></a><strong id="en-us_topic_0043961401_en-us_topic_0043394871_b4386163916041"><a name="en-us_topic_0043961401_en-us_topic_0043394871_b4386163916041"></a><a name="en-us_topic_0043961401_en-us_topic_0043394871_b4386163916041"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043961401_en-us_topic_0043394871_row15993813153632"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043961401_en-us_topic_0043394871_p41631540153632"><a name="en-us_topic_0043961401_en-us_topic_0043394871_p41631540153632"></a><a name="en-us_topic_0043961401_en-us_topic_0043394871_p41631540153632"></a>Topic Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043961401_en-us_topic_0043394871_p44258107153632"><a name="en-us_topic_0043961401_en-us_topic_0043394871_p44258107153632"></a><a name="en-us_topic_0043961401_en-us_topic_0043394871_p44258107153632"></a>Topic name, which:</p>
    <a name="en-us_topic_0043961401_en-us_topic_0043394871_ul40971925153757"></a><a name="en-us_topic_0043961401_en-us_topic_0043394871_ul40971925153757"></a><ul id="en-us_topic_0043961401_en-us_topic_0043394871_ul40971925153757"><li>Contains only letters, numerals, hyphens (-), and underscores (_) and starts with a letter or numeral.</li><li>Is a string of 1 to 255 characters.</li><li>Must be unique and cannot be modified once the topic is created.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0043961401_row1798615142421"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043961401_p1025213190423"><a name="en-us_topic_0043961401_p1025213190423"></a><a name="en-us_topic_0043961401_p1025213190423"></a>Display Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043961401_p1881782917426"><a name="en-us_topic_0043961401_p1881782917426"></a><a name="en-us_topic_0043961401_p1881782917426"></a>Message sender name, which must be less than 192 bytes.</p>
    <div class="note" id="en-us_topic_0043961401_note13186621175918"><a name="en-us_topic_0043961401_note13186621175918"></a><a name="en-us_topic_0043961401_note13186621175918"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="en-us_topic_0043961401_p0186821165916"><a name="en-us_topic_0043961401_p0186821165916"></a><a name="en-us_topic_0043961401_p0186821165916"></a>After you specify a display name, the sender in email messages will be presented as <em id="en-us_topic_0043961401_i1306384680"><a name="en-us_topic_0043961401_i1306384680"></a><a name="en-us_topic_0043961401_i1306384680"></a>Display name</em><strong id="en-us_topic_0043961401_b1698617597"><a name="en-us_topic_0043961401_b1698617597"></a><a name="en-us_topic_0043961401_b1698617597"></a>&lt;username@example.com&gt;</strong>. Otherwise, the sender will be <strong id="en-us_topic_0043961401_b1444431809"><a name="en-us_topic_0043961401_b1444431809"></a><a name="en-us_topic_0043961401_b1444431809"></a>username@example.com</strong>.</p>
    </div></div>
    </td>
    </tr>
    <tr id="en-us_topic_0043961401_row101210019315"><td class="cellrowborder" valign="top" width="21%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043961401_p0121302312"><a name="en-us_topic_0043961401_p0121302312"></a><a name="en-us_topic_0043961401_p0121302312"></a>Tag</p>
    </td>
    <td class="cellrowborder" valign="top" width="79%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043961401_p712190143113"><a name="en-us_topic_0043961401_p712190143113"></a><a name="en-us_topic_0043961401_p712190143113"></a>Tags consist of keys and values. They identify cloud resources so that you can easily categorize and search for your resources.</p>
    <a name="en-us_topic_0043961401_ul584116317458"></a><a name="en-us_topic_0043961401_ul584116317458"></a><ul id="en-us_topic_0043961401_ul584116317458"><li>A key or value is composed of letters, numerals, special characters -_@ and cannot start or end with a space. A key contains 36 characters at most, and a value contains 43 characters at most.</li><li>You can add up to 10 tags for each topic.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

7.  Click  **OK.**

    The topic you created is displayed in the topic list. The system generates a topic URN, which is the unique resource identifier of the topic and cannot be changed.

8.  Click the name of the topic to view its details, including the subscriptions, URN, and display name.

## Step 2. Add a Subscription<a name="section10105949172514"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application**  category, click  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Subscriptions**.

5.  Click  **Add Subscription**.

    The  **Add Subscription**  box is displayed.

    **Figure  3**  Add Subscription<a name="smn_ug_0008_fig3586058616227"></a>  
    ![](figures/add-subscription.png "add-subscription")

6.  Specify the required subscription information.
    1.  Click  ![](figures/icon-plus.png)  beside the  **Topic Name**  box to select a topic.
    2.  Specify the subscription protocol and endpoints.

        **Table  2**  Required subscription information

        <a name="smn_ug_0008_table2272876216264"></a>
        <table><thead align="left"><tr id="smn_ug_0008_row4550804216264"><th class="cellrowborder" valign="top" width="18.990000000000002%" id="mcps1.2.3.1.1"><p id="smn_ug_0008_p5005312516264"><a name="smn_ug_0008_p5005312516264"></a><a name="smn_ug_0008_p5005312516264"></a><strong id="smn_ug_0008_b5030070116264"><a name="smn_ug_0008_b5030070116264"></a><a name="smn_ug_0008_b5030070116264"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="81.01%" id="mcps1.2.3.1.2"><p id="smn_ug_0008_p4861508816264"><a name="smn_ug_0008_p4861508816264"></a><a name="smn_ug_0008_p4861508816264"></a><strong id="smn_ug_0008_b2777129716264"><a name="smn_ug_0008_b2777129716264"></a><a name="smn_ug_0008_b2777129716264"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="smn_ug_0008_row9669750155910"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.2.3.1.1 "><p id="smn_ug_0008_p1384519585597"><a name="smn_ug_0008_p1384519585597"></a><a name="smn_ug_0008_p1384519585597"></a>Topic Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.2.3.1.2 "><p id="smn_ug_0008_p167015504594"><a name="smn_ug_0008_p167015504594"></a><a name="smn_ug_0008_p167015504594"></a>Name of the topic to subscribe to</p>
        </td>
        </tr>
        <tr id="smn_ug_0008_row153044716264"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.2.3.1.1 "><p id="smn_ug_0008_p5558394516264"><a name="smn_ug_0008_p5558394516264"></a><a name="smn_ug_0008_p5558394516264"></a>Protocol</p>
        </td>
        <td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.2.3.1.2 "><p id="smn_ug_0008_en-us_topic_0043394871_p34500824131839"><a name="smn_ug_0008_en-us_topic_0043394871_p34500824131839"></a><a name="smn_ug_0008_en-us_topic_0043394871_p34500824131839"></a>Protocol the subscription endpoints support. The available options include <strong id="smn_ug_0008_b2041793552202137"><a name="smn_ug_0008_b2041793552202137"></a><a name="smn_ug_0008_b2041793552202137"></a>SMS</strong>, <strong id="smn_ug_0008_b842352706202512"><a name="smn_ug_0008_b842352706202512"></a><a name="smn_ug_0008_b842352706202512"></a>DMS</strong>, <strong id="smn_ug_0008_b84235270610165"><a name="smn_ug_0008_b84235270610165"></a><a name="smn_ug_0008_b84235270610165"></a>Email</strong>, <strong id="smn_ug_0008_b842352706101613"><a name="smn_ug_0008_b842352706101613"></a><a name="smn_ug_0008_b842352706101613"></a>HTTP</strong>, and <strong id="smn_ug_0008_b842352706101618"><a name="smn_ug_0008_b842352706101618"></a><a name="smn_ug_0008_b842352706101618"></a>HTTPS</strong>.</p>
        </td>
        </tr>
        <tr id="smn_ug_0008_row3620920716264"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.2.3.1.1 "><p id="smn_ug_0008_p1377403016264"><a name="smn_ug_0008_p1377403016264"></a><a name="smn_ug_0008_p1377403016264"></a>Endpoint</p>
        </td>
        <td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.2.3.1.2 "><p id="smn_ug_0008_p4204778416264"><a name="smn_ug_0008_p4204778416264"></a><a name="smn_ug_0008_p4204778416264"></a>Subscription endpoint. You can enter up to 10 SMS, email, HTTP, or HTTPS endpoints, one in each line.</p>
        <a name="smn_ug_0008_ul4684327816264"></a><a name="smn_ug_0008_ul4684327816264"></a><ul id="smn_ug_0008_ul4684327816264"><li><strong id="smn_ug_0008_b979883229152813"><a name="smn_ug_0008_b979883229152813"></a><a name="smn_ug_0008_b979883229152813"></a>SMS</strong>: Enter one or more valid phone numbers.<p id="smn_ug_0008_p5119305416264"><a name="smn_ug_0008_p5119305416264"></a><a name="smn_ug_0008_p5119305416264"></a>The phone number is preceded by a plus sign (+) and a country code.</p>
        <p id="smn_ug_0008_p5808430716264"><a name="smn_ug_0008_p5808430716264"></a><a name="smn_ug_0008_p5808430716264"></a>Example:</p>
        <p id="smn_ug_0008_p6487584816264"><a name="smn_ug_0008_p6487584816264"></a><a name="smn_ug_0008_p6487584816264"></a><strong id="smn_ug_0008_b84235270614502"><a name="smn_ug_0008_b84235270614502"></a><a name="smn_ug_0008_b84235270614502"></a>+4900000000</strong></p>
        <p id="smn_ug_0008_p4701172816264"><a name="smn_ug_0008_p4701172816264"></a><a name="smn_ug_0008_p4701172816264"></a><strong id="smn_ug_0008_b84235270614505"><a name="smn_ug_0008_b84235270614505"></a><a name="smn_ug_0008_b84235270614505"></a>+4900000001</strong></p>
        <p id="smn_ug_0008_p2045237016264"><a name="smn_ug_0008_p2045237016264"></a><a name="smn_ug_0008_p2045237016264"></a><strong id="smn_ug_0008_b84235270614509"><a name="smn_ug_0008_b84235270614509"></a><a name="smn_ug_0008_b84235270614509"></a>+4900000002</strong></p>
        <p id="smn_ug_0008_p4985360916264"><a name="smn_ug_0008_p4985360916264"></a><a name="smn_ug_0008_p4985360916264"></a><strong id="smn_ug_0008_b842352706145012"><a name="smn_ug_0008_b842352706145012"></a><a name="smn_ug_0008_b842352706145012"></a>+4900000003</strong></p>
        </li><li><strong id="smn_ug_0008_b213535384154035"><a name="smn_ug_0008_b213535384154035"></a><a name="smn_ug_0008_b213535384154035"></a>Email</strong>: Enter one or more valid email addresses.<p id="smn_ug_0008_p92860116264"><a name="smn_ug_0008_p92860116264"></a><a name="smn_ug_0008_p92860116264"></a>Example:</p>
        <p id="smn_ug_0008_p835741116264"><a name="smn_ug_0008_p835741116264"></a><a name="smn_ug_0008_p835741116264"></a><strong id="smn_ug_0008_b842352706145031"><a name="smn_ug_0008_b842352706145031"></a><a name="smn_ug_0008_b842352706145031"></a>username1@example.com</strong></p>
        <p id="smn_ug_0008_p810783916264"><a name="smn_ug_0008_p810783916264"></a><a name="smn_ug_0008_p810783916264"></a><strong id="smn_ug_0008_b842352706145038"><a name="smn_ug_0008_b842352706145038"></a><a name="smn_ug_0008_b842352706145038"></a>username2@example.com</strong></p>
        </li><li><strong id="smn_ug_0008_b84235270691358"><a name="smn_ug_0008_b84235270691358"></a><a name="smn_ug_0008_b84235270691358"></a>HTTP</strong> or <strong id="smn_ug_0008_b8423527069146"><a name="smn_ug_0008_b8423527069146"></a><a name="smn_ug_0008_b8423527069146"></a>HTTPS</strong>: Enter one or more public network URLs.<p id="smn_ug_0008_p5275525916264"><a name="smn_ug_0008_p5275525916264"></a><a name="smn_ug_0008_p5275525916264"></a>Example:</p>
        <p id="smn_ug_0008_p503528316264"><a name="smn_ug_0008_p503528316264"></a><a name="smn_ug_0008_p503528316264"></a><strong id="smn_ug_0008_b842352706145047"><a name="smn_ug_0008_b842352706145047"></a><a name="smn_ug_0008_b842352706145047"></a>http://example1.com/notification/action</strong></p>
        <p id="smn_ug_0008_p4531755416264"><a name="smn_ug_0008_p4531755416264"></a><a name="smn_ug_0008_p4531755416264"></a><strong id="smn_ug_0008_b842352706145051"><a name="smn_ug_0008_b842352706145051"></a><a name="smn_ug_0008_b842352706145051"></a>http://example2.com/notification/action</strong></p>
        </li><li><strong id="smn_ug_0008_b842352706203344"><a name="smn_ug_0008_b842352706203344"></a><a name="smn_ug_0008_b842352706203344"></a>DMS</strong>: Click <a name="smn_ug_0008_image188793502465"></a><a name="smn_ug_0008_image188793502465"></a><span><img id="smn_ug_0008_image188793502465" src="figures/icon-plus.png"></span> to select a message queue. Ensure that the queue policy grants the <strong id="smn_ug_0008_b8423527061693"><a name="smn_ug_0008_b8423527061693"></a><a name="smn_ug_0008_b8423527061693"></a>DMS:ProduceMessages</strong> permission to SMN. For details, see "Managing Queue Policies" in the <em id="smn_ug_0008_i842352697152551"><a name="smn_ug_0008_i842352697152551"></a><a name="smn_ug_0008_i842352697152551"></a>Distributed Message Service User Guide</em>.</li></ul>
        </td>
        </tr>
        </tbody>
        </table>

7.  Click  **OK**.

    The subscription you added is displayed in the subscription list.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   To prevent malicious users from attacking subscription endpoints, SMN limits the number of confirmation messages that can be sent to an endpoint within a specified period of time. For details, see section  [Control on Subscription Confirmation Traffic](control-on-subscription-confirmation-traffic.md).  
    >-   SMN does not check whether subscription endpoints exist when you add subscriptions. However, subscribers will not receive notification messages until they confirm their subscriptions.  
    >-   The token is valid only for 48 hours. Therefore, subscribers must confirm subscriptions within that time.  


## Step 3. Create a Message Template<a name="section09021127162619"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application**  category, click  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Message Templates**.
5.  Click  **Create Message Template**.

    The  **Create Message Template**  box is displayed.

    **Figure  4**  Create Message Template<a name="en-us_topic_0043394889_fig18154514124448"></a>  
    ![](figures/create-message-template.png "create-message-template")

6.  Specify the template name, protocol, and content.

    **Table  3**  Parameters required for creating a message template

    <a name="en-us_topic_0043394889_table9567729153632"></a>
    <table><thead align="left"><tr id="en-us_topic_0043394889_row46643153153632"><th class="cellrowborder" valign="top" width="19.74%" id="mcps1.2.3.1.1"><p id="en-us_topic_0043394889_p45773798153632"><a name="en-us_topic_0043394889_p45773798153632"></a><a name="en-us_topic_0043394889_p45773798153632"></a><strong id="en-us_topic_0043394889_b633727016234"><a name="en-us_topic_0043394889_b633727016234"></a><a name="en-us_topic_0043394889_b633727016234"></a>Parameter</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="80.25999999999999%" id="mcps1.2.3.1.2"><p id="en-us_topic_0043394889_p16690171153632"><a name="en-us_topic_0043394889_p16690171153632"></a><a name="en-us_topic_0043394889_p16690171153632"></a><strong id="en-us_topic_0043394889_b4355688916234"><a name="en-us_topic_0043394889_b4355688916234"></a><a name="en-us_topic_0043394889_b4355688916234"></a>Description</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="en-us_topic_0043394889_row15993813153632"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043394889_p43710295164421"><a name="en-us_topic_0043394889_p43710295164421"></a><a name="en-us_topic_0043394889_p43710295164421"></a>Template Name</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043394889_p44258107153632"><a name="en-us_topic_0043394889_p44258107153632"></a><a name="en-us_topic_0043394889_p44258107153632"></a>Template name, which:</p>
    <a name="en-us_topic_0043394889_ul40971925153757"></a><a name="en-us_topic_0043394889_ul40971925153757"></a><ul id="en-us_topic_0043394889_ul40971925153757"><li>Contains letters, numerals, underscores (_), and hyphens (-) and starts with a letter or numeral.</li><li>Is a character string 1 to 64 bytes long.</li><li>Cannot be modified once the template is created.</li></ul>
    </td>
    </tr>
    <tr id="en-us_topic_0043394889_row62778644153632"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043394889_p27643693164446"><a name="en-us_topic_0043394889_p27643693164446"></a><a name="en-us_topic_0043394889_p27643693164446"></a>Protocol</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043394889_p40584374104257"><a name="en-us_topic_0043394889_p40584374104257"></a><a name="en-us_topic_0043394889_p40584374104257"></a>Endpoint protocol of the template, which cannot be changed once the template is created</p>
    <p id="en-us_topic_0043394889_p43586774153632"><a name="en-us_topic_0043394889_p43586774153632"></a><a name="en-us_topic_0043394889_p43586774153632"></a>The value can be <strong id="en-us_topic_0043394889_b2108805878143347"><a name="en-us_topic_0043394889_b2108805878143347"></a><a name="en-us_topic_0043394889_b2108805878143347"></a>Default</strong>, <strong id="en-us_topic_0043394889_b1095921216143347"><a name="en-us_topic_0043394889_b1095921216143347"></a><a name="en-us_topic_0043394889_b1095921216143347"></a>SMS</strong>, <strong id="en-us_topic_0043394889_b218424467143347"><a name="en-us_topic_0043394889_b218424467143347"></a><a name="en-us_topic_0043394889_b218424467143347"></a>HTTP</strong>, <strong id="en-us_topic_0043394889_b1369851447143347"><a name="en-us_topic_0043394889_b1369851447143347"></a><a name="en-us_topic_0043394889_b1369851447143347"></a>HTTPS</strong>, <strong id="en-us_topic_0043394889_b84235270615203"><a name="en-us_topic_0043394889_b84235270615203"></a><a name="en-us_topic_0043394889_b84235270615203"></a>DMS</strong>, or <strong id="en-us_topic_0043394889_b1100015765143347"><a name="en-us_topic_0043394889_b1100015765143347"></a><a name="en-us_topic_0043394889_b1100015765143347"></a>Email</strong>.</p>
    <p id="en-us_topic_0043394889_p12468638104149"><a name="en-us_topic_0043394889_p12468638104149"></a><a name="en-us_topic_0043394889_p12468638104149"></a>If you do not specify a protocol, the <strong id="en-us_topic_0043394889_b842352706204357"><a name="en-us_topic_0043394889_b842352706204357"></a><a name="en-us_topic_0043394889_b842352706204357"></a>Default</strong> protocol is used.</p>
    </td>
    </tr>
    <tr id="en-us_topic_0043394889_row23418429162644"><td class="cellrowborder" valign="top" width="19.74%" headers="mcps1.2.3.1.1 "><p id="en-us_topic_0043394889_p32830814164510"><a name="en-us_topic_0043394889_p32830814164510"></a><a name="en-us_topic_0043394889_p32830814164510"></a>Content</p>
    </td>
    <td class="cellrowborder" valign="top" width="80.25999999999999%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043394889_p5697748316413"><a name="en-us_topic_0043394889_p5697748316413"></a><a name="en-us_topic_0043394889_p5697748316413"></a>Template content</p>
    <p id="en-us_topic_0043394889_p29184378155831"><a name="en-us_topic_0043394889_p29184378155831"></a><a name="en-us_topic_0043394889_p29184378155831"></a>You can use variables as placeholders. Before you send messages using the template, SMN replaces the variables with the message content you specify. A variable is a string of up to 21 characters. It may contain upper- or lower-case letters, numerals, hyphens (-), underscores (_), and periods (.) and must start with a letter or numeral.</p>
    <p id="en-us_topic_0043394889_p40948298155833"><a name="en-us_topic_0043394889_p40948298155833"></a><a name="en-us_topic_0043394889_p40948298155833"></a>The message template must meet the following requirements:</p>
    <a name="en-us_topic_0043394889_ul24327004104111"></a><a name="en-us_topic_0043394889_ul24327004104111"></a><ul id="en-us_topic_0043394889_ul24327004104111"><li>The template supports plain text only.</li><li>The template content cannot be left blank and cannot exceed 256 KB.</li></ul>
    <a name="en-us_topic_0043394889_ul36563140155946"></a><a name="en-us_topic_0043394889_ul36563140155946"></a><ul id="en-us_topic_0043394889_ul36563140155946"><li>A template can contain up to 90 non-repeating variables or 256 variables counting the repeated ones. </li><li>When you send messages using a template, the message content you specify for each variable cannot exceed 1 KB.</li></ul>
    </td>
    </tr>
    </tbody>
    </table>

    For example, the template information is as follows:

    -   **Template Name**:  **tem\_001**
    -   **Protocol**:  **Default**
    -   **Content**:  **The Arts and Crafts Exposition will be held from \{startdate\} through \{enddate\}. We sincerely invite you to join us.** 

        **Figure  5**  Create Message Template<a name="en-us_topic_0043394889_en-us_topic_0044170770_fig17426812318"></a>  
        ![](figures/create-message-template-0.png "create-message-template-0")

7.  Click  **OK**.

    The template you created is displayed in the template list.


## Step 4. Publish a Template Message<a name="section19496217192711"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application**  category, click  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Topics**.

    The  **Topics**  page is displayed.

5.  In the topic list, locate the topic to which you need to publish a message and click  **Publish Message**  under  **Operation**.
6.  Configure the required parameters. The topic name is provided by default and cannot be changed.

    Select  **Template**  for  **Message Format**. Then, manually type the template content in the  **Message**  box or click  **Generate Template Message**  to generate it automatically. The template message content cannot exceed 256 KB.

    -   If you choose to manually type the template message, see  [Template Message Format](template-message-format.md)  for detailed requirements.
    -   If you choose to automatically generate the template message, proceed with steps  [7](#en-us_topic_0044170770_li37303092212221)  through  [10](#en-us_topic_0044170770_li3929025721230).

7.  <a name="en-us_topic_0044170770_li37303092212221"></a>Click  **Generate Template Message**.
8.  Select a template name, for example,  **tem\_001**, and enter values for the variables.

    The system replaces the variables with the message content you specified. The protocols configured in the template are displayed after each variable. In the example shown in the following figure, only the default protocol is specified in  **tem\_001**. Therefore, all confirmed subscribers in the topic will receive the message content in the default template. 

    **Figure  6**  Generate Template Message<a name="en-us_topic_0044170770_fig365979611560"></a>  
    ![](figures/generate-template-message.png "generate-template-message")

9.  Click the  **Preview**  tab to preview the message.

    In this example, the message generated is "The Arts and Crafts Exposition will be held from February 10 through February 21. We sincerely invite you to join us." 

    **Figure  7**  Previewing the template message<a name="en-us_topic_0044170770_fig4102954615137"></a>  
    ![](figures/previewing-the-template-message.png "previewing-the-template-message")

10. <a name="en-us_topic_0044170770_li3929025721230"></a>Click  **OK**.

    The message that is generated contains the template name and variables.

    **Figure  8**  Template message example<a name="en-us_topic_0044170770_fig20843289192615"></a>  
    ![](figures/template-message-example.png "template-message-example")

11. Click  **OK**.

    SMN delivers your message to all subscription endpoints. For details about messages for different protocols, see  [Messages of Different Protocols](messages-of-different-protocols.md).


## Step 5. Receive the Message<a name="section099510497272"></a>

Subscription endpoints of different protocols receive different messages.

-   Email protocol

    Subscription endpoints are email addresses.

    Email messages contain the message subject, content, and a link to unsubscribe.

    **Figure  9**  Email message<a name="fig1804131982"></a>  
    ![](figures/email-message.png "email-message")

-   HTTP/HTTPS protocol

    Subscription endpoints are public network URLs. For details, see section "HTTP/HTTPS Messages" in the  _Simple Message Notification User Guide_.

-   SMS protocol

    Subscription endpoints are phone numbers.

    SMS messages contain only the message content.

-   DMS protocol

    Subscription endpoints are message queues.

    Message content is not displayed in message queues. You can access the DMS console and check the number of messages in a queue. After you publish a message to a message queue, the number in that queue will increase.


