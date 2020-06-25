# Why Does the System Display a Message Indicating that the Password for Logging In to a Windows ECS Cannot Be Viewed?<a name="EN-US_TOPIC_0031736846"></a>

## Symptom<a name="en-us_topic_0031703610_section563002281179"></a>

Password authentication is required to log in to a Windows ECS. Therefore, a key file is required to obtain the initial password for logging in to the ECS. However, after  **Get Password**  \(see  [Obtaining the Password for Logging In to a Windows ECS](obtaining-the-password-for-logging-in-to-a-windows-ecs.md)\) is clicked, the system displays a message indicating that the password could not be viewed. ECS login was therefore unsuccessful.

## Possible Causes<a name="en-us_topic_0031703610_section379062211192"></a>

Possible causes vary depending on the image used to create the Windows ECS.

-   Cause 1: The image used to create the Windows ECS is a private image, on which Cloudbase-Init has not been installed.
-   Cause 2: Cloudbase-Init has been installed on the image, but the key pair had not been obtained when the Windows ECS was created.

## Solution<a name="en-us_topic_0031703610_section32757467113923"></a>

-   If the issue is a result of cause 1, proceed as follows:

    If a private image is created without Cloudbase-Init installed, the ECS configuration cannot be customized. As a result, you can log in to the ECS only using the original image password.

    The original image password is the OS password configured when the private image was created. If the original image password has been forgotten, use the password reset function available on the  **Elastic Cloud Server**  page to reset the password.

-   If the issue is a result of cause 2, proceed as follows:
    1.  Locate the row containing the target ECS, click  **More**  in the  **Operation**  column, and select  **Restart**.
    2.  Click  **More**  in the  **Operation**  column and select  **Get Password**  to check whether the password can be obtained.
        -   If the password can be obtained, no further action is required.
        -   If no, contact technical support.



