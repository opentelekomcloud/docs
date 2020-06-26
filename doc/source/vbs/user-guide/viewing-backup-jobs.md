# Viewing Backup Jobs<a name="EN-US_TOPIC_0112805386"></a>

On the  **Backup Jobs**  panel of the backup policy, you can view all backup jobs of the selected backup policy. If a backup job is in the  **Failed**  or  **Timed out**  state, you can click  **Back Up Again**  in the  **Operation**  column to manually back up the EVS disk again.

In the upper right corner of the list, you can select a state from the  **All statuses**  drop-down list to search for backup jobs.

The  **Backup Jobs**  list can show policy-driven backup jobs that have been executed in the past 30 days.

For policy-driven backup jobs executed more than 30 days ago, you can check whether they are successful on the VBS backup list:

1.  If a backup was generated at the specified point in time more than 30 days ago and it is in the  **Available**  state, the backup job is successful.
2.  If the expected backup is not displayed, the existing number of backups has not reached the maximum allowed value and you have not deleted it, or the backup is displayed but it is in the  **Error**  state, the backup job has failed.

    >![](/images/icon-note.gif) **NOTE:**   
    >For  **Failed**  backup jobs that were completed in the last date, the management console can report alarms to tenants through email and text message \(if tenants have registered their email addresses and mobile phone numbers\).  


