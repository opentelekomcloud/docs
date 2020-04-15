# Configuring a Website Accessed by Browsers<a name="EN-US_TOPIC_0125376087"></a>

## Scenario<a name="s35f2580c2b064ba895f351d4a3accf10"></a>

Websites hosted in the MRS cluster can be accessed only using browsers. Google Chrome must be used, because the SSH channel enables the SOCKS proxy. The proxy must be enabled when any website is accessed.

## Prerequisites<a name="s3b0a6f6af18f4d199c7a802531fffac9"></a>

You have performed operations in  [Creating an SSH Channel to Connect an MRS Cluster and Configuring the Browser](creating-an-ssh-channel-to-connect-an-mrs-cluster-and-configuring-the-browser.md)  and obtained the floating IP addresses of the local proxy port and MRS Manager.

## Procedure<a name="s70d590a04fbb4fabbf9d1cb9382754d9"></a>

1.  Configure a browser proxy.
    -   Google Chrome
        1.  Create the  **rule.pac**  text file on the local PC. Copy the following content and save it to the file.

            ```
            function FindProxyForURL(url, host)
            {
                return "SOCKS5 localhost:1080";
            }
            ```

        2.  In the browser, choose  **Settings**  \>  **Show advanced settings**  \>  **Network**  \>  **Change proxy settings**  \>  **Connections**  \>  **LAN setting**.
        3.  Select  **Use automatic configuration script** and enter the path of the **rule.pac**  file.

            The path format is  **file://c:/Users/rule.pac**. Use the default format. Do not configure other parameters.

        4.  Save the configurations and close the  **Settings**  page.

2.  In the address bar of the browser, enter the address for accessing MRS Manager.

    Address format:  **https://_Floating IP address of_** **_MRS Manager_:28443/web**

    The username and password of the MRS cluster need to be entered for accessing clusters with Kerberos authentication enabled, for example, user  **admin**. They are not required for accessing clusters with Kerberos authentication disabled.

    When accessing the MRS Manager for the first time, you must add the address to the trusted site list.

3.  Prepare the website access address.
    1.  Obtain the website address format and the role instance according to  [Overview](web-uis-of-open-source-components.md).
    2.  Click  **Services**.
    3.  Click the specified service name, for example, HDFS.
    4.  Click  **Instance** and view **Service IP** of **NameNode\(Active\)**.

4.  In the address bar of the browser, enter the website address to access it.
5.  When logging out of the website, terminate and close the SSH channel.

