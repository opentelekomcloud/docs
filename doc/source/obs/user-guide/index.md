# User Guide

-   [Service Overview]
    -   [About OBS](about-obs.md)
    -   [Advantages](advantages.md)
    -   [Application Scenarios](application-scenarios.md)
    -   [Permissions Management](permissions-management.md)
    -   [Using OBS](using-obs.md)
    -   [Related Services](related-services.md)
    -   [Basic Concepts]
        -   [Objects](objects.md)
        -   [Buckets](buckets.md)
        -   [Access Keys \(AK/SK\)](access-keys-(ak-sk).md)
        -   [Endpoints and Domain Names](endpoints-and-domain-names.md)
        -   [Region and AZ](region-and-az.md)

-   [OBS Console Operation Guide]
    -   [Console Function Overview](console-function-overview.md)
    -   [Web Browser Versions Supported by OBS Console](web-browser-versions-supported-by-obs-console.md)
    -   [Getting Started]
        -   [Process Description](process-description-(console).md)
        -   [Configuring User Permissions](configuring-user-permissions-(console).md)
        -   [Creating a Bucket](creating-a-bucket-(getting-started).md)
        -   [Uploading a File](uploading-a-file-(getting-started).md)
        -   [Downloading a File](downloading-a-file-(getting-started).md)
        -   [Deleting a File](deleting-a-file-(console-getting-started).md)
        -   [Deleting a Bucket](deleting-a-bucket-(console-getting-started).md)

    -   [Storage Classes Overview](storage-classes-overview-(console).md)
    -   [Managing Buckets]
        -   [Creating a Bucket](creating-a-bucket.md)
        -   [Viewing Basic Information of a Bucket](viewing-basic-information-of-a-bucket-(console).md)
        -   [Searching for a Bucket](searching-for-a-bucket.md)
        -   [Deleting a Bucket](deleting-a-bucket-(console).md)

    -   [Managing Objects]
        -   [Creating a Folder](creating-a-folder-(console).md)
        -   [Uploading a File](uploading-a-file.md)
        -   [Downloading a File](downloading-a-file.md)
        -   [Searching for a File or Folder](searching-for-a-file-or-folder-(console).md)
        -   [Accessing an Object Using Its URL](accessing-an-object-using-its-url.md)
        -   [Restoring a Cold File Stored in OBS](restoring-a-cold-file-stored-in-obs.md)
        -   [Deleting a File or Folder](deleting-a-file-(console).md)
        -   [Undeleting a File](undeleting-a-file.md)
        -   [Managing Fragments](managing-fragments-(console).md)

    -   [Server-Side Encryption]
        -   [Server-Side Encryption Overview](server-side-encryption-overview-(console).md)
        -   [Uploading a File with Server-Side Encryption](uploading-a-file-with-server-side-encryption-(console).md)

    -   [Object Metadata]
        -   [Object Metadata Overview](object-metadata-overview.md)
        -   [Configuring Object Metadata](configuring-object-metadata.md)

    -   [Permission Control]
        -   [Overview](permission-control-overview-(console).md)
        -   [Permission Control Mechanisms]
            -   [IAM Policies](iam-policies.md)
            -   [Bucket Policies and Object Policies](bucket-policies-and-object-policies.md)
            -   [Bucket ACLs and Object ACLs](bucket-acls-and-object-acls.md)
            -   [Relationship Between a Bucket ACL and a Bucket Policy](relationship-between-a-bucket-acl-and-a-bucket-policy.md)
            -   [How Does Authorization Work When Multiple Access Control Mechanisms Co-Exist?](how-does-authorization-work-when-multiple-access-control-mechanisms-co-exist.md)

        -   [Bucket Policy Parameters]
            -   [Effect](effect.md)
            -   [Principal](principal.md)
            -   [Resources](resources.md)
            -   [Actions](actions.md)
            -   [Conditions](conditions.md)

        -   [Configuring IAM Policies]
            -   [Creating a User and Granting OBS Permissions](creating-a-user-and-granting-obs-permissions.md)

        -   [Configuring a Bucket Policy]
            -   [Configuring a Standard Bucket Policy](configuring-a-standard-bucket-policy.md)
            -   [Configuring a Custom Bucket Policy \(Common Mode\)](configuring-a-custom-bucket-policy-(common-mode).md)
            -   [Configuring a Custom Bucket Policy \(Coding Mode\)](configuring-a-custom-bucket-policy-(coding-mode).md)

        -   [Configuring an Object Policy](configuring-an-object-policy.md)
        -   [Configuring a Bucket ACL](configuring-a-bucket-acl-(console).md)
        -   [Configuring an Object ACL](configuring-an-object-acl.md)
        -   [Application Cases]
            -   [Granting an IAM User with the Operation Permissions for a Specified Bucket](granting-an-iam-user-with-the-operation-permissions-for-a-specified-bucket.md)
            -   [Granting Other Accounts with the Operation Permissions for a Specified Bucket](granting-other-accounts-with-the-operation-permissions-for-a-specified-bucket.md)
            -   [Restricting Bucket Access to a Specified Address ](restricting-bucket-access-to-a-specified-address.md)
            -   [Configuring the Start Time and End Time of Access to Objects in a Bucket](configuring-the-start-time-and-end-time-of-access-to-objects-in-a-bucket.md)
            -   [Authorizing Access Permissions to Anonymous Users](authorizing-access-permissions-to-anonymous-users.md)
            -   [Authorizing Folder Access Permissions to Anonymous Users](authorizing-folder-access-permissions-to-anonymous-users.md)

    -   [Versioning]
        -   [Versioning Overview](versioning-overview.md)
        -   [Configuring Versioning](configuring-versioning.md)

    -   [Logging]
        -   [Logging Overview](logging-overview-(console).md)
        -   [Configuring Access Logging for a Bucket](configuring-access-logging-for-a-bucket.md)

    -   [Tags]
        -   [Tag Overview](tag-overview.md)
        -   [Configuring Tags](configuring-tags.md)

    -   [Event Notification]
        -   [SMN-Enabled Event Notification](smn-enabled-event-notification.md)
        -   [Configuring SMN-Enabled Event Notification](configuring-smn-enabled-event-notification.md)
        -   [Application Example: Configuring SMN-Enabled Event Notification](application-example-configuring-smn-enabled-event-notification.md)

    -   [Lifecycle Management]
        -   [Lifecycle Management Overview](lifecycle-management-overview-(console).md)
        -   [Configuring a Lifecycle Rule](configuring-a-lifecycle-rule-(console).md)

    -   [Static Website Hosting]
        -   [Static Website Hosting Overview](static-website-hosting-overview.md)
        -   [Redirection Overview](redirection-overview.md)
        -   [Configuring Static Website Hosting](configuring-static-website-hosting.md)
        -   [Configuring Redirection](configuring-redirection.md)
        -   [Using a User-Defined Domain Name to Configure Static Website Hosting](using-a-user-defined-domain-name-to-configure-static-website-hosting.md)

    -   [CORS]
        -   [CORS Overview](cors-overview-(console).md)
        -   [Configuring CORS](configuring-cors.md)

    -   [URL Validation]
        -   [URL Validation Overview](url-validation-overview.md)
        -   [Configuring URL Validation](configuring-url-validation.md)

    -   [Cloud Trace Service](cloud-trace-service.md)
    -   [Task Management](task-management-(console).md)
    -   [Troubleshooting]
        -   [An Object Fails to Be Downloaded Using Internet Explorer 11](an-object-fails-to-be-downloaded-using-internet-explorer-11.md)
        -   [OBS Console Cannot Be Opened in Internet Explorer 9](obs-console-cannot-be-opened-in-internet-explorer-9.md)
        -   [The Object Name Changes After an Object with a Long Name Is Downloaded to a Local Computer](the-object-name-changes-after-an-object-with-a-long-name-is-downloaded-to-a-local-computer.md)
        -   [Failed to Configure Event Notification](failed-to-configure-event-notification.md)
        -   [Time Difference Is Longer Than 15 Minutes Between the Client and Server](time-difference-is-longer-than-15-minutes-between-the-client-and-server.md)

    -   [List of OBS Error Codes](list-of-obs-error-codes-(console).md)

