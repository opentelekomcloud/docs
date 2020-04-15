# Stopping or Uninstalling the Flume Client<a name="EN-US_TOPIC_0125375792"></a>

## Scenario<a name="s5425b99e39c347a98e219ba9fa37a50c"></a>

This section describes how to stop and start the Flume client as well as uninstall it when the Flume data collection channel is not required. 

## Procedure<a name="sa53a0b1d5cc242538abedac2c7be7075"></a>

-   Stopping the Flume client

Suppose the installation path of the Flume client is  **/opt/FlumeClient**. Run the following command to stop the Flume client: 

**cd /opt/FlumeClient/fusioninsight-flume-1.6.0/bin**

**./flume-manage.sh stop**

If the following information is displayed after the command execution, the Flume client is successfully stopped.

```
Stop Flume PID=120689 successful..
```

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>The Flume client will be automatically restarted after being stopped. If you do not need automatic restart, run the following command:   
>**./flume-manage.sh stop force**  
>If you want to restart the Flume client, run the following command:   
>**./flume-manage.sh start force**  

-   Uninstalling the Flume client

Suppose the installation path of the Flume client is  **/opt/FlumeClient**. Run the following command to uninstall the Flume client: 

**cd /opt/FlumeClient/fusioninsight-flume-1.6.0/inst**

**./uninstall.sh**

