# Binding and Unbinding an EIP<a name="en-us_topic_public_sqlserver_accessibility"></a>

## **Scenarios**<a name="en-us_topic_0192953725_section26758795194119"></a>

By default, a DB instance is not publicly accessible \(not bound with an EIP\) after being created. You can bind an EIP to the DB instance for public accessibility and can unbind the EIP from the DB instance as required.

>![](public_sys-resources/icon-notice.gif) **NOTICE:**   
>To ensure successful access to the database, the security group associated with the database must allow access over the database port. For example, if the database port is 8635, ensure that the security group allow access over the 8635 port.  

## Prerequisites<a name="en-us_topic_0192953725_section25123869979"></a>

-   You have assigned an EIP on the VPC console.
-   You can bind an EIP to a primary DB instance or read replica only.
-   If a DB instance has already been bound with an EIP, you must unbind the EIP from the DB instance first before binding a new EIP to it.

>![](public_sys-resources/icon-note.gif) **NOTE:**   
>This function is currently unavailable for some existing DB instances because the connection IP addresses were created in a way that does not support binding EIPs.  

## Binding an EIP<a name="en-us_topic_0192953725_section3199593620428"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the target DB instance.
5.  On the  **EIPs**  page, click  **Bind EIP**.
6.  In the displayed dialog box, all unbound EIPs are listed. Select the EIP to be bound and click  **OK**. If no available EIPs are displayed, click  **View EIP**  and obtain an EIP.
7.  On the  **EIPs**  page, view the EIP that has been bound to the DB instance.

    You can also view the progress and result of binding an EIP to a DB instance on the  **Task Center**  page.

    To unbind the EIP from the DB instance, see  [Unbinding an EIP](#en-us_topic_0192953725_section186511510267).


## Unbinding an EIP<a name="en-us_topic_0192953725_section186511510267"></a>

1.  Log in to the management console.
2.  Click  ![](figures/region.png)  in the upper left corner and select a region and a project.
3.  Click  **Service List**. Under  **Database**, click  **Relational Database Service**  to go to the RDS console. The RDS console is displayed.
4.  On the  **Instance Management**  page, click the DB instance that has been bound with an EIP.
5.  On the  **EIPs**  page, locate the target EIP to be unbound and click  **Unbind**. In the displayed dialog box, click  **Yes**.
6.  On the  **EIPs**  page, view the unbinding result.

    You can also view the progress and result of unbinding an EIP from a DB instance on the  **Task Center**  page.

    To bind an EIP to the DB instance again, see  [Binding an EIP](#en-us_topic_0192953725_section3199593620428).


