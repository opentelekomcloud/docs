## Topic Policy Modification

### Scenarios

You, the topic creator, can configure a topic policy to flexibly grant topic permissions to other users, including querying the subscription list of a topic, creating message templates, publishing messages, modifying topic attributes, and deleting the topic.

After authorizing topic permissions to other users, the topic creator still has the highest operation permissions over a topic.

This section describes how you can modify a topic policy.

### Prerequisites

The topic creator has the right to modify the topic policy.

### Procedure

1.  Log in to the management console.

2.  Click ![](figure/001.png). Under **Application**, click **Simple Message Notification**.

	The **Simple Message Notification** page is displayed.

1.  In the navigation tree on the left, choose **Topic**.

	The **Topic** page is displayed.

1.  Select a topic, click **More** under **Operation**, and select **Modify Topic Policy**.

2.  In the **Modify Topic Policy** page, configure the topic policy. You can choose to configure a basic or advanced policy. The basic mode configures permission for specified users to publish messages to the topic. The advanced mode provides a more flexible way to control topic access permissions. For details, see <a href="#table1">Table 1</a>.

	<a name="table1">**Table 1** Parameters for configuring the topic policy</a>
	<table>
    <tr>
       <th>Policy </th>
       <th>Parameter</th> 
       <th>Configuration</th>
       <th>Description</th>
     </tr>
     <tr>
         <td rowspan="4">Basic</td>
         <td rowspan="3">Users who can publish messages</td>
		 <td>Only the creator of the topic</td>
       	 <td>Only the topic creator has permission to publish messages to the topic.</td>
     </tr>
	<tr>
		 <td>All users</td>
       	 <td>All users have permission to publish message to the topic.</td>
     </tr>
	<tr>
		 <td>Only the following users</td>
       	 <td>You can specify a user in <b>urn:csp:iam::domainId:root</b> format. When multiple users are entered, separate every two with a comma (,).<dd>SMN does not limit the number of users you can specify, but the total length of the topic policy cannot exceed 30 KB.You only need to enter the domain ID of the user and click <b>OK</b>.</dd> <dd>The system completes all other required information for you.</dd> <dd>For details about obtaining the domain ID, see <a href="#domain">Obtaining a User's Domain ID</a>.</dd>                                                                                                                                                              <dd>Configurations in the basic mode are also presented in the advanced mode. You can modify them in the advanced mode if necessary. </dd>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              <dd>Topic creators always have the highest operation permissions over a topic even if they grant topic permissions to other users. </dd></td>
     </tr>
     <tr>
         <td>Services that can publish messages</td>
         <td>OBS and MaaS                                                                                                                                                                   
         </td>
		 <td>The specified cloud service has the operation permission of the topic, for example, OBS.
			<dd>NOTE</dd>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               For details about how to use smn in other cloud services, see user guides of the related services.                                                                                                                                                                       
         </td>
     </tr>
     <tr>
         <td>Advanced</td>
         <td>Users who can perform specified operations on a topic</td>
		 <td>Policy language <dd>For details, see section <a href="Topic Policy.md">Topic Policy</a>.</td>
       	 <td>The advanced mode provides a more flexible topic policy.</td>
     </tr>
     </table>   
### <a name="domain">Obtaining a User's Domain ID</a>

1.  Log in to the management console.

2.  In the upper right, click the username and select **My Credential**.

3.  Obtain the user's domain ID in the account information.
