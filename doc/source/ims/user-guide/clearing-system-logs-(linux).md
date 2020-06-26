# Clearing System Logs<a name="EN-US_TOPIC_0125076462"></a>

Delete log files  and historical records, and stop the ECS.

1.  Run the following commands to delete redundant key files:

    **echo** **\>** _/$path/$to/$root_**/.ssh/authorized\_keys**

    An example command is  **echo \> /root/.ssh/authorized\_keys**.

    **echo** **\>** _/$path/$to/$none-root_**/.ssh/authorized\_keys**

    An example command is  **echo \> /home/linux/.ssh/authorized\_keys**.


1.  Run the following command to clear log files in the  **/var/log**  directory:

    **rm** **-rf** **/var/log/\***

2.  Run the following commands to clear historical records:

    **history** **-w**

    **echo** **\>** **/root/.bash\_history**

    **history** **-c**

    **history** **-c**

    **history** **-c**


