# Resetting Kafka Password<a name="EN-US_TOPIC_0143117127"></a>

## Scenario<a name="section33628036"></a>

If you forget the password of a Kafka premium instance, you can reset the password to access the instance.

>![](/images/icon-note.gif) **NOTE:**   
>-   You can reset the password of a Kafka premium instance only if Kafka SASL\_SSL has been enabled for the instance.  
>-   You can only reset the password of a Kafka premium instance in the  **Running**  state.  

## Prerequisites<a name="section34216874"></a>

A Kafka premium instance has been created.

## Procedure<a name="section12258217288"></a>

1.  Log in to the management console.
2.  Choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
3.  In the navigation pane, choose  **Kafka Premium**.
4.  Choose  **More**  \>  **Reset Kafka Password**  in the same row as the Kafka premium instance for which you want to reset the password.
5.  In the displayed  **Reset Kafka Password**  dialogue box, enter a new password and confirm the password.

    For details about password complexity requirements, see  [DMS Password Complexity Requirements](dms-password-complexity-requirements.md).

6.  Click  **OK**.

    -   If the password is successfully reset, a success message will be displayed.
    -   If the password failed to be reset, a failure message will be displayed. Reset the password again. If the password fails to be reset for multiple times, contact the administrator.

    >![](/images/icon-note.gif) **NOTE:**   
    >The system will display a success message only after the password is successfully reset on all nodes.  


