# Failed to Download an Object<a name="obs_faq_0135"></a>

-   Check whether the network connectivity is normal between the local computer and OBS. If the network is down, restore the network connection.
-   Check whether the account is in arrears or the account balance is insufficient. If it is the case, top up the account.
-   Check whether the account has the permission to download objects from the bucket. Check the  IAM policies, bucket policies, object policies, bucket ACLs, and object ACLs. If the account does not have the permission, obtain the permission first.
-   Check whether KMS encryption is enabled for the current object. If the object is encrypted, downloading objects from OBS Console or OBS Browser will fail. If you download the encrypted object by using the SDK or API, the key for decryption is required.
-   Check whether the current object is in the Cold storage class. If yes and it is in the status of unrestored, restore the object first.
-   If the fault persists, contact the customer service personnel.

