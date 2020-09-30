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

    A bucket policy applies to the configured OBS bucket and objects in the bucket. An OBS bucket owner can use a bucket policy to grant permissions of buckets and objects in the buckets to IAM users or other accounts.

-   Object Policy

    An object policy is a policy that applies to objects in a bucket. In a bucket policy, you can specify a set of objects as the resources to which the bucket policy applies, or you can use asterisk symbol \(\*\) to indicate all objects in the bucket. To configure an object policy, select an object, and then configure the object policy directly for the object.

-   Access Control List \(ACL\)

    ACLs control read and write permissions for accounts, which are not as fine-grained as bucket policies and  IAM policies. Therefore, you are advised to use  IAM policies  and bucket policies for access control.


