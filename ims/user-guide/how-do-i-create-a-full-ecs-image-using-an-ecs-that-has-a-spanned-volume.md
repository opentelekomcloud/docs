# How Do I Create a Full-ECS Image Using an ECS That Has a Spanned Volume?<a name="EN-US_TOPIC_0106444267"></a>

An ECS used to create a Windows full-ECS image cannot have a spanned volume. Otherwise, data may be lost when the full-ECS image is used to create ECSs.

If the ECS has a spanned volume, back up the data in the spanned volume and then delete this volume from the ECS. Use the ECS to create a full-ECS image. Use the full-ECS image to create an ECS. You can also use the backup to create a spanned volume if necessary.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If a Linux ECS has a volume group or a logical volume consisting of multiple physical volumes, back up the data in the volume group or logical volume and delete the volume group or logical volume before creating a full-ECS image using this ECS to prevent data loss.  

