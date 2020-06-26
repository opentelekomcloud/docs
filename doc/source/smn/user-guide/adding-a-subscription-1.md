# Adding a Subscription<a name="smn_ug_0008"></a>

## Scenario<a name="section3499028611828"></a>

To deliver messages published to a topic to endpoints, you must add the subscription endpoints to the topic. Endpoints can be email addresses, phone numbers, message queues, and HTTP/HTTPS URLs. After you add endpoints to the topic and the subscribers confirm the subscription, they are able to receive messages published to the topic.

You can add multiple subscriptions to each topic. This section describes how to add subscriptions to a topic you created or one to which you have been granted permissions and how to delete subscriptions.

## To Add a Subscription<a name="section66624127194914"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  on the upper left to select the desired region and project.
3.  In the  **Application**  category, click  **Simple Message Notification**.

    The SMN console is displayed.

4.  In the navigation pane, choose  **Subscriptions**.

5.  Click  **Add Subscription**.

    The  **Add Subscription**  box is displayed.

    **Figure  1**  Add Subscription<a name="fig3586058616227"></a>  
    ![](figures/add-subscription.png "add-subscription")

6.  Specify the required subscription information.
    1.  Click  ![](figures/icon-plus.png)  beside the  **Topic Name**  box to select a topic.
    2.  Specify the subscription protocol and endpoints.

        **Table  1**  Required subscription information

        <a name="table2272876216264"></a>
        <table><thead align="left"><tr id="row4550804216264"><th class="cellrowborder" valign="top" width="18.990000000000002%" id="mcps1.2.3.1.1"><p id="p5005312516264"><a name="p5005312516264"></a><a name="p5005312516264"></a><strong id="b5030070116264"><a name="b5030070116264"></a><a name="b5030070116264"></a>Parameter</strong></p>
        </th>
        <th class="cellrowborder" valign="top" width="81.01%" id="mcps1.2.3.1.2"><p id="p4861508816264"><a name="p4861508816264"></a><a name="p4861508816264"></a><strong id="b2777129716264"><a name="b2777129716264"></a><a name="b2777129716264"></a>Description</strong></p>
        </th>
        </tr>
        </thead>
        <tbody><tr id="row9669750155910"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p1384519585597"><a name="p1384519585597"></a><a name="p1384519585597"></a>Topic Name</p>
        </td>
        <td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.2.3.1.2 "><p id="p167015504594"><a name="p167015504594"></a><a name="p167015504594"></a>Name of the topic to subscribe to</p>
        </td>
        </tr>
        <tr id="row153044716264"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p5558394516264"><a name="p5558394516264"></a><a name="p5558394516264"></a>Protocol</p>
        </td>
        <td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.2.3.1.2 "><p id="en-us_topic_0043394871_p34500824131839"><a name="en-us_topic_0043394871_p34500824131839"></a><a name="en-us_topic_0043394871_p34500824131839"></a>Protocol the subscription endpoints support. The available options include <strong id="b2041793552202137"><a name="b2041793552202137"></a><a name="b2041793552202137"></a>SMS</strong>, <strong id="b842352706202512"><a name="b842352706202512"></a><a name="b842352706202512"></a>DMS</strong>, <strong id="b84235270610165"><a name="b84235270610165"></a><a name="b84235270610165"></a>Email</strong>, <strong id="b842352706101613"><a name="b842352706101613"></a><a name="b842352706101613"></a>HTTP</strong>, and <strong id="b842352706101618"><a name="b842352706101618"></a><a name="b842352706101618"></a>HTTPS</strong>.</p>
        </td>
        </tr>
        <tr id="row3620920716264"><td class="cellrowborder" valign="top" width="18.990000000000002%" headers="mcps1.2.3.1.1 "><p id="p1377403016264"><a name="p1377403016264"></a><a name="p1377403016264"></a>Endpoint</p>
        </td>
        <td class="cellrowborder" valign="top" width="81.01%" headers="mcps1.2.3.1.2 "><p id="p4204778416264"><a name="p4204778416264"></a><a name="p4204778416264"></a>Subscription endpoint. You can enter up to 10 SMS, email, HTTP, or HTTPS endpoints, one in each line.</p>
        <a name="ul4684327816264"></a><a name="ul4684327816264"></a><ul id="ul4684327816264"><li><strong id="b979883229152813"><a name="b979883229152813"></a><a name="b979883229152813"></a>SMS</strong>: Enter one or more valid phone numbers.<p id="p5119305416264"><a name="p5119305416264"></a><a name="p5119305416264"></a>The phone number is preceded by a plus sign (+) and a country code.</p>
        <p id="p5808430716264"><a name="p5808430716264"></a><a name="p5808430716264"></a>Example:</p>
        <p id="p6487584816264"><a name="p6487584816264"></a><a name="p6487584816264"></a><strong id="b84235270614502"><a name="b84235270614502"></a><a name="b84235270614502"></a>+4900000000</strong></p>
        <p id="p4701172816264"><a name="p4701172816264"></a><a name="p4701172816264"></a><strong id="b84235270614505"><a name="b84235270614505"></a><a name="b84235270614505"></a>+4900000001</strong></p>
        <p id="p2045237016264"><a name="p2045237016264"></a><a name="p2045237016264"></a><strong id="b84235270614509"><a name="b84235270614509"></a><a name="b84235270614509"></a>+4900000002</strong></p>
        <p id="p4985360916264"><a name="p4985360916264"></a><a name="p4985360916264"></a><strong id="b842352706145012"><a name="b842352706145012"></a><a name="b842352706145012"></a>+4900000003</strong></p>
        </li><li><strong id="b213535384154035"><a name="b213535384154035"></a><a name="b213535384154035"></a>Email</strong>: Enter one or more valid email addresses.<p id="p92860116264"><a name="p92860116264"></a><a name="p92860116264"></a>Example:</p>
        <p id="p835741116264"><a name="p835741116264"></a><a name="p835741116264"></a><strong id="b842352706145031"><a name="b842352706145031"></a><a name="b842352706145031"></a>username1@example.com</strong></p>
        <p id="p810783916264"><a name="p810783916264"></a><a name="p810783916264"></a><strong id="b842352706145038"><a name="b842352706145038"></a><a name="b842352706145038"></a>username2@example.com</strong></p>
        </li><li><strong id="b84235270691358"><a name="b84235270691358"></a><a name="b84235270691358"></a>HTTP</strong> or <strong id="b8423527069146"><a name="b8423527069146"></a><a name="b8423527069146"></a>HTTPS</strong>: Enter one or more public network URLs.<p id="p5275525916264"><a name="p5275525916264"></a><a name="p5275525916264"></a>Example:</p>
        <p id="p503528316264"><a name="p503528316264"></a><a name="p503528316264"></a><strong id="b842352706145047"><a name="b842352706145047"></a><a name="b842352706145047"></a>http://example1.com/notification/action</strong></p>
        <p id="p4531755416264"><a name="p4531755416264"></a><a name="p4531755416264"></a><strong id="b842352706145051"><a name="b842352706145051"></a><a name="b842352706145051"></a>http://example2.com/notification/action</strong></p>
        </li><li><strong id="b842352706203344"><a name="b842352706203344"></a><a name="b842352706203344"></a>DMS</strong>: Click <a name="image188793502465"></a><a name="image188793502465"></a><span><img id="image188793502465" src="figures/icon-plus.png"></span> to select a message queue. Ensure that the queue policy grants the <strong id="b8423527061693"><a name="b8423527061693"></a><a name="b8423527061693"></a>DMS:ProduceMessages</strong> permission to SMN. For details, see "Managing Queue Policies" in the <em id="i842352697152551"><a name="i842352697152551"></a><a name="i842352697152551"></a>Distributed Message Service User Guide</em>.</li></ul>
        </td>
        </tr>
        </tbody>
        </table>

7.  Click  **OK**.

    The subscription you added is displayed in the subscription list.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   To prevent malicious users from attacking subscription endpoints, SMN limits the number of confirmation messages that can be sent to an endpoint within a specified period of time. For details, see section  [Control on Subscription Confirmation Traffic](control-on-subscription-confirmation-traffic.md).  
    >-   SMN does not check whether subscription endpoints exist when you add subscriptions. However, subscribers will not receive notification messages until they confirm their subscriptions.  
    >-   The token is valid only for 48 hours. Therefore, subscribers must confirm subscriptions within that time.  


