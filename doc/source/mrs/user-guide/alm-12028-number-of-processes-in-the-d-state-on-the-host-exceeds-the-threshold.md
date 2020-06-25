# ALM-12028 Number of Processes in the D State on the Host Exceeds the Threshold<a name="EN-US_TOPIC_0125375578"></a>

## Description<a name="s8edc49f7e0ec4ff3ac5fde4590a1a434"></a>

The system checks the number of processes of user  **omm**  that are in the D state on the host every 30 seconds and compares the number with the threshold. This alarm is generated when the number of processes in the D state exceeds the threshold and is cleared when the number is less than or equal to the threshold.

## Attribute<a name="s9c83e728937a446baa7e89255f9be8f0"></a>

<a name="ta28e661f46004eb3910029d6a79da32d"></a>
<table><thead align="left"><tr id="ra8c863d2faa14c759f53b476028f0236"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a9ae2467277d641e3855626bb189a28e8"><a name="a9ae2467277d641e3855626bb189a28e8"></a><a name="a9ae2467277d641e3855626bb189a28e8"></a><strong id="aff8b84073bab41de8835bdf30c81d710"><a name="aff8b84073bab41de8835bdf30c81d710"></a><a name="aff8b84073bab41de8835bdf30c81d710"></a>Alarm ID</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="en-us_topic_0035509086_p778217311143"><a name="en-us_topic_0035509086_p778217311143"></a><a name="en-us_topic_0035509086_p778217311143"></a><strong id="en-us_topic_0035509086_b293069911143"><a name="en-us_topic_0035509086_b293069911143"></a><a name="en-us_topic_0035509086_b293069911143"></a>Alarm Severity</strong></p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="ab737f3a8a36742a78947be611f405d63"><a name="ab737f3a8a36742a78947be611f405d63"></a><a name="ab737f3a8a36742a78947be611f405d63"></a><strong id="a006401631ea14279ad20b5d6380aa533"><a name="a006401631ea14279ad20b5d6380aa533"></a><a name="a006401631ea14279ad20b5d6380aa533"></a>Automatically Cleared</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="rcfb0e1f463c946bd8961070ccf6a6536"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a4698df76e7c74b1b85df71b6702e1f79"><a name="a4698df76e7c74b1b85df71b6702e1f79"></a><a name="a4698df76e7c74b1b85df71b6702e1f79"></a>12028</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="a6c79c7afa8a14350ba46599f5fe90761"><a name="a6c79c7afa8a14350ba46599f5fe90761"></a><a name="a6c79c7afa8a14350ba46599f5fe90761"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="en-us_topic_0035509086_p410086511143"><a name="en-us_topic_0035509086_p410086511143"></a><a name="en-us_topic_0035509086_p410086511143"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="sa7ec7c5427fb4c98b0569d0a6062bf85"></a>

