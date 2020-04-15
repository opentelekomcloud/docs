# View Execution Records<a name="EN-US_TOPIC_0226028131"></a>

You can view the execution result of the bootstrap operation on the  **Bootstrap Action**  tab page of the cluster details page.

## Viewing the Execution Result<a name="section1923518517376"></a>

1.  Log in to the MRS management console.
2.  In the left navigation pane, choose  **Clusters**  \>  **Active Clusters**. Click a cluster you want to query.

    The cluster details page is displayed.

3.  On the cluster details page, click the  **Bootstrap Action**  tab. Information about the bootstrap actions added during cluster creation is displayed.

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >-   You select  **Before component start**  or  **After component start**  in the upper right corner to query information about the related bootstrap actions.  
    >-   The last execution result is listed here. For a newly created cluster, the records of bootstrap actions executed during cluster creation are listed. If a cluster is expanded, the records of bootstrap actions executed on the newly added nodes are listed.  


## Viewing Execution Logs<a name="section03072163912"></a>

If you want to view the run logs of a bootstrap action, set  **Action upon Failure**  to  **Continue**  when adding the bootstrap action. And then, log in to each node to view the run logs in the  **/var/log/Bootstrap**  directory. If you add bootstrap actions before and after component start, you can distinguish bootstrap action logs of the two phases based on the timestamps.

You are advised to print logs in detail in the script so that you can view the detailed run result. MRS redirects the standard output and error output of the script to the log directory of the bootstrap action.

