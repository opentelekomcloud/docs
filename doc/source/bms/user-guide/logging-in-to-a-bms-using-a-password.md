# Logging In to a BMS Using a Password<a name="EN-US_TOPIC_0053537015"></a>

By default, login to Linux BMSs using the password is disabled. If you want to use this function, log in to the BMS \(see section  [Logging In to a BMS Using an SSH Key Pair](logging-in-to-a-bms-using-an-ssh-key-pair.md)\) and enable the function. For details, see section  [How Do I Set SSH Configuration Items?](how-do-i-set-ssh-configuration-items.md).

## Prerequisites<a name="section33044631113942"></a>

-   The BMS must be in  **Running**  state.
-   You have bound an EIP to the BMS. For details, see  [Binding an EIP to a BMS](binding-an-eip-to-a-bms.md).
-   You have configured the inbound rules of the security group. For details, see section  [Adding Security Group Rules](adding-security-group-rules.md).
-   The network connection between the login tool \(such as PuTTY\) and the target BMS is normal. For example, the default port 22 is not blocked by the firewall.
-   SSH login to BMSs using the password is enabled.

## Log In to a BMS from a Windows PC<a name="section62238598113942"></a>

You can use the following methods to log in to a Linux BMS from a local PC running Windows \(for example, use PuTTY\):

>![](/images/icon-note.gif) **NOTE:**   
>Download PuTTY from  [https://www.chiark.greenend.org.uk/\~sgtatham/putty/latest.html](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).  

1.  Run PuTTY.
2.  In the navigation pane on the left, choose  **Session**, enter the EIP of the BMS in the text box under  **Host Name \(or IP address\)**, and select  **SSH**  for  **Connection type**.
3.  Choose  **Windows**  \>  **Translation**  and select  **UTF-8**  from the  **Received data assumed to be in which character set:**  drop-down list box.
4.  Click  **Open**.
5.  Enter username  **root**  and the password you set to log in to the BMS.

## Log In to a BMS from a Linux PC<a name="section6934158113942"></a>

To log in to a Linux BMS from a Linux PC, run the following command:

**ssh **_EIP of the BMS_

