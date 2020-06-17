# Step 2: Log In to the BMS<a name="EN-US_TOPIC_0140737435"></a>

## Scenarios<a name="section35217122012"></a>

After creating a BMS, you can log in to it using multiple methods. This section describes how to log in to a BMS using an SSH key pair. For more login modes, see  [Linux BMS Login Methods](linux-bms-login-methods.md)  or  [Windows BMS Login Methods](windows-bms-login-methods.md).

## Procedure<a name="section11564732142211"></a>

The following steps describe how to log in to a BMS using an SSH key pair through PuTTY.

1.  Log in to the Cloud Server Console.
2.  In the navigation pane, choose  **Bare Metal Server**.
3.  In the upper left corner, click  ![](figures/icon-region.png)  and select a region.
4.  In the BMS list, locate the created BMS  **bms-7676-nginx**. Record the EIP of the BMS and perform the following steps:
    1.  Check whether the private key file has been converted to  **.ppk**  format.
        -   If yes, go to step  [4.g](#en-us_topic_0053536938_li693703913264).
        -   If no, go to step  [4.b](#en-us_topic_0053536938_li11816141811202).

    2.  <a name="en-us_topic_0053536938_li11816141811202"></a>Visit the following website and download PuTTY and PuTTYgen:

        [https://www.chiark.greenend.org.uk/\~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

        >![](/images/icon-note.gif) **NOTE:**   
        >PuTTYgen is a private key generator, which is used to create a key pair that consists of a public key and a private key for PuTTY.  

    3.  Run PuTTYgen.
    4.  In the  **Actions**  area, click  **Load**  and import the private key file that you stored when creating the BMS.

        Ensure that the private key file is in the format of  **All files \(\*.\*\)**.

    5.  Click  **Save private key**.
    6.  <a name="en-us_topic_0053536938_li194442401260"></a>Save the converted private key to the local PC, for example,  **kp-123.ppk**, to the local computer.
    7.  <a name="en-us_topic_0053536938_li693703913264"></a>Double-click  **PUTTY.EXE**. The  **PuTTY Configuration**  page is displayed.

        **Figure  1**  PuTTY Configuration<a name="en-us_topic_0053536938_fig14750143592717"></a>  
        ![](figures/putty-configuration.png "putty-configuration")

    8.  Choose  **Connection**  \>  **Data**. Enter the image username in  **Auto-login username**.

        >![](/images/icon-note.gif) **NOTE:**   
        >Contact the administrator to obtain the image username.  

    9.  Choose  **Connection**  \>  **SSH**  \>  **Auth**. In the last configuration item  **Private key file for authentication**, click  **Browse**  and select the .ppk private key in step  [4.f](#en-us_topic_0053536938_li194442401260).
    10. Choose  **Session**  and enter the EIP of the BMS in the box under  **Host Name \(or IP address\)**.
    11. Click  **Open**.

        Log in to a BMS.



