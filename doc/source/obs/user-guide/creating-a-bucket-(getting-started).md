# Creating a Bucket<a name="obs_03_0306"></a>

This section describes how to create a bucket on OBS Console. A bucket is a container that stores objects in OBS. Before you store data in OBS, you need to create buckets.

>![](/images/icon-note.gif) **NOTE:**   
>On OBS Console, an account can have 100 buckets.  

## Procedure<a name="sb79f841ab9af4b9faf6cbad1932c33b0"></a>

1.  In the upper right corner of the OBS Console homepage, click  **Create Bucket**. The  **Create Bucket**  dialog box is displayed. See  [Figure 1](#fig30207295194414).

    **Figure  1**  Creating a bucket<a name="fig30207295194414"></a>  
    ![](figures/creating-a-bucket.png "creating-a-bucket")

2.  Set  **Region**  and  **Storage Class**, and then enter a name for the bucket.

    >![](/images/icon-note.gif) **NOTE:**   
    >-   Once a bucket is created, you cannot change the name of it. Make sure that the bucket name you set is appropriate.  
    >-   When a URL is used to access a bucket, the bucket name will become a part of the URL. According to the DNS rule, URLs do not support uppercase letters and cannot be used to access a bucket whose name contains uppercase letters. Therefore, a bucket name can contain only lowercase letters, digits, periods \(.\), and hyphens \(-\). For example, if you attempt to access bucket  **MyBucket**  using the URL, bucket  **mybucket**  will be accessed instead, causing an access error.  

3.  Bucket policy: You can select the  **Private**,  **Public Read**, or  **Public Read and Write**  policy for a bucket.
4.  Tags: Tags are used to identify and classify OBS buckets. Each tag has only one pair of key-value. Each tag is represented by one key-value pair. For more information, see  [Tag Overview](tag-overview.md).
5.  Click  **Create Now**.

