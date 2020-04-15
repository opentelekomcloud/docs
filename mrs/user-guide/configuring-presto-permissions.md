# Configuring Presto Permissions<a name="EN-US_TOPIC_0221415077"></a>

Presto permission configuration is supported in MRS 2.1.0 or later.

## Configuring Presto Permissions in a Security Cluster<a name="section03361729163916"></a>

By default, the Hive Catalog authorization of the Presto component is enabled in a security cluster. The Presto permission configuration procedure is as follows:

1.  Log in to MRS Manager. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md).
2.  Choose  **System**  \>  **Manage Role**, configure a role that has the Hive database/table permissions, and bind the role to the user.

## Configuring Presto Permissions in a Normal Cluster<a name="section1790764493916"></a>

By default, Presto authorization is not enabled in a normal cluster. You need to manually configure Presto permissions as follows:

1.  Go to the MRS cluster details page.
2.  Choose  **Components**  \>  **Hive**. Set  **Type**  to  **All**. On the displayed Hive configuration page, modify parameter settings.
3.  Search for and modify the following parameters:
    -   Set  **hive.security.authorization.enabled**  to  **true**.
    -   Set  **hive.security.authorization.manager**  to  **org.apache.hadoop.hive.ql.security.authorization.plugin.sqlstd.SQLStdHiveAuthorizerFactory**.

4.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the Hive service.
5.  Choose  **Components**  \>  **Presto**. Set  **Type**  to  **All**. On the displayed Presto configuration page, modify parameter settings.
6.  Search for and modify the value of  **hive.security**  to  **sql-standard-with-group**.
7.  Click  **Save Configuration**  and select  **Restart the affected services or instances**  to restart the Presto service.
8.  Log in to MRS Manager. For details, see  [Accessing MRS Manager](accessing-mrs-manager.md).
9.  Choose  **System**  \>  **Change OMS Database Password**  \>  **Restart the OMS service**.
10. Choose  **System**  \>  **Manage Role**, configure a role that has the Hive database/table permissions, and bind the role to the user.

