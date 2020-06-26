# Overview<a name="EN-US_TOPIC_0046588154"></a>

IMS allows you to create encrypted images to ensure data security.

>![](/images/icon-note.gif) **NOTE:**   
>-   To use the  image encryption  function, you must apply for KMS Administrator permissions.   

## Constraints<a name="section168724402494"></a>

-   KMS must be enabled.
-   Encrypted images  cannot be shared with others.
-   The system disk of an ECS created from an encrypted image is also encrypted, and its key is the same as the image key.
-   If an ECS has an encrypted system disk, private images created using the ECS are also encrypted.
-   The key used for encrypting an image cannot be changed.
-   If the key used for encrypting an image is disabled or deleted, the image is unavailable.

