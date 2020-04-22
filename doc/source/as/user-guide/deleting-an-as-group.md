# Deleting an AS Group<a name="EN-US_TOPIC_0042018375"></a>

## Scenarios<a name="section08931748103217"></a>

You can delete an AS group when it is no longer required.

-   If an AS group is not required during a specified period of time, you are advised to disable it but not delete it.
-   An AS group can be deleted only when it has no instances and no scaling action is being performed.
-   After an AS group is deleted, its AS policies and the alarm rules generated based on the AS policies configured for the AS group will be automatically deleted.

## Procedure<a name="section1959939911151"></a>

1.  Log in to the management console.
2.  Click  ![](figures/icon-region.png)  in the upper left corner and select the desired region and project.
3.  Under  **Computing**, click  **Auto Scaling**. In the navigation pane on the left, choose  **Instance Scaling**.
4.  In the AS group list, locate the row containing the target AS group and choose  **More**  \>  **Delete**  in the  **Operation**  column.
5.  In the displayed  **Delete AS Group**  dialog box, click  **Yes**.

