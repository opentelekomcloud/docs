# Changing the Name of a BMS<a name="EN-US_TOPIC_0083737000"></a>

## Scenarios<a name="section31883092112"></a>

To make it easy for you to identify and manage each BMS, the cloud platform allows you to set BMS names and change the names at any time. The new name of a BMS takes effect after the BMS is restarted.

## Constraints<a name="section49641651142610"></a>

The names of Windows BMSs cannot be changed.

## Procedure<a name="section11351898212"></a>

1.  Log in to the management console.
2.  Under  **Computing**, click  **Bare Metal Server**.

    The BMS console is displayed.

3.  Click the name of the BMS whose name is to be changed.
4.  Click  ![](figures/edit-icon.png)  next to  **Name**, enter a new name that meets requirements, and click  ![](figures/ok-icon.png)  to save the change.

    The BMS name can contain only letters, digits, hyphens \(-\), underscores \(\_\), and periods \(.\).

5.  Log in to the BMS OS and run the following command to enable automatic hostname synchronization:

    **vi /opt/huawei/network\_config/bms-network-config.conf**

    Set the value of  **auto\_synchronize\_hostname**  to  **True**.

    ```
    auto_synchronize_hostname = True
    ```

    Press  **Esc**  and enter  **:wq**  to save and exit the file.

    >![](/images/icon-note.gif) **NOTE:**   
    >If the value of  **auto\_synchronize\_hostname**  is  **False**, after the BMS is restarted, the hostname will be automatically changed to that set during BMS creation.  

6.  Log in to the management console again. Locate the row that contains the BMS, click  **More**  in the  **Operation**  column, and select  **Restart**.

    After about 10 minutes, verify that the BMS is restarted and its hostname is automatically updated.