<a name="tb1555f4314294d95b53de22fdff78635"></a>
<table><thead align="left"><tr id="rba73335ec7e3405aacc38b01124f3aff"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="en-us_topic_0035509086_p899478511143"><a name="en-us_topic_0035509086_p899478511143"></a><a name="en-us_topic_0035509086_p899478511143"></a><strong id="a3f168979d25246ff85334dba58d6cffc"><a name="a3f168979d25246ff85334dba58d6cffc"></a><a name="a3f168979d25246ff85334dba58d6cffc"></a>Parameter</strong></p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="ac9eaf1ba08aa43479a80ecd53da85661"><a name="ac9eaf1ba08aa43479a80ecd53da85661"></a><a name="ac9eaf1ba08aa43479a80ecd53da85661"></a><strong id="ac7c45f5c072b46fdb56394bdf471e25e"><a name="ac7c45f5c072b46fdb56394bdf471e25e"></a><a name="ac7c45f5c072b46fdb56394bdf471e25e"></a>Description</strong></p>
</th>
</tr>
</thead>
<tbody><tr id="r661e58de6b994045830d017a310e18e1"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a7e6de475457044bdbb78de9999d14322"><a name="a7e6de475457044bdbb78de9999d14322"></a><a name="a7e6de475457044bdbb78de9999d14322"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ae81399ce79704f3eb595e407008adf15"><a name="ae81399ce79704f3eb595e407008adf15"></a><a name="ae81399ce79704f3eb595e407008adf15"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="r792430d4d1a04c55865deab3a858fc4e"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a47579d3b02a0488b9612094db505e14d"><a name="a47579d3b02a0488b9612094db505e14d"></a><a name="a47579d3b02a0488b9612094db505e14d"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac3a80be14fee4eab9eabe23694f6f5cc"><a name="ac3a80be14fee4eab9eabe23694f6f5cc"></a><a name="ac3a80be14fee4eab9eabe23694f6f5cc"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="r6569be2702f14b1cbdaeb7540b013c12"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="aadbc4210d01742eb980a1a5dbabb5961"><a name="aadbc4210d01742eb980a1a5dbabb5961"></a><a name="aadbc4210d01742eb980a1a5dbabb5961"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a6b167a470617474d93b71bd3a0600d79"><a name="a6b167a470617474d93b71bd3a0600d79"></a><a name="a6b167a470617474d93b71bd3a0600d79"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
<tr id="r9faae9596b4141029f39ef78fcb8c0a1"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="af90d87a0e8a54c1fb8c4b90bc8f92529"><a name="af90d87a0e8a54c1fb8c4b90bc8f92529"></a><a name="af90d87a0e8a54c1fb8c4b90bc8f92529"></a>Trigger Condition</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="en-us_topic_0035509086_p443250011143"><a name="en-us_topic_0035509086_p443250011143"></a><a name="en-us_topic_0035509086_p443250011143"></a>Generates an alarm when the actual indicator value exceeds the specified threshold.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s718af49c6a5348519915982c4c295824"></a>

Excessive system resources are used and service processes respond slowly.

## Possible Causes<a name="scc019b8fc3314861b02baab6b9506f7d"></a>

The host responds slowly to I/O \(disk I/O and network I/O\) requests and a process is in the D state.

## **Procedure**<a name="s112474b5ee504fd79acff730482d10ec"></a>

1.  Check the process that is in the D state.
    1.  In the alarm list on MRS Manager, locate the row that contains the alarm, and view the IP address of the alarm host in the alarm details.
    2.  Log in to the alarm node.
    3.  Run the following command to switch the user:

        **sudo su - root**

        **su - omm**

    4.  Run the following command to view the PID of the process of user  **omm**  that is in the D state:

        **ps -elf | grep -v "\\\[thread\_checkio\\\]" | awk 'NR!=1 \{print $2, $3, $4\}' | grep omm | awk -F' ' '\{print $1, $3\}' | grep D | awk '\{print $2\}'**

    5.  Check whether no command output is displayed.
        -   If yes, the service process is running properly. Go to  [1.g](#l1fca8746a9ab4b948e41734d92c64181).
        -   If no, go to  [1.f](#l902aa97a80dc49a89113c715d79233b3).

    6.  <a name="l902aa97a80dc49a89113c715d79233b3"></a>Switch to user  **root** and run the **reboot**  command to restart the alarm host.

        Restarting the host is risky. Ensure that the service process runs properly after the restart.

    7.  <a name="l1fca8746a9ab4b948e41734d92c64181"></a>Wait 5 minutes and check whether the alarm is cleared.
        -   If yes, no further action is required.
        -   If no, go to  [2](#l9c007aace97b45ecab3954ef77aa0430).

2.  <a name="l9c007aace97b45ecab3954ef77aa0430"></a>Collect fault information.
    1.  On MRS Manager, choose  **System**  \>  **Export Log**.
    2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).


## **Related Information**<a name="sc470765132fc44c4802cb2b932b56f39"></a>

N/A

