## Topic Policy

### Topic Policy Introduction

A topic policy is configured by a topic owner to grant topic operation permissions to other users or cloud services.

By default, CES and Anti-DDoS have the permission to publish messages to topics of all users.

You can configure the topic policy using statements. A topic policy may contain one or more statements. In the statements, you can grant topic permissions to other users, including querying the subscription list of a topic, creating message templates, publishing messages, modifying topic attributes, and deleting the topic.

The following is an example to grant a user permissions to publish messages to a topic and query topic details:

    {
	     "Version": "2016-09-07",
	     "Id": "\_\_default\_policy\_ID",
	     "Statement": [
					     {
					     "Sid": "\_\_user\_pub\_0",
					     "Effect": "Allow",
					     "Principal": {
									     "CSP": [
									     "urn:csp:iam::3fc217979ee6454c9144b7db870b489b:root"
									     ]
					    			 },
					     "Action": [
								     "SMN:Publish",
								     "SMN:QueryTopicDetail"
								     ],
	    				 "Resource": "urn:smn:regionId:8234e169f2cb4262896c1cc69c0b69dd:SMN\_02"
	     				}
	     			]
    }

### Topic Policy Evaluation

When a user accesses the topic of another user, policy evaluation is required.

The system checks the statements in the topic policy in sequence. If the **Effect** value of a statement is **Deny**, the evaluation finishes, and the user's access request is denied. If the **Effect** value of at least one statement is **Allow**, the operation is allowed. If all statements are checked while no statement allows the operation, the operation is denied by default.

### Topic Policy Elements

<a href="#table1">Table 1</a> lists the elements of a topic policy.

<a name="table1">**Table 1** Topic policy elements</a>
	<table>
    <tr>
       <th>Parameter</th>
       <th>Description</th> 
	   <th>Constraint</th>
     </tr>
     <tr>
         <td>Version </td>
         <td>Policy specification version</td>
		 <td>Currently, only **2016-09-07** is supported.</td>
     </tr>
     <tr>
         <td>Id</td>
         <td>Policy ID, which uniquely identifies a policy</td>
		 <td>The policy ID cannot be left empty.</td>
     </tr>
     <tr>
         <td>Statement</td>
         <td>Policy statement</td>
		 <td>A policy must contain at least one statement. For details about the statement elements, see section <i>Statement Elements.</i> </td>
     </tr>
     </table>   
### Topic Policy Example

The following policy contains two statements:

    {
	     "Version": "2016-09-07",
	     "Id": "access\_policy\_01",
	     "Statement": [
	     {Statement1},
	     {Statement2}
	     ]
    }
    
