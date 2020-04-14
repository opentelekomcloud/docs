# Obtaining the Password of a Windows BMS<a name="EN-US_TOPIC_0140749073"></a>

## Scenarios<a name="section0230121618127"></a>

Password authentication mode is required to log in to a Windows BMS. Therefore, you must use the key file used when you created the BMS to obtain the administrator password generated when the BMS was initially installed. The administrator user is  **Administrator**  or the user configured using Cloudbase-Init. This password is randomly generated, offering high security.

## Prerequisites<a name="section81271915161618"></a>

You have obtained the private key file used during BMS creation.

## Procedure<a name="section15236417161414"></a>

1.  Log in to the management console. 
2.  Under  **Computing**, click  **Bare Metal Server**.
3.  Locate the row that contains the Windows BMS, click  **More**  in the  **Operation**  column, and select  **Obtain Password**.
4.  Use either of the following methods to obtain the password through the private key:
    -   Click  **Select File**  and upload the private key from a local directory.
    -   Copy the private key content to the text field.

5.  Click  **Get Password**  to obtain a random password.

