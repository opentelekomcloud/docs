## Creating a Topic


### Scenarios

A topic is a specified event for message publishing or notification subscription. It serves as a message sending channel, where publishers and subscribers can interact with each other. Before you can send any messages using SMN, you must create a topic.

### Creating a Topic

1.  Log in to the management console.

2.  Click ![](./figure/001.png). Under **Application**, click **Simple Message Notification**.

	The **Simple Message Notification** page is displayed.

1. In the navigation tree on the left, choose **Topic**.

	The **Topic** page is displayed.

1.  Click **Create Topic**.

	The **Create Topic** a1rea is displayed.

	 **Figure 1** Create Topic
	 
	 ![](./figure/topic.png)

1.  Enter a topic name and display name.

	**Table 1** Information required for creating a topic
   	<table>
    <tr>
       <th>Parameter</th>
       <th>Description</th>
        
     </tr>
     <tr>
         <td>Topic Name</td>
         <td>Specifies the topic name, which:                                                                                                                                                                                                                  
               <ul>
				<li>Contains only upper or lower case letters, digits, hyphens (-), and underscores (_) and must start with a letter or digit. </li>
                <li>Must be 1-256 characters long.</li>
				<li>Must be unique and cannot be modified once the topic is created.</li>
			    </ul>
		  </td>
     </tr>
     <tr>
         <td>Display Name</td>
         <td>Describes the topic, which must be less than 192 bytes.                                                                                                                                                                                                
               <dd>NOTICE</dd>                                                                                                                                                                                                                                                  
               <dd>The topic display name is presented as the name of the email sender when you push an email message.</dd>
         </td>
     </tr>
   </table>
1. Click **OK**.

	The topic you created is displayed in the topic list. The system generates a topic URN, which is the unique resource identifier of the topic and cannot be changed.
