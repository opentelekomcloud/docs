## Statement Elements

###Statement elements

Table 4-2 Statement elements
	<table>
    <tr>
       <th>Element</th>
       <th>Description</th> 
	   <th>Constraint</th>
     </tr>
     <tr>
         <td>Sid</td>
         <td>Statement ID</td>
		 <td>The statement ID, for example, <b>statement01</b> and <b>statement02</b>, must be unique. </td>
     </tr>
     <tr>
         <td>Effect</td>
         <td>Statement effect</td>
		 <td> The value can be <b>Allow</b> or  <b>Deny</b>.</td>
     </tr>
     <tr>
         <td>Principal</td>
         <td><p>Object on which the statement takes effect</p>
			<p>Currently, only <b>CSP</b> and <b>Service</b> are supported.                                                                                                                                                                                   
                <ul><li><b>CSP</b> indicates cloud users.</li>                                                                                                                                                                                                              
                <li><b>Service</b> indicates cloud services.</li></ul></p>    
			</td>
		 <td><p>Either<b>Principal</b>or <b>NotPrincipal</b> must be configured. </p><p>If you enter <b>CSP</b>, you must specify the user information in <b>urn:csp:iam::domainId:root</b>format. You need to obtain the domain IDs of users you specify.                                                                                                                                         If you enter <b>Service</b>, you must specify the cloud service names in lower case. </p></td>
     </tr>
	<tr>
         <td>NotPrincipal</td>
         <td>Object on which the statement does not take effect  </td>
		 <td><p>Either <b>Principal</b> or <b>NotPrincipal</b>must be configured.</p>
			<p>If you enter <b>CSP</b>, you must specify the user information in <b>urn:csp:iam::domainId:root</b> format. You need to obtain the domain IDs of users you specify.If you enter <b>Service</b>, you must specify the cloud service names in lower case. </p>
		</td>
     </tr>
	<tr>
         <td>Action</td>
         <td><p>Statement actions</p>
				<p>You can use a wildcard character to configure a type of actions, for example, <b>SMN:Update * </b> and <b>SMN:Delete * </b>.                                                                                                                                 If you only enter an asterisk (*) in the statement, all supported actions will take effect.</p></td>
		 <td><p>Either <b>Action</b> or <b>NotAction</b>must be configured.</p>
				The following actions are supported: 
				<ul>
				<li>SMN:UpdateTopic </li>                                                                                                                                                                                                            <li>SMN:DeleteTopic </li>
				<li>SMN:QueryTopicDetail </li>
				<li>SMN:ListTopicAttributes </li>
				<li>SMN:UpdateTopicAttribute  </li>
				<li>SMN:DeleteTopicAttributes </li>
				<li>SMN:DeleteTopicAttributeByName </li>
				<li>SMN:ListSubscriptionsByTopic </li>
				<li>SMN:Subscribe </li>
				<li>SMN:Unsubscribe  </li>
				<li>SMN:Publish </li>
				</ul>
				For details about mappings between the operations and APIs, see <i>Table A-1</i>. 
		</td>
		<tr>
         <td>NotAction</td>
         <td><p>Statement excluding actions</p>
				<p>You can use a wildcard character to configure a type of actions, for example, <b>SMN:Update * </b> and <b>SMN:Delete * </b>.                                                                               </p></td>
		 <td><p>Either <b>Action</b> or <b>NotAction</b>must be configured.</p>
				The following actions are supported: 
				<ul>
				<li>SMN:UpdateTopic </li>                                                                                                                                                                                                            <li>SMN:DeleteTopic </li>
				<li>SMN:QueryTopicDetail </li>
				<li>SMN:ListTopicAttributes </li>
				<li>SMN:UpdateTopicAttribute  </li>
				<li>SMN:DeleteTopicAttributes </li>
				<li>SMN:DeleteTopicAttributeByName </li>
				<li>SMN:ListSubscriptionsByTopic </li>
				<li>SMN:Subscribe </li>
				<li>SMN:Unsubscribe  </li>
				<li>SMN:Publish </li>
				</ul>
				For details about mappings between the operations and APIs, see <i>Table A-1</i>. 
		</td>
     </tr>
		<tr>
         <td>Resource</td>
         <td>Topic on which the statement takes effect   </td>
		 <td><p>Either <b>Resource</b> or <b>NotResource</b>must be configured.</p>
			<p>You need to enter the topic URN. </p></td>
     </tr>
	</tr>
		<tr>
         <td>Condition  </td>
         <td>(Optional) Conditions for the policy statement to take effect                                                        Enter supported condition operators and key words. </td>
		 <td><p>Enter supported condition operators and key words.</p>
			<p>You can specify conditions to configure fine-grained permission control over a topic. </p></td>
     </tr>
     </table>  

###Statement example

    "Statement": [
			     {
				     "Sid": "statement01",
				     "Effect": "[Allow|Deny]",
				     "[Principal|NotPrincipal]": {
				     								"CSP": [
				     											"urn:csp:iam::5f5631c473084f2bb68c93f23348ccd5:root"
				     										],
					    							 "Service":[""]
					     						},
				     "[Action|NotAction]": [
										     "SMN:Publish",
										     "SMN:QueryTopicDetail"
										     ],
				     "[Resource|NotResource]": "urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic"
				     "Condition":{
								     "DateLessThan":{
								     "csp:CurrentTime":"2016-11-07T15:35:00+08:00"
								     }
				     			}
			     }
    ]
