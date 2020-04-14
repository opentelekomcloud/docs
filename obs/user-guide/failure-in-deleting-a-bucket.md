# Failure in Deleting a Bucket<a name="obs_faq_0064"></a>

-   Check whether the network connectivity is normal between the local computer and OBS. If the network is down, restore the network connection.
-   Check whether all objects in the bucket have been deleted. If not, delete all objects from the bucket.
-   Check whether all fragments in the bucket have been deleted. If not, delete all fragments from the bucket.
-   If versioning is enabled, check whether there are deleted objects remaining in the bucket. If yes, permanently delete all deleted objects from the bucket.
-   Check whether the account that deletes the bucket is the owner of the bucket.
-   If the fault persists, contact the customer service personnel.

