# Configuring SSO<a name="en-us_topic_0079626574"></a>

Configuring an IdP login link on the enterprise management system allows enterprise users to access the cloud system after being authenticated by the enterprise IdP.

## Prerequisites<a name="section532423118535"></a>

An IdP has been created, and its login link is available.

## Procedure<a name="section4342101645419"></a>

1.  In the navigation pane, choose  **Identity Providers**.
2.  Click  **View**  in the row that contains the target IdP.
3.  Click  **Copy**  to the right of  **Login link**.
4.  On the web page of the enterprise management system, press  **F12**  and configure the following information:

    ```
    <a href="<Login link>"> Cloud system entry </a>
    ```

    **Figure  1**  Entry model<a name="fig41120284164022"></a>  
    ![](figures/entry-model.png "entry-model")

    After logging in to the enterprise management system, enterprise users can click the system entry link on the enterprise management system to access the cloud system.


