## Adding a Subscription to the Topic

###Scenarios

To send messages published to a topic to a subscription endpoint, you must add the endpoint to the topic. The endpoint can be a mail address, a mobile phone number, or an HTTP/HTTPS URL. After you add the subscription endpoint to the topic and the subscriber confirms the subscription, the subscriber is able to receive messages published to the topic.

###Adding a Subscription

1. Log in to the management console.

2.  Click ![](./figure/001.png). Under **Application**, click **Simple Message Notification**.

	The **Simple Message Notification** page is displayed.


1. In the navigation tree on the left, choose **Topic**.

	The **Topic** page is displayed.


1. Click the topic name. The topic details are displayed.
1. In the **Subscriptions** area, query the subscription list.

3.  Click **Add Subscription** in the upper right of the subscription list.

	The **Add Subscription** page is displayed.

1. Specify the subscription protocol and endpoint.

	**Table 3-2** Information required for adding a subscription
	<table>
    <tr>
       <th>Parameter</th>
       <th>Description</th>
        
     </tr>
     <tr>
         <td>Topic Name</td>
         <td>Provides the name of the topic to be subscribed to, which cannot be changed. </td>
     </tr>
     <tr>
         <td>Protocol</td>
         <td><p>Specifies the protocol the subscription endpoint supports.</p>                                                                                                                                                                            	 <p>The available options include <b>SMS</b>, <b>Email</b>, <b>HTTP</b>, and <b>HTTPS</b>.</p> 
         </td>
     </tr>
     <tr>
         <td>Endpoint</td>
         <td><p>Specifies the subscription endpoint. You can enter up to 10 endpoints, with every two separated with a line break.</p> 
                                                                                                                                  
              <ul>
			  <li><b>SMS</b>: Enter one or more valid phone numbers.                                                                                                                                                                                    
                  <p>The phone number must be preceded by a plus sign (+) and the country code.</p>                                                                                                                                                          
                  <p>For example:</p>                                                                                                                                                                                                                        
                  <ul>
                  <li><p><b>+4900000000</b></p></li>                                                                                                                                                                                                                     
                  <li><p><b>+4900000001</b></p></li>                                                                                                                                                                                                                      
                  <li><p><b>+4900000002</b></p></li>                                                                                                                                                                                                                     
                  <li><p><b>+4900000003</b></p></li>
                  </ul>
             </li>                                                                                                                                                                                                                         
              <li><p><b>Email</b>: Enter one or more email addresses.<p>                                                                                                                                                                                        
                  <p>For example:</p>                                                                                                                                                                                                                         
                  <ul>
                  <li><p><b>username@example.com</b></p></li>                                                                                                                                                                                                            
                  <li><p><b>username2@example.com</b></p></li>
                  </ul>
              </li>                                                                                                                                                                                                                
              <li><b>HTTP</b> or <b>HTTPS</b>: Enter one or more public network URLs.                                                                                                                                                                           
	              <p>For example:</p>                                                                                                                                                                                                                           
	              <ul>
				  <li><p><b>http://example.com/notification/action</b></p></li>                                                                                                                                                                                             
	              <li><p><b>http://example2.com/notification/action</b></p></li>
				 </ul>
             </li>
			</ul>   
         </td>
     </tr>
     </table>                                                                

1.  Click **OK**.

	The subscription you added is displayed in the subscription list. SMN automatically sends a confirmation message to the subscription endpoint, and the subscriber must confirm the subscription within 48 hours so that they can receive notification messages. Otherwise, you need to send a new confirmation message to the subscriber.

![](./figure/notice.png)

1.  To prevent a malicious user from attacking subscription endpoints, SMN limits the number of confirmation messages that can be sent to an endpoint within a specified period of time. For details, see section A.4 Traffic Control on Subscription Confirmation.
2.  SMN does not check whether a subscription endpoint exists when you add a subscription. However, a subscriber can receive notification messages only when they confirm the subscription.
3.  The token is valid only for 48 hours. Therefore, the subscriber must confirm the subscription within that time.
