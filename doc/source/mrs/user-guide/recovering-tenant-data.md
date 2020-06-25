# Recovering Tenant Data<a name="EN-US_TOPIC_0125375962"></a>

## Scenario<a name="section22248508195314"></a>

Tenant data is stored on MRS Manager and in cluster components by default. When components are recovered from faults or reinstalled, some tenant configuration data may be abnormal. In this case, you can  manually recover the tenant data.

## Procedure<a name="section13550232195331"></a>

1.  On MRS Manager, click  **Tenant**.
2.  In the tenant list on the left, click a tenant node.
3.  Check the status of the tenant data.
    1.  In  **Summary**, check the color of the circle on the left of **Basic Information**. Green indicates that the tenant is available and gray indicates that the tenant is unavailable.
    2.  Click  **Resource**, and check the color of the circle on the left of **Yarn** or **HDFS Storage**. Green indicates that the resource is available and gray indicates that the resource is unavailable.
    3.  Click  **Service Association**, and check the **Status** column of the associated service table. **Good** indicates that the component can provide services for the associated tenant, while **Bad** indicates that the component cannot.
    4.  If any of the preceding check items is abnormal, go to  [4](#li10849798195335)  to recover tenant data.

4.  <a name="li10849798195335"></a>Click  **Restore Tenant Data**.
5.  In the  **Restore Tenant Data** window, select one or more components whose data needs to be recovered, and click **OK**. The system automatically recovers the tenant data.

