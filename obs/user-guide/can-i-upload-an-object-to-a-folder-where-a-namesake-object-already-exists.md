# Can I Upload an Object to a Folder Where a Namesake Object Already Exists?<a name="obs_faq_0050"></a>

If versioning is enabled and an object is being uploaded, OBS automatically allocates a unique version ID to the object. Objects with the same name are stored in OBS with different version IDs.

If versioning is not enabled and objects with the same name are being uploaded to a specific folder, the new object will overwrite the existing one.

