# Objects<a name="obs_03_0206"></a>

Objects are basic units stored in OBS. It contains both data and the metadata that describes data properties. Data uploaded to OBS is stored in buckets as objects.

An object consists of data, metadata, and a key.

-   A key specifies the name of an object. An object key is a UTF-8 string ranging from 1 to 1024 characters. Each object is uniquely identified by a key within a bucket.
-   Metadata: Metadata describes the object, and is classified into system metadata and custom metadata. The metadata is a set of key-value pairs that are assigned an object stored in OBS.
    -   System metadata is automatically assigned by OBS for managing the object. System metadata includes Date, Content-Length, Last-Modified, Content-MD5, and more.
    -   You can specify custom metadata to describe the object when you upload the the object to OBS.

-   Data: refers to the content that the object contains.

Generally, objects are managed as files. However, OBS is an object-based storage service and there is no concept of files and folders. For easy data management, OBS provides a method to simulate folders. By adding a slash \(/\) in an object name, for example,  **test/123.jpg**, you can specify  **test**  as a folder and  **123.jpg**  as the name of a file in the  **test**  folder. The key of the object is  **test/123.jpg**.

When uploading an object, you can set a storage class for the object. If no storage class is specified, the object is stored in the same storage class as the bucket in which it resides. You can also change the storage class of an existing object in a bucket.

On OBS Console or OBS clients, you can use folders the same way as they are used in a file system.

