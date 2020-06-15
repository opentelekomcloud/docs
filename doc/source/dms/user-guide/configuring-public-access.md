# Configuring Public Access<a name="EN-US_TOPIC_0221089390"></a>

To access a Kafka instance over a public network, you can enable public access and configure public network bandwidth for the instance. If you no longer need public access to the instance, you can disable it as required.

## Procedure<a name="section7716364362"></a>

1.  Log in to the management console.
2.  Choose  **Application**  \>  **Distributed Message Service**  to open the DMS console.
3.  In the navigation pane, choose  **Kafka Premium**.
4.  Click the name of an instance.
5.  In the  **Public Access**  section, click  ![](figures/icon-edit.png).

    The  **Change Public Network Bandwidth**  page is displayed.

6.  Perform the following operations as required:
    -   Enable public access

        Click  ![](figures/icon-close-publicnetwork.png)  to enable public access and set the bandwidth.

        >![](/images/icon-note.gif) **NOTE:**   
        >-   You can enable public access for a maximum of three instances. If you want to enable public access for more instances, contact customer service to increase your quota.  
        >-   If you have enabled and disabled public access before, the public access address will be different when you enable public access again.  
        >-   Bandwidth value range:  
        >    -   When the instance specification is 100 MB/s, the public network bandwidth must be a multiple of 3 in the range from 3 to 900.  
        >    -   When the instance specification is 300 MB/s, the public network bandwidth must be a multiple of 3 in the range from 3 to 900.  
        >    -   When the instance specification is 600 MB/s, the public network bandwidth must be a multiple of 4 in the range from 4 to 1,200.  
        >    -   When the instance specification is 1,200 MB/s, the public network bandwidth must be a multiple of 8 in the range from 8 to 2,400.  

    -   Disable public access

        Click  ![](figures/icon-open-publicnetwork.png)  to disable public access.

    -   Modify public network bandwidth

        Next to  **Bandwidth \(Mbit/s\)**, slide the bar or enter a number in the text box to set the bandwidth.

        >![](/images/icon-note.gif) **NOTE:**   
        >-   The public network bandwidth can only be changed to the higher value.  
        >-   During the public network bandwidth expansion, a few services may fail. You are advised to perform this operation during off-peak hours.  


7.  Click  **Submit**  to save the changes.

    A message is displayed, indicating that the task is successfully submitted. You can view the operation progress on the  **Background Task Management**  page. If the task status is  **Successful**, the modification has succeeded.


