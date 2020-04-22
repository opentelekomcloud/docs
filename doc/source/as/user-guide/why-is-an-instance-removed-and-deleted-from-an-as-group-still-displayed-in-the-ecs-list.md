# Why Is an Instance Removed and Deleted from an AS Group Still Displayed in the ECS List?<a name="EN-US_TOPIC_0187475600"></a>

If an instance automatically added to an AS group is protected, it is only removed out of the AS group, but not deleted, so that it can still be used by other services.

An instance that is being used by other services are protected generally. For example, an instance is used by IMS for creating a private image, or used by storage DR.

