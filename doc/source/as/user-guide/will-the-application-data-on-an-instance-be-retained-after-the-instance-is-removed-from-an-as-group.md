# Will the Application Data on an Instance Be Retained After the Instance Is Removed from an AS Group and Deleted?<a name="EN-US_TOPIC_0123129155"></a>

No. AS automatically releases ECS instances. You must ensure that instances in the AS group do not store application status information or important data, such as sessions, databases, and logs. If you want to store your application status, you can store it on an independent server \(such as ECS\) or database \(such as RDS database\). 

