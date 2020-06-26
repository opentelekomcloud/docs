# How Can I Check the Status of a Backend ECS?<a name="EN-US_TOPIC_0115500498"></a>

1.  Verify that the ECS is enabled.
    1.  Log in to the ECS.
    2.  Run the following command to check the port listening status of the system:

        **netstat -ntpl**

        >![](/images/icon-note.gif) **NOTE:**   
        >For Windows ECSs, you can run the  **netstat -ano**  command on the CLI to view the port listening status or server software status.  
        >**Figure  1**  Port listening status of the system<a name="en-us_topic_0101328255_fig4990866211124"></a>    
        >![](figures/port-listening-status-of-the-system.jpg "port-listening-status-of-the-system")  


2.  Verify that the ECS communication function is normal.

    For example, if the ECS uses the HTTP protocol and port 80, you can run the  **curl**  command to check whether the communication function is normal.

    ![](figures/icon-image-2.jpg)


