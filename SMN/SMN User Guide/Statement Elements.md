## Statement Elements

### Statement elements

Table 1 Statement elements
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
		 <td>The value can be <b>Allow</b> or  <b>Deny</b>.</td>
     </tr>
     <tr>
         <td>Principal</td>
         <td>Object on which the statement takes effect.
			<dd>Currently, only <b>CSP</b> and <b>Service</b> are supported.                                                                                                                                                                                   
                <ul><li><b>CSP</b> indicates cloud users.</li>                                                                                                                                                                                                              
                <li><b>Service</b> indicates cloud services.</li></ul></dd>    
			</td>
		 <td>Either<b>Principal</b>or <b>NotPrincipal</b> must be configured.<dd>If you enter <b>CSP</b>, you must specify the user information in <b>urn:csp:iam::domainId:root</b>format. You need to obtain the domain IDs of users you specify.                                                                                                                                         If you enter <b>Service</b>, you must specify the cloud service names in lower case. </dd></td>
     </tr>
	<tr>
         <td>NotPrincipal</td>
         <td>Object on which the statement does not take effect  </td>
		 <td>Either <b>Principal</b> or <b>NotPrincipal</b>must be configured.
			<dd>If you enter <b>CSP</b>, you must specify the user information in <b>urn:csp:iam::domainId:root</b> format. You need to obtain the domain IDs of users you specify.If you enter <b>Service</b>, you must specify the cloud service names in lower case. </dd>
		</td>
     </tr>
	<tr>
         <td>Action</td>
         <td>Statement actions
				<dd>You can use a wildcard character to configure a type of actions, for example, <b>SMN:Update * </b> and <b>SMN:Delete * </b>. </dd>                                                                                                                                <dd>If you only enter an asterisk (*) in the statement, all supported actions will take effect.</dd></td>
		 <td>Either <b>Action</b> or <b>NotAction</b>must be configured.
				<dd>The following actions are supported: 
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
				<li>SMN:Publish </li></dd>
				</ul>
				For details about mappings between the operations and APIs, see Table 1 in section <a href="Mappings Between SMN Operations and APIs">Mappings Between SMN Operations and APIs</a>. 
		</td>
		<tr>
         <td>NotAction</td>
         <td>Statement excluding actions
				<dd>You can use a wildcard character to configure a type of actions, for example, <b>SMN:Update * </b> and <b>SMN:Delete * </b>.                                                                         </dd></td>
		 <td>Either <b>Action</b> or <b>NotAction</b>must be configured.
				<dd>The following actions are supported: 
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
				</ul></dd>
				For details about mappings between the operations and APIs, see Table 1 in section <a href="Mappings Between SMN Operations and APIs">Mappings Between SMN Operations and APIs</a>. 
		</td>
     </tr>
		<tr>
         <td>Resource</td>
         <td>Topic on which the statement takes effect   </td>
		 <td>Either <b>Resource</b> or <b>NotResource</b>must be configured.
			<dd>You need to enter the topic URN. </dd></td>
     </tr>
	</tr>
		<tr>
         <td>Condition  </td>
         <td>(Optional) Conditions for the policy statement to take effect                                                        Enter supported condition operators and key words. </td>
		 <td>Enter supported condition operators and key words.
			<dd>You can specify conditions to configure fine-grained permission control over a topic. </dd></td>
     </tr>
     </table>  

### Statement example

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
