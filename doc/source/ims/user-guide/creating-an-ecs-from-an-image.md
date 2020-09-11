# Creating an ECS from an Image<a name="EN-US_TOPIC_0030713200"></a>

## Scenarios<a name="en-us_topic_0029124530_section3974322317454"></a>

You can use a public or private image to create an ECS. The differences are as follows:

-   If you use a public image, the created ECS contains an OS and pre-installed public applications. You need to install applications as needed.
-   If you use a private image, the created ECS contains an OS, pre-installed public applications, and private applications.

## Procedure<a name="en-us_topic_0029124530_section2828301817653"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Image Management Service**.

    The IMS console is displayed.

3.  Click the  **Public Images**  or  **Private Images**  tab to display the image list.
4.  Locate the row that contains the private image and click  **Apply for Server**  in the  **Operation**  column.

    Alternatively, click the image name. In the upper right corner of the image details page, click  **Apply for Server**.

5.  For details about how to create an ECS, see  _Elastic Cloud Server User Guide_.

    When creating an ECS using a system disk image, you can reset the ECS specifications and system disk type, but the system disk can only be larger than that of the image.


