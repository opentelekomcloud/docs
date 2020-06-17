# How Do I Set the Password Validity Period?<a name="EN-US_TOPIC_0079122353"></a>

If you cannot log in to a BMS due to password expiry, contact the administrator.

If you can log in to the BMS, perform the following operations to set the password validity period:

1.  <a name="li96511055152412"></a>Log in to the BMS OS and run the following command to query the password validity period:

    **vi /etc/login.defs**

    The value of parameter  **PASS\_MAX\_DAYS**  indicates the password validity period.

2.  Run the following command to change the value of parameter  **PASS\_MAX\_DAYS**  in  [1](#li96511055152412):

    **chage -M** _99999 user\_name_

    _99999_  is the validity period of the password, and  _user\_name_  is a system user.

    You are advised to set the password validity period as needed and change it on a regular basis.

3.  Run  **vi /etc/login.defs**  to verify that the configuration has taken effect.

    **Figure  1**  Configuration verification<a name="fig12619131052519"></a>  
    ![](figures/configuration-verification.png "configuration-verification")


