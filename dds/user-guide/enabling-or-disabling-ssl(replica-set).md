# Enabling or Disabling SSL<a name="dds_02_0016"></a>

## Scenarios<a name="en-us_topic_0085468614_section4282820218710"></a>

DDS allows you to use SSL to encrypt connections to a DB instance to protect your data.

-   If SSL is enabled, you can connect to a database using SSL. For details, see  [SSL Connection](connecting-to-a-db-instance-through-a-client(replica-set).md#section3730754113815).
-   If SSL is disabled, you can connect to the database using a common connection. For details, see  [Common Connection](connecting-to-a-db-instance-through-a-client(replica-set).md#en-us_topic_0085335422_sfc3bfb212a8440799f49320d91fc096c).

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>Enabling or disabling SSL will cause DB instance restart. Exercise caution when you perform this operation.  

## Enabling SSL<a name="en-us_topic_0085468614_en-us_topic_0049044698_section45421719172826"></a>

1.  On the  **Instance Management**  page, click the target replica set instance.
2.  In the  **DB Information**  area on the  **Basic Information**  page, click  ![](figures/icon-off.png)  to enable SSL in the  **SSL**  field.
3.  In the displayed dialog box, click  **Yes**.
4.  On the  **Basic Information**  page, view the modification result.

## Disabling SSL<a name="en-us_topic_0085468614_section4225593518277"></a>

1.  On the  **Instance Management**  page, click the target replica set instance.
2.  In the  **DB Information**  area on the  **Basic Information**  page, click  ![](figures/icon-on.png)  to disable SSL in the  **SSL**  field.
3.  In the displayed dialog box, click  **Yes**.
4.  On the  **Basic Information**  page, view the modification result.

