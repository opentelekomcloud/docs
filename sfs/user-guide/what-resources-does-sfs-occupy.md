# What Resources Does SFS Occupy?<a name="sfs_01_0094"></a>

To ensure that file systems can be used properly, the service occupies the following resources:

-   When a file system is created, the inbound rules of ports 111, 445, 2049, 2051, and 2052 are enabled in the security group entered by the user. The default source IP address is 0.0.0.0/0. You can change the IP address as required.
-   If an encrypted file system is created, the KMS key entered by the user is used for encryption. Note that if the key is deleted, data in the file system cannot be used.

-   For SFS file systems:
    -   When an SFS file system is created, the inbound rules of ports 111, 445, 2049, 2051, and 2052 are enabled in the security group entered by the user. The default source IP address is 0.0.0.0/0. You can change the IP address as required.


When data is written to the folders of a file system, the running memory of the server is occupied, but the storage space of the server disk is not occupied. The file system uses independent space.

