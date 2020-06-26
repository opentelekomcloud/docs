# Introduction to Bootstrap Actions<a name="EN-US_TOPIC_0127245535"></a>

Bootstrap actions indicate that you can run your scripts on a specified cluster node before or after starting big data components. You can run bootstrap actions to install additional third-party software, modify the cluster running environment, and perform other customizations.

If you choose to run bootstrap actions when scaling out a cluster, the bootstrap actions will be run on the newly added nodes in the same way. If auto scaling is enabled in the cluster, you can add an automation script in addition to configuring a resource plan. Then the automation script executes the corresponding script on the nodes that are scaled out or in to implement custom operations.

MRS runs the script you specify as user  **root**. You can run the  **su -  _XXX_**  command in the script to switch the user.

>![](/images/icon-note.gif) **NOTE:**   
>The bootstrap action scripts must be executed as user  **root**. Improper use of the script may affect the cluster availability. Therefore, exercise caution when performing this operation.  

MRS determines the result based on the return code after the execution of the bootstrap action script. If the return code is  **0**, the script is executed successfully. If the return code is not  **0**, the execution fails. If a bootstrap action script fails to be executed on a node, the corresponding boot script will fail to be executed. In this case, you can set  **Action upon Failure**  to choose whether to continue to execute the subsequent scripts. Example 1: If a script fails to be executed and  **Action upon Failure**  is set to  **Stop**, subsequent scripts will not be executed and cluster creation or scale-out will fail. Example 2: If you set  **Action upon Failure**  to  **Continue**  for all scripts during cluster creation, all the scripts will be executed regardless of whether the scripts are successfully executed or fail to be executed, and the startup process is complete.

You can add a maximum of 18 bootstrap actions, which will be executed before or after the cluster component is started in the order you specified. The bootstrap actions performed before or after the component startup must be completed within 60 minutes. Otherwise, the cluster creation or scale-out will fail.

