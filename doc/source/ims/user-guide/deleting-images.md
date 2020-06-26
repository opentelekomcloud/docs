# Deleting Images<a name="EN-US_TOPIC_0030713201"></a>

## Scenarios<a name="section193899835818"></a>

You can delete private images that are no longer needed.

## Constraints<a name="section199217147114"></a>

Private images that have been published in Marketplace cannot be deleted.

## Procedure<a name="en-us_topic_0029124542_section5858145710388"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.
3.  Click the  **Private Images**  tab to display the image list.
4.  Locate the row that contains the image, click  **More**  \>  **Delete**  in the  **Operation**  column.

    >![](/images/icon-note.gif) **NOTE:**   
    >To delete multiple images, perform the following operations:  
    >1.  Select the images you want to delete in the image list.  
    >2.  Click  **Delete**  on above the image list.  

5.  \(Optional\) Choose whether to select  **Delete CSBS backups of the full-ECS images**.

    This parameter is available only when the private images to be deleted include full-ECS images.

    If you select this option, the system deletes the CSBS backups of the full-ECS images. 

    >![](/images/icon-note.gif) **NOTE:**   
    >After you perform the operation to delete the images, a case may occur where full-ECS images are successfully deleted, but their CSBS backups are not deleted. This may be because the CSBS backups are being created and cannot be deleted. Click  **Delete**  and continue to delete the CSBS backups as prompted.  

6.  Click  **Yes**.