-   [OBS Browser Operation Guide]
    -   [Introduction to OBS Browser]
        -   [OBS Browser Overview](obs-browser-overview.md)
        -   [Function Description](function-description.md)

    -   [Getting Started]
        -   [Process Description](process-description.md)
        -   [Configuring User Permissions](configuring-user-permissions-(browser).md)
        -   [Downloading OBS Browser](downloading-obs-browser.md)
        -   [Creating Access Keys \(AK and SK\)](creating-access-keys-(ak-and-sk).md)
        -   [Logging In to OBS Browser](logging-in-to-obs-browser.md)
        -   [Adding a Bucket](adding-a-bucket-(getting-started).md)
        -   [Uploading a File or Folder](uploading-a-file-or-folder-(browser).md)
        -   [Downloading a File or Folder](downloading-a-file-or-folder-(getting-started).md)
        -   [Deleting a File or Folder](deleting-a-file-(browser-getting-started).md)
        -   [Deleting a Bucket](deleting-a-bucket-(browser-getting-started).md)

    -   [Storage Classes Overview](storage-classes-overview-(browser).md)
    -   [Managing Buckets]
        -   [Bucket Management Methods](bucket-management-methods.md)
        -   [Adding a Bucket](adding-a-bucket.md)
        -   [Searching for a Bucket](searching-for-a-bucket-2.md)
        -   [Viewing Basic Information of a Bucket](viewing-basic-information-of-a-bucket-(browser).md)
        -   [Managing Fragments](managing-fragments.md)
        -   [Deleting a Bucket](deleting-a-bucket-(browser).md)

    -   [Managing Objects]
        -   [Object Management Methods](object-management-methods.md)
        -   [Creating a Folder](creating-a-folder-(browser).md)
        -   [Uploading a File or Folder](uploading-a-file-or-folder.md)
        -   [Downloading a File or Folder](downloading-a-file-or-folder.md)
        -   [Accessing an Object Using Its Object URL](accessing-an-object-using-its-object-url.md)
        -   [Searching for a File or Folder](server-side-encryption-overview-(browser).md)
        -   [Deleting a File or Folder](deleting-a-file-(browser).md)
        -   [Restoring a Cold File in OBS](restoring-a-cold-file-in-obs.md)

    -   [Server-Side Encryption]
        -   [Server-Side Encryption Overview](server-side-encryption-overview-(browser).md)
        -   [Uploading a File with Server-Side Encryption](uploading-a-file-with-server-side-encryption.md)

    -   [Permission Control]
        -   [Overview](permission-control-overview-(browser).md)
        -   [Configuring a Bucket Policy](configuring-a-bucket-policy.md)
        -   [Configuring a Bucket ACL](configuring-a-bucket-acl-(browser).md)

    -   [Lifecycle Management]
        -   [Lifecycle Management Overview](lifecycle-management-overview-(browser).md)
        -   [Configuring a Lifecycle Rule](configuring-a-lifecycle-rule-(browser).md)

    -   [CORS]
        -   [CORS Overview](cors-overview-(browser).md)
        -   [Configuring CORS](configuring-cors-(browser).md)

    -   [Logging]
        -   [Logging Overview](logging-overview-(browser).md)
        -   [Configuring Logging](configuring-logging.md)

    -   [External Buckets]
        -   [External Buckets Overview](external-buckets-overview.md)
        -   [Adding External Buckets](adding-external-buckets.md)
        -   [Application Example 1: Authorizing Access Permissions Required for Adding an External Bucket Through the Bucket ACL](application-example-1-authorizing-access-permissions-required-for-adding-an-external-bucket-through.md)
        -   [Application Example 2: Authorizing Access Permissions Required for Adding an External Bucket Through the Standard Bucket Policy](application-example-2-authorizing-access-permissions-required-for-adding-an-external-bucket-through.md)
        -   [Application Example 3: Authorizing Access Permissions Required for Adding an External Bucket Through the Custom Bucket Policy](application-example-3-authorizing-access-permissions-required-for-adding-an-external-bucket-through.md)

    -   [Task Management](task-management.md)
    -   [Related Operations]
        -   [Configuring the System](configuring-the-system.md)
        -   [Managing Accounts](managing-accounts.md)
        -   [Updating OBS Browser](updating-obs-browser.md)

    -   [Troubleshooting]
        -   [Login Page of OBS Browser Does Not Respond upon User Login](login-page-of-obs-browser-does-not-respond-upon-user-login.md)
        -   [No Upload Task Is Created After a Large Number of Files Are Selected for Upload On OBS Browser](no-upload-task-is-created-after-a-large-number-of-files-are-selected-for-upload-on-obs-browser.md)
        -   [Blue or Black Screen of Death Occurs During File Upload on OBS Browser](blue-or-black-screen-of-death-occurs-during-file-upload-on-obs-browser.md)
        -   [Tasks Are Not Displayed in the Task List When Objects Are Managed Using OBS Browser](tasks-are-not-displayed-in-the-task-list-when-objects-are-managed-using-obs-browser.md)
        -   [Time Difference Is Longer Than 15 Minutes Between the Client and the Server](time-difference-is-longer-than-15-minutes-between-the-client-and-the-server.md)
        -   [An Error Occurs During the Start-up of OBS Browser, Indicating That the Task Management Function Cannot Work Properly Due to Unavailability of the Database](an-error-occurs-during-the-start-up-of-obs-browser-indicating-that-the-task-management-function-cann.md)

    -   [List of OBS Error Codes](list-of-obs-error-codes-(browser).md)

