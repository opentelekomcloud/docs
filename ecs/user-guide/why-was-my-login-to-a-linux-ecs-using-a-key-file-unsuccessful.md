# Why Was My Login to a Linux ECS Using a Key File Unsuccessful?<a name="EN-US_TOPIC_0031734664"></a>

## Symptom<a name="en-us_topic_0031703610_section563002281179"></a>

When the key file for creating a Linux ECS was used to log in to the ECS, the login failed.

## Possible Causes<a name="en-us_topic_0031703610_section379062211192"></a>

Possible causes vary depending on the image used to create the Linux ECS.

-   Cause 1: The image used to create the Linux ECS is a private image, on which Cloud-Init is not installed.
-   Cause 2: Cloud-Init is installed on the image, but the key pair was not obtained during ECS creation.

## Solution<a name="en-us_topic_0031703610_section32757467113923"></a>

-   If the issue is a result of cause 1, proceed as follows:

    If a private image is created without Cloud-Init installed, the ECS configuration cannot be customized. As a result, you can log in to the ECS only using the original image password or key pair.

    The original image password or key pair is the OS password or key pair configured when the private image was created. If the original image password was forgotten or key pair has been lost, use the password reset function available on the  **Elastic Cloud Server**  page to reset the password.

-   If the issue is a result of cause 2, proceed as follows:
    1.  Locate the row containing the target ECS, click  **More**  in the  **Operation**  column, and select  **Restart**.
    2.  Use the key file to log in to the ECS again and check whether the login is successful.
        -   If the login is successful, no further action is required.
        -   If no, contact technical support.



