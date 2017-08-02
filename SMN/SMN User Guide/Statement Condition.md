## Statement Condition

### Condition Introduction

A condition in the statement can configure fine-grained permission control over a topic. It matches the key words you specified to control topic permissions.

In a topic policy statement, if a condition contains multiple condition operations or a condition operation contains multiple condition key words, an AND operation is executed. If you specify multiple values for a key word, an OR operation is executed.

    "Condition":{
			     "condition1": {
							     "conditionKey1": ["value11","value12"],
							     "conditionKey2": ["value21"]
							     }
			     "condition2": {
							     "conditionKey3": [value31,value32]
							     }
    }

**Figure 1** Condition logic

![](./figure/condition.png)

### Condition Evaluation Rules

Only when all conditions in a statement are met, the statement operation can take effect. Otherwise, the requested operation is denied.

### Condition Elements

<a href="#table1">Table 1</a> lists the elements in a condition.

<a name="table1>"**Table 1** Condition elements</a>
	<table>
    <tr>
       <th>Item</th>
       <th>Description</th> 
	   <th>Constraint</th>
     </tr>
     <tr>
         <td>Operation </td>
         <td>Specifies the character strings, digits, date, or time to be matched in the operation.</td>
		 <td>The time you entered must comply with the ISO 8601 specifications.</td>
     </tr>
     <tr>
         <td>Operation key word</td>
         <td>Specifies the object on which the condition operation takes effect.</td>
		 <td>The operation key word cannot be empty.</td>
     </tr>
     </table>  
### Topic Policy Examples

The condition operation examples are as follows:

Example 1:

    {
	     "Version": "2016-09-07",
	     "Id": "\_\_default\_policy\_ID",
	     "Statement": [
					     {
						     "Sid": "\_\_user\_pub\_0",
						     "Effect": "Allow",
						     "Principal": {
										     "CSP": [
										     "urn:csp:iam::123456789:root",
										     "urn:csp:iam::987654321:root"
										     ]
					     					},
						     "Action": [
									     "SMN:Publish",
									     "SMN:QueryTopicDetail"
									     ],
						     "Resource": "urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic",
						     "Condition": {
										     "DateLessThan":{
										     "csp:CurrentTime":"2017-11-07T15:35:00Z"
										     }
										   }
						    }
			     ]
    }

The example is explained as follows:

The policy allows user **urn:csp:iam::123456789:root** and user **urn:csp:iam::987654321:root** to publish messages to and query details about topic **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**. This policy is valid until **2017-11-07T15:35:00Z**.

Example 2:
    
    {
	     "Version": "2016-09-07",
	     "Id": "\_\_default\_policy\_ID",
	     "Statement": [
					     {
						     "Sid": "\_\_user\_pub\_0",
						     "Effect": "Allow",
						     "Principal": {
										     "CSP": [
										     "urn:csp:iam::123456789:root",
										     "urn:csp:iam::987654321:root"
										     ]
					     				},
					     "Action": [
								     "SMN:Subscribe"
								     ],
					     "Resource": "urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic",
					     "Condition": {
									     "DateLessThan":{
													     "csp:CurrentTime":"2017-11-07T15:35:00Z"
																	     }
									     "StringLike": {
									     					"smn:Endpoint":["\*@gmail.com","\*@hotmail.com"]
									     				}
									   }
					     }
					   ]
    }

The example is explained as follows:

The policy allows user **urn:csp:iam::123456789:root** and user **urn:csp:iam::987654321:root** to add email subscriptions (only Gmail and Hotmail addresses) to topic **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**. This policy is valid until **2017-11-07T15:35:00Z**.
