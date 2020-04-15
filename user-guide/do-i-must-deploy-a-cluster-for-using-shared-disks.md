# Do I Must Deploy a Cluster for Using Shared Disks?<a name="evs_faq_0039"></a>

Yes.

If you simply attach a shared disk to multiple servers, files cannot be shared between the servers because shared disks do not have the cluster capability. Therefore, build a shared file system or deploy a cluster management system to share files between servers.

