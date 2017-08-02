### Topic Policy Example

The following is an example for configuring a topic policy:

    {
     	
    	"Version": "2016-09-07",
    	 "Id": "__default_policy_ID",
     	"Statement": [
     					{
     						"Sid": "__user_pub_0",
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
    					 "Resource": "urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM_BKS_Topic"
    					 },
					     {
						     "Sid": "__user_pub_1",
						     "Effect": "Deny",
						     "Principal": {
										     "CSP": [
										     "urn:csp:iam::987654321:root"
					     					]
					     },
					     	"Action": [
									     "SMN:Publish",
									     "SMN:QueryTopicDetail"
					    			 ],
					     "Resource": "urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM_BKS_Topic"
					     },
					     {
						     "Sid": "__service_pub_0",
						     "Effect": "Allow",
						     "Principal": {
					     					"Service": [
					    								 "obs"
					    							 ]
					     				},
					   		  "Action": [
										     "SMN:Publish",
										     "SMN:QueryTopicDetail"
										     ],
					    	 "Resource": "urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM_BKS_Topic"
					     }
     ]
    }
    
The example is explained as follows:

1.  The statement whose ID is **\_\_user\_pub\_0** allows the user whose domain ID is **123456789** or **987654321** to publish messages to topic **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic** and query details about the topic.

2.  The statement whose ID is **\_\_user\_pub\_1** denies the user whose domain ID is **987654321** to publish messages to topic **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic** and query details about the topic.

3.  The statement whose ID is **\_\_service\_pub\_0** allows the OBS service to publish messages to topic **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic** and query details about the topic.

4.  If the user whose domain ID is **987654321** tries to publish a message to topic **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**, statement **\_\_user\_pub\_0** allows the operation, but statement **\_\_user\_pub\_1** denies it. Therefore, the operation is denied.

5.  If the user whose domain ID is **432198765** tries to publish messages to topic **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**, no statement denies the operation, but at the same time no statement allows it. Therefore, the operation is denied.

6.  If the user whose domain ID is **123456789** tries to publish messages to topic **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**, no statement denies the operation, and statement **\_\_user\_pub\_0** allows it. Therefore, the operation is allowed.
