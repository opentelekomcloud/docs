# Using the Encryption Tool of the Flume Client<a name="EN-US_TOPIC_0125376046"></a>

## Scenario<a name="s1df7777105694de5abe2a478dd417a86"></a>

The Flume client provides an encryption tool to encrypt some parameter values in the configuration file.

## Prerequisites<a name="s6f7b23058db34805bc813b53536817b9"></a>

You have installed the Flume client.

## **Procedure**<a name="sfd5554677bfe471bb013c56ca46d2b1c"></a>

1.  Log in to the Flume client node and go to the client installation directory, for example,  **/opt/FlumeClient**.
2.  Run the following command to switch the directory:

    **cd fusioninsight-flume-1.6.0/bin**

3.  Run the following command to encrypt information:

    **./genPwFile.sh**

    Input the information that you want to encrypt twice.

4.  Run the following command to query the encrypted information:

    **cat password.property**

    >![](public_sys-resources/icon-note.gif) **NOTE:**   
    >If the encryption parameter is used for the Flume server, you need to perform encryption on the corresponding Flume server node. The path for the encryption script is  **/opt/Bigdata/FusionInsight/FusionInsight-Flume-1.6.0/flume/bin/genPwFile.sh**. Execute the encryption script as user **omm**.  


