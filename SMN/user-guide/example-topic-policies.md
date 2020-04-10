# Example Topic Policies<a name="smn_ug_44003"></a>

## Example 1<a name="section1055594864013"></a>

```
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
            "Resource": "urn:smn:region:cffe4fc4c9a54219b60dbaf7b586e132:Mytopic",
            "Condition": {
                "DateLessThan":{
                     "csp:CurrentTime":"2017-11-07T15:35:00Z"
                }
            }
        }
    ]
}
```

The example is explained as follows:

The policy whose ID is  **\_\_default\_policy\_ID**  contains one statement. The statement ID is  **\_\_user\_pub\_0**. The statement allows users whose domain IDs are  **123456789**  and  **987654321**  to query details of and publish messages to the topic whose URN is  **urn:smn:region:cffe4fc4c9a54219b60dbaf7b586e132:Mytopic**. This topic policy is valid until  **2017-11-07T15:35:00Z**.

## Example 2<a name="section139924544112"></a>

```
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
                "SMN:Subscribe" 
            ], 
            "Resource": "urn:smn:region:6558ed0a1485466897e962f38fdfdb88:helloworld",
            "Condition": {
                "DateLessThan":{
                     "csp:CurrentTime":"2017-11-07T15:35:00Z"
                }
                "StringLike": {
                     "smn:Endpoint":["*@gmail.com","*@hotmail.com"]
                }
            }
        }
    ]
}
```

The example is explained as follows:

The policy whose ID is  **\_\_default\_policy\_ID**  contains one statement. The statement ID is  **\_\_user\_pub\_0**. The statement allows users whose domain IDs are  **123456789**  and  **987654321**  to subscribe Gmail and Hotmail email addresses to the topic whose URN is  **urn:smn:region:6558ed0a1485466897e962f38fdfdb88:helloworld**. This topic policy is valid until  **2017-11-07T15:35:00Z**.

## Example 3<a name="section1692213342413"></a>

```
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
```

The example is explained as follows:

The policy whose ID is  **\_\_default\_policy\_ID**  contains three statements whose IDs are  **\_\_user\_pub\_0**,  **\_\_user\_pub\_1**, and  **\_\_service\_pub\_0**.

-   Statement  **\_\_user\_pub\_0**  allows users whose domain IDs are  **123456789**  and  **987654321**  to query details of and publish messages to the topic whose URN is  **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**.
-   Statement  **\_\_user\_pub\_1**  does not allow the user whose domain ID is  **987654321**  to query details of and publish messages to the topic whose URN is  **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**.
-   Statement  **\_\_service\_pub\_0**  allows the OBS service to query details of and publish messages to the topic whose URN is  **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**.

The three statements altogether determine the effect of the topic policy. The evaluation process is as follows:

-   If the user whose domain ID is  **987654321**  tries to publish a message to topic  **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**, statement  **\_\_user\_pub\_0**  allows the operation request, but statement  **\_\_user\_pub\_1**  denies it. Therefore, the request is denied.
-   If the user whose domain ID is  **888888888**  tries to publish a message to topic  **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**, no statement denies the request, but there is also no statement that explicitly allows it. Therefore, the request is denied.
-   If the user whose domain ID is  **123456789**  tries to publish a message to topic  **urn:smn:regionId:e23bf08ebb924730b452426c60849564:ECM\_BKS\_Topic**, statement  **\_\_user\_pub\_0**  allows the operation request, and no statement denies it. Therefore, the request is allowed.

