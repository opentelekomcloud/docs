# How Can I Control Access Permissions for OBS?<a name="obs_faq_0042"></a>

You can use the following mechanisms to control access permissions for OBS: 

-   IAM policies

    IAM policies  define the actions that can be performed on your cloud resources. In other words,  IAM policies  specify what actions are allowed or denied.

    IAM policies  are recommended if you assign permissions to IAM users of the same account.

    The implementation mechanism of  IAM policies  is as follows:

    1.  Create a user group and select an IAM permission set for the user group.
    2.  Create an IAM user and add it to the user group so that it inherits permissions of the user group.

-   IAM Agency

    Delegates other accounts or services to access OBS. A delegated party can manage OBS resources on behalf of the delegating party. This achieves secure and efficient service management.

-   Bucket Policy

    A bucket policy is attached to a bucket and objects in the bucket. By leveraging bucket policies, the owner of a bucket can authorize IAM users or other accounts the permissions to operate the bucket and objects in the bucket.

-   Object Policy

    In a bucket policy, you can configure resources to which the bucket policy applies. You can use the asterisk \(\*\) to indicate all objects in the bucket or specify an object name prefix, so that the policy applies to objects that share the specified name prefix. An object policy is directly configured for the selected object.

-   Access Control List \(ACL\)

    ACLs control the read and write permissions for accounts, whose permission granularity is not as fine as bucket policies and  IAM policies. Generally, it is recommended that you use  IAM policies  and bucket policies for access control.


