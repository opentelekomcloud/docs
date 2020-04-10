# Image Creation FAQs<a name="EN-US_TOPIC_0193146244"></a>

## How Many Private Images Can be Created Under an Account?<a name="section14208122617454"></a>

Currently, you can create a maximum of 100 private images per account in a region.

## Should I Stop the ECS Before Using It to Create a Private Image?<a name="section196746554818"></a>

No. You can create an image from a running ECS. However, if data is written to the ECS during image creation, the data is not contained in the created image.

## Where Can I View the Image Creation Progress? How Long Does It Take to Create an Image?<a name="section06781459374"></a>

Log in to the management console. Choose  **Computing**  \>  **Image Management Service**  and click the  **Private Images**  tab. View the image creation progress in the  **Status**  column.

The time required for creating an image depends on the network speed, image file type, and disk size of the instance to which the image belongs.

