# Overview<a name="EN-US_TOPIC_0032042417"></a>

You can use the  image sharing  function to share your private images with others tenants. Other tenants who accept the shared images can use the images to create ECSs of the same specifications.

If you are a multi-project user, the image sharing function allows you to use images conveniently in multiple projects in the same region.

>![](/images/icon-note.gif) **NOTE:**   
>Projects  are used to group and isolate OpenStack resources, which include computing, storage, and network resources. A project can be either a department or a project team. Multiple projects can be created under one account.  

-   You can specify the images to be shared, stop image sharing, and add or delete tenants with whom they share images.
-   The recipient can choose to accept or refuse the shared images and remove the images they have accepted.

## Constraints<a name="section4023295419426"></a>

-   You can only share private images that have not been published in Marketplace.
-   You can only share images within the same region. 
-   Each image can be shared with a maximum of 128 tenants.
-   You can stop sharing images anytime without notifying the recipient.
-   You can delete shared image anytime without notifying the recipient.
-   Encrypted images cannot be shared.
-   Full-ECS images cannot be shared.

## Procedure<a name="section49924060194159"></a>

If you want to share a private image with another tenant, the procedure is as follows:

1.  You obtain the project ID from the tenant.
2.  You share an image with the tenant.
3.  The tenant accepts the shared image.

    After accepting the image, the tenant can use it to create ECSs.


## Related FAQs<a name="section20211133810163"></a>

If you have any other questions, see  [Image Sharing FAQs](image-sharing-faqs.md).

