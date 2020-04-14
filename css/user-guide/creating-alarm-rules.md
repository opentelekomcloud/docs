# Creating Alarm Rules<a name="css_01_0043"></a>

You can create the alarm rules for cluster metrics on the Cloud Eye management console. If the monitored metrics meet the specified alarm rule, alarms are reported. In this case, you can learn about cluster exceptions in time and take proper measures to prevent business loss.

## Procedure<a name="section13368958185312"></a>

1.  Log in to the CSS management console. Click  **Clusters**  to switch to the  **Clusters**  page. Locate the row where the target cluster resides and click  **View Metric**  in the  **Operation**  column to switch to the Cloud Eye management console.
2.  In the left navigation pane, choose  **Alarm Management \> Alarm Rules**.
3.  On the displayed  **Alarm Rules**  page, click  **Create Alarm Rule**.
4.  In the displayed  **Create Alarm Rule**  dialog box, set parameters as prompted.

    You can create an alarm rule for a specific metric or use the alarm template to create alarm rules in batches for multiple cloud service instances. In this example, assume that you use the alarm template to create the alarm rule for the CSS cluster.

    1.  Specify  **Resource Type**,  **Dimension**, and  **Monitored Object**. Set  **Resource Type**  to  **Cloud Search Service**,  **Dimension**  to  **Cloud Search Server**, and  **Monitored Object**  to the name of the target cluster.
    2.  Click  **Next**.
    3.  Specify  **Method**,  **Template**, and  **Alarm Notification**.

        >![](public_sys-resources/icon-note.gif) **NOTE:**   
        >You need to specify parameters  **Topic**  and  **Trigger Condition**  only when  **Alarm Notification**  is selected.  

    4.  Click  **Next**.
    5.  Specify  **Name**.
    6.  Click  **Finish**.

    After an alarm rule is successfully created, it will be displayed in the alarm rule list


