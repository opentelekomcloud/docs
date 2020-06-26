# Accessing the Storm WebUI<a name="EN-US_TOPIC_0125375658"></a>

## Scenario<a name="sb62fd1846df54baaba3b5b368d1a9cb2"></a>

The Storm WebUI provides a graphical interface for using Storm. Only streaming clusters with Kerberos authentication enabled support this function.

## Prerequisites<a name="sac8b14b63ec94a23b79fa09b5d108ee0"></a>

-   The password of user  **admin** has been obtained. The **admin**  password is specified by the user when the MRS cluster is created.
-   If a user other than  **admin** is used to access the Storm WebUI, the user must be added to the **storm** or **stormadmin**  user group.

## Procedure<a name="sf116c7b96ef244c2a3db130c6cc33344"></a>

1.  Access MRS Manager.
2.  Choose  **Service**  \>  **Storm**. In **Storm WebUI** of **Storm Summary**, click any UI link to access the Storm WebUI.

    >![](/images/icon-note.gif) **NOTE:**   
    >When accessing the Storm WebUI for the first time, you must add the address to the trusted site list.  

    The following information can be queried on the Storm WebUI:

    -   Storm cluster summary
    -   Nimbus summary
    -   Topology summary
    -   Supervisor summary
    -   Nimbus configurations


## Relevant Tasks<a name="sa6308b8625194bbab118217fa3fa15d9"></a>

**Query topology details.**

1.  Access the Storm WebUI.
2.  In  **Topology Summary**, click the desired topology to view its detailed information, status, Spouts information, Bolts information, and configurations.

