## Publishing a JSON Message

###Scenarios

In a JSON message, you can specify different message content for different protocols, including SMS, email, HTTP, and HTTPS. After you publish a JSON message to the topic, SMN will send the message to applicable subscription endpoints in the topic.

###Prerequisites

Subscribers of the topic have confirmed the subscription, or they will not be able to receive any messages.

###Publishing a JSON Message

1.  Log in to the management console.

2.  Click ![](./figure/001.png). Under **Application**, click **Simple Message Notification**.

	The **Simple Message Notification** page is displayed.

1.  In the navigation tree on the left, choose **Topic**.

	The **Topic** page is displayed.

1.  Select the topic to which you want to publish a message and click **Publish Message** under **Operation**.

2.  Configure the required parameters according to Table 3-3. The topic name is provided by default and you cannot change it.

	Select **JSON** for **Message Type** and manually type the JSON message in the **Message** box or click **Generate JSON Message** to generate the message. The total size of a JSON message cannot exceed 256 KB.

	- If you choose to manually type the JSON message, see section A.2 JSON Message Format for detailed requirements.

	- If you choose to automatically generate the JSON message, perform operations in steps [6](#jump01) to [9](#jump02).

1.  <span id="jump01" class="anchor"></span>Click **Generate JSON Message**.

2.  Enter the message content, for example, "This is a default message.", in the **Message** box and select all message protocols.

	The total size of a JSON message, including the braces, quotation marks, spaces, line breaks, and message content, cannot exceed 256 KB. The size of the JSON message generated for each protocol may vary. The system counts the number of bytes you have entered and prompts you how many remaining bytes you can enter. For details about how to calculate the JSON message size, see [Calculation on the JSON Message Size](#section11977745123756) in section A.2 JSON Message Format.

	**Figure 3-3** Generate JSON Message

    ![](./figure/Json01.png)

1.  Click **OK**. The system generates a JSON message.

	**Figure 3-4** JSON message

    ![](./figure/Json02.png)

1.  <span id="jump02" class="anchor"></span>Modify the message content for each protocol so that different messages are sent to endpoints of different protocols. The system generates the JSON-formatted content, including a default message and messages for different protocols. When SMN fails to match any specific message protocol, it sends the default message. For detailed JSON message format, see section A.2 JSON Message Format.

	**Figure 3-5** JSON message example

	![](./figure/Json03.png)

1.  Click **OK**.

	SMN delivers the message to the applicable subscription endpoints.

	- The message received by an email or HTTP/HTTPS endpoint contains the message subject, message content, and unsubscription link.

	- The message received by an SMS endpoint contains only the message content.
