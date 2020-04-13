# Making Preparations<a name="EN-US_TOPIC_0083737005"></a>

Before using the BMS service, you need to make the following preparations:

-   [Create an IAM User](#section929013341428)
-   [Create a Key Pair](#section2031413481717)

## Create an IAM User<a name="section929013341428"></a>

If you want to allow multiple users to manage your resources without sharing your password or private key, you can create users using IAM and grant permissions to the users. These users can use specified login links and their own accounts to access the public cloud and help you efficiently manage resources. You can also set account security policies to ensure the security of these accounts and reduce enterprise information security risks.

If you have registered on the public cloud platform but have no IAM user, you can create one on the IAM console. For example, to create a BMS administrator, perform the following steps:

1.  Enter your username and password to log in to the management console.
2.  In the upper right corner of the page, click the username and select  **Identity and Access Management**.
3.  In the navigation pane, choose  **Users**. In the right pane, click  **Create User**.
4.  Enter basic user information as prompted.
    -   **Username**: Enter a username, for example,  **bms\_administrator**.
    -   **Credential Type**: Select  **Password**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >-   A password can be used to log in to the management console and enable development tools \(such as APIs, the CLI, and SDK\) that can access cloud services through password authentication. This is the recommended option because the security administrator manages users.  
        >-   Access keys are used to enable development tools \(such as APIs, the CLI, and SDK\) that can access cloud services through key authentication.  

    -   In the  **User Groups**  area, select  **admin**  from the drop-down list.
    -   **Description**: Enter description of the user, for example,  **BMS administrator**.

5.  Click  **Next**. Select  **Set manually**  for  **Password Type**.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >A BMS administrator can log in to the management console and manage users. You are advised to select  **Set manually**  for  **Password Type**  when you create a BMS administrator for your domain. If you create a BMS administrator for another user, you are advised to select  **Set at first login**  for  **Password Type**  instead so that the user can set their own password.  

6.  Select  **Require Password Reset**  to ensure that the BMS administrator is forced to change the password the first time the administrator logs in. The  **Require Password Reset**  option is selected by default. It is recommended that you retain the default setting to ensure that the security administrator account password is set by the security administrator, preventing password leakage.
7.  Click  **OK**.

    After the user is created, you can use the IAM user login link above the list and the created user to log in to the console.


## Create a Key Pair<a name="section2031413481717"></a>

The cloud platform uses the public key cryptography to protect the login information of your BMS. You need to specify the key pair name and provide the private key when logging to the BMS using SSH. 

If you have no key pair, create one on the management console.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>If you want to create BMSs in multiple regions, you need to create a key pair in each region. For more information about regions, see  [Region and AZ](region-and-az.md).  

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.
3.  In the navigation tree, choose  **Key Pair**.
4.  On the right side of the page, click  **Create Key Pair**.
5.  Enter the key name and click  **OK**.

    An automatically allocated key name consists of  **KeyPair-**  and a 4-digit random number. Change it to an easy-to-remember one, for example,  **KeyPair-_xxxx_\_bms**.

6.  Download the private key file. Alternatively, the system will automatically download it for you. The file name is the specified key pair name with a suffix of .pem. Securely store the private key file. In the displayed dialog box, click  **OK**.

    >![](public_sys-resources/icon-notice.gif) **NOTICE:**   
    >This is the only opportunity for you to save the private key file. Keep it secure. When creating a BMS, provide the name of the desired key pair. Each time you log in to the BMS using SSH, provide the private key.  