-   [FAQs]
    -   [OBS Basics]
        -   [How Can I Use OBS?](how-can-i-use-obs.md)
        -   [How Do I Obtain An OBS Endpoint?](how-do-i-obtain-an-obs-endpoint.md)
        -   [What Are the Advantages of Object Storage When Compared with SAN and NAS Storage?](what-are-the-advantages-of-object-storage-when-compared-with-san-and-nas-storage.md)
        -   [Which Types of Data Can Be Stored in OBS?](which-types-of-data-can-be-stored-in-obs.md)
        -   [What Is the Data Volume That I Can Store in OBS?](what-is-the-data-volume-that-i-can-store-in-obs.md)
        -   [Can Folders in OBS Be Used the Same Way in a File System?](can-folders-in-obs-be-used-the-same-way-in-a-file-system.md)
        -   [Where Is Data Stored in OBS?](where-is-data-stored-in-obs.md)
        -   [What Is the Relationship Between OBS Bucket Names and OBS Domain Names?](what-is-the-relationship-between-obs-bucket-names-and-obs-domain-names.md)
        -   [Does OBS Support Access over HTTPS?](does-obs-support-access-over-https.md)
        -   [Can Other Users Access My Data Stored in OBS?](can-other-users-access-my-data-stored-in-obs.md)
        -   [Does OBS Support Resumable Data Transfer?](does-obs-support-resumable-data-transfer.md)
        -   [Does OBS Support Batch Upload?](does-obs-support-batch-upload.md)
        -   [Does OBS Support Batch Download?](does-obs-support-batch-download.md)
        -   [Does OBS Support Batch Deletion of Objects?](does-obs-support-batch-deletion-of-objects.md)
        -   [What Are the Factors that Affect the Upload and Download Speed of OBS?](what-are-the-factors-that-affect-the-upload-and-download-speed-of-obs.md)
        -   [Why Does Data Stored on OBS Get Lost?](why-does-data-stored-on-obs-get-lost.md)
        -   [Can Deleted Data Be Recovered?](can-deleted-data-be-recovered.md)
        -   [Will Data Remanence Exist in OBS After I Delete Data?](will-data-remanence-exist-in-obs-after-i-delete-data.md)
        -   [Does OBS Provide Multi-AZ Reliability?](does-obs-provide-multi-az-reliability.md)

    -   [Access Control]
        -   [How Can I Control Access Permissions for OBS?](how-can-i-control-access-permissions-for-obs.md)
        -   [What Are the Differences Between an IAM Policy and a Bucket Policy in Access Control?](what-are-the-differences-between-an-iam-policy-and-a-bucket-policy-in-access-control.md)
        -   [What Is the Relationship Between a Bucket Policy and an Object Policy?](what-is-the-relationship-between-a-bucket-policy-and-an-object-policy.md)

    -   [Buckets and Objects]
        -   [Failed to Create a Bucket](failed-to-create-a-bucket.md)
        -   [Failed to Upload an Object](failed-to-upload-an-object.md)
        -   [Failed to Download an Object](failed-to-download-an-object.md)
        -   [Failure in Deleting a Bucket](failure-in-deleting-a-bucket.md)
        -   [Bucket Storage Class vs. Object Storage Class](bucket-storage-class-vs-object-storage-class.md)
        -   [Can I Modify the Region of a Bucket?](can-i-modify-the-region-of-a-bucket.md)
        -   [How Do I Obtain the Access Path to an Object?](how-do-i-obtain-the-access-path-to-an-object.md)
        -   [Objects in a Bucket Cannot Be Searched For](objects-in-a-bucket-cannot-be-searched-for.md)

    -   [Security]
        -   [How Is Data Security Ensured in OBS?](how-is-data-security-ensured-in-obs.md)
        -   [Does OBS Scan My Data for Other Purposes?](does-obs-scan-my-data-for-other-purposes.md)
        -   [Can Background Management Personnel Export My Data from OBS?](can-background-management-personnel-export-my-data-from-obs.md)
        -   [How Does OBS Prevent My Data from Being Stolen?](how-does-obs-prevent-my-data-from-being-stolen.md)
        -   [Can a Pair of AK and SK Be Replaced When They Are Being Used to Access OBS?](can-a-pair-of-ak-and-sk-be-replaced-when-they-are-being-used-to-access-obs.md)
        -   [Can a Pair of AK and SK Be Used by Multiple Users to Access OBS?](can-a-pair-of-ak-and-sk-be-used-by-multiple-users-to-access-obs.md)
        -   [Which Encryption Technologies Are Supported by OBS?](which-encryption-technologies-are-supported-by-obs.md)

    -   [How Do I Use Fragment Management?]
        -   [Why Are Fragments Generated?](why-are-fragments-generated.md)
        -   [How Do I Manage Fragments?](how-do-i-manage-fragments.md)

    -   [How Do I Use Versioning?]
        -   [Can I Upload an Object to a Folder Where a Namesake Object Already Exists?](can-i-upload-an-object-to-a-folder-where-a-namesake-object-already-exists.md)
        -   [Can I Recover a Deleted Object?](can-i-recover-a-deleted-object.md)

    -   [How Do I Use Tags?]
        -   [Can I Search for a Bucket by Tag?](can-i-search-for-a-bucket-by-tag.md)
        -   [What Can I Do with Tags?](what-can-i-do-with-tags.md)

    -   [Event Notification]
        -   [Which Events Can Trigger Event Notifications?](which-events-can-trigger-event-notifications.md)

    -   [How Do I Use Lifecycle Management?]
        -   [What Are the Application Scenarios of Lifecycle Management?](what-are-the-application-scenarios-of-lifecycle-management.md)

    -   [How Do I Use Static Website Hosting?]
        -   [Can OBS Host My Static Websites?](can-obs-host-my-static-websites.md)
        -   [Which Types of Websites Are Suitable for Static Website Hosting in OBS?](which-types-of-websites-are-suitable-for-static-website-hosting-in-obs.md)
        -   [How Do I Obtain the Static Website Hosting Address of a Bucket?](how-do-i-obtain-the-static-website-hosting-address-of-a-bucket.md)

-   [Glossary](glossary.md)

