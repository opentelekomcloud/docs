## Recording SMN Operations


### Scenarios

SMN is integrated with Cloud Trace Service (CTS) to record resource operations. CTS records operations performed on the management console, operations performed by calling cloud service APIs, and operations triggered within the cloud system.

If you have enabled CTS, when an SMN API is called, the operation information will be reported to CTS, which will then store the operation record to the specified OBS bucket. You can query the operation information in the CTS records, including the request content, source IP address, who sent the request, and when the request was sent.

### SMN Information in CTS

After you enable CTS, when an SMN API is called, the operation will be recorded in the log file, which will then be delivered to the specified OBS bucket for storage.

If someone makes an API call to cancel a subscription without logging in to the management console, CTS will not record the operation. For example, if the subscriber has clicked the link in an email notification to cancel the subscription, the Unsubscribe API is called, but CTS does not record the operation.

CTS can record the following operations in SMN:

- CreateTopic

- DeleteTopic

- UpdateTopic

- UpdateTopicAttribute

- DeleteTopicAttributes

- DeleteTopicAttributeByName

- Subscribe

- Unsubscribe

- CreateMessageTemplate

- UpdateMessageTemplate

- DeleteMessageTemplate

### CTS Log Entries

Each log entry consists of a trace in JSON format. A log entry indicates an SMN API request, including the requested operation, the operation date and time, operation parameters, and information about the user who sends the request. The user information is obtained from the Identity and Access Management (IAM) service.

The following example shows CTS log entries for the **CreateTopic**, **DeleteTopic**, and **UpdateTopic** actions:

    {
	     "time": "2017-02-15 14:21:50 GMT+08:00",
	     "user": "xxx",
	     "request": "xxx",
	     "response": "xxx",
	     "code": 200,
	     "service\_type": "SMN",
	     "resource\_type": "topic",
	     "resource\_id": "topicUrn instance",
	     "source\_ip": "127.0.0.1",
	     "trace\_name": "createTopic",
	     "trace\_rating": "normal",
	     "trace\_type": "ApiCall",
	     "api\_version": "2.0",
	     "project\_id": "tenantId instance",
	     "record\_time": "2017-02-15 14:21:50 GMT+08:00",
	     "trace\_id": "xxx"
    }
    {
	     "time": "2017-02-15 14:12:15 GMT+08:00",
	     "user": "xxx",
	     "response": "xxx",
	     "code": 200,
	     "service\_type": "SMN",
	     "resource\_type": "topic",
	     "resource\_id": "topicUrn instance",
	     "source\_ip": "127.0.0.1",
	     "trace\_name": "deleteTopic",
	     "trace\_rating": "normal",
	     "trace\_type": "ApiCall",
	     "api\_version": "2.0",
	     "project\_id": "tenantId instance",
	     "record\_time": "2017-02-15 14:12:15 GMT+08:00",
	     "trace\_id": "xxx"
    }
    {
	     "time": "2017-02-13 15:38:30 GMT+08:00",
	     "user": "xxx",
	     "request": "xxx",
	     "response": "xxx",
	     "code": 200,
	     "service\_type": "SMN",
	     "resource\_type": "topic",
	     "resource\_id": "topicUrn instance",
	     "source\_ip": "127.0.0.1",
	     "trace\_name": "updateTopic",
	     "trace\_rating": "normal",
	     "trace\_type": "ApiCall",
	     "api\_version": "2.0",
	     "project\_id": "tenantId instance",
	     "record\_time": "2017-02-13 15:38:30 GMT+08:00",
	     "trace\_id": "xxx"
    }
