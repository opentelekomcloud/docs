# ALM-12043 DNS Resolution Duration Exceeds the Threshold<a name="EN-US_TOPIC_0125375339"></a>

## Description<a name="s0ec2e688ab1941e1b226993a3357045c"></a>

The system checks the DNS resolution duration every 30 seconds and compares the actual DNS resolution duration with the threshold \(the default threshold is 20,000 ms\). This alarm is generated when the system detects that the DNS resolution duration exceeds the threshold for several times \(2 times by default\) consecutively.

To change the threshold, choose  **System**  \>  **Threshold Configuration**  \>  **Device**  \>  **Host**  \>  **Network Status**  \>  **DNS Name Resolution Duration**  \>  **DNS Name Resolution Duration**.

When the  **hit number**  is 1, this alarm is cleared when the DNS resolution duration is less than or equal to the threshold. When the  **hit number**  is not 1, this alarm is cleared when the DNS resolution duration is less than or equal to 90% of the threshold.

## Attribute<a name="s4793702b5feb416b9ac77987135d35a0"></a>

<a name="t633089f684534186ac9b2abfcfc77599"></a>
<table><thead align="left"><tr id="r2f5e1be16a734f21bbdf1ee82eb66b6a"><th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.1"><p id="a0a140e28bd1a4e4caa0ab00d48a3b5b9"><a name="a0a140e28bd1a4e4caa0ab00d48a3b5b9"></a><a name="a0a140e28bd1a4e4caa0ab00d48a3b5b9"></a>Alarm ID</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.2"><p id="ac56186b0205e4467b064c9cbc8e88c32"><a name="ac56186b0205e4467b064c9cbc8e88c32"></a><a name="ac56186b0205e4467b064c9cbc8e88c32"></a>Alarm Severity</p>
</th>
<th class="cellrowborder" valign="top" width="33.33333333333333%" id="mcps1.1.4.1.3"><p id="ab7707685c8274a4bb9822a250d201cc3"><a name="ab7707685c8274a4bb9822a250d201cc3"></a><a name="ab7707685c8274a4bb9822a250d201cc3"></a>Automatically Cleared</p>
</th>
</tr>
</thead>
<tbody><tr id="r258410fdfdff4f429f5a90da24da4092"><td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.1 "><p id="a02837ff31b8e4371ad662416fde878c6"><a name="a02837ff31b8e4371ad662416fde878c6"></a><a name="a02837ff31b8e4371ad662416fde878c6"></a>12043</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.2 "><p id="aa0e2780a127d4328ba9d83424fdde65f"><a name="aa0e2780a127d4328ba9d83424fdde65f"></a><a name="aa0e2780a127d4328ba9d83424fdde65f"></a>Major</p>
</td>
<td class="cellrowborder" valign="top" width="33.33333333333333%" headers="mcps1.1.4.1.3 "><p id="a9b395ec726cf4bb2ab6f926c0b2f753d"><a name="a9b395ec726cf4bb2ab6f926c0b2f753d"></a><a name="a9b395ec726cf4bb2ab6f926c0b2f753d"></a>Yes</p>
</td>
</tr>
</tbody>
</table>

## Parameters<a name="scb4e675040b840dda4370f8ba73c15ef"></a>

<a name="ta78115782a5640959af7ab2228054b3e"></a>
<table><thead align="left"><tr id="rf3936ce7ba084997b20b8d23c7e2662a"><th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.1"><p id="adc9bdf4dee634e1e973f5d10c7beddf8"><a name="adc9bdf4dee634e1e973f5d10c7beddf8"></a><a name="adc9bdf4dee634e1e973f5d10c7beddf8"></a>Parameter</p>
</th>
<th class="cellrowborder" valign="top" width="50%" id="mcps1.1.3.1.2"><p id="a875ecf913c8f4dbaa7dc27da1b93c700"><a name="a875ecf913c8f4dbaa7dc27da1b93c700"></a><a name="a875ecf913c8f4dbaa7dc27da1b93c700"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="r3a60c49342e54ad68cbb831c9c610d88"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="acd649f5fb54f4a8eab83c9738e241857"><a name="acd649f5fb54f4a8eab83c9738e241857"></a><a name="acd649f5fb54f4a8eab83c9738e241857"></a>ServiceName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a5901e54f7651460f84abede9be2c03c9"><a name="a5901e54f7651460f84abede9be2c03c9"></a><a name="a5901e54f7651460f84abede9be2c03c9"></a>Specifies the service for which the alarm is generated.</p>
</td>
</tr>
<tr id="rf3c13ce83e97411c8b9d67db106bad22"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3f3a8eaa94d64f0c9a800b07a7640248"><a name="a3f3a8eaa94d64f0c9a800b07a7640248"></a><a name="a3f3a8eaa94d64f0c9a800b07a7640248"></a>RoleName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="a8e3cfa97ab494b4e97029b7f8ffaeba2"><a name="a8e3cfa97ab494b4e97029b7f8ffaeba2"></a><a name="a8e3cfa97ab494b4e97029b7f8ffaeba2"></a>Specifies the role for which the alarm is generated.</p>
</td>
</tr>
<tr id="rfee6a92b257a41829d21e4296a030441"><td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.1 "><p id="a3fb3812c4a8a4b39ae51a39349d380aa"><a name="a3fb3812c4a8a4b39ae51a39349d380aa"></a><a name="a3fb3812c4a8a4b39ae51a39349d380aa"></a>HostName</p>
</td>
<td class="cellrowborder" valign="top" width="50%" headers="mcps1.1.3.1.2 "><p id="ac9ae91fc93cc44c9a27646075d1abb2e"><a name="ac9ae91fc93cc44c9a27646075d1abb2e"></a><a name="ac9ae91fc93cc44c9a27646075d1abb2e"></a>Specifies the host for which the alarm is generated.</p>
</td>
</tr>
</tbody>
</table>

## Impact on the System<a name="s3432ce031214475492d398c40324cebe"></a>

-   Kerberos-based secondary authentication is slow.
-   The ZooKeeper service is abnormal.
-   The node is faulty.

## Possible Causes<a name="s4234956d254e422082b4c841e227a27c"></a>

-   The node is configured with the DNS client.
-   The node is equipped with the DNS server and the DNS server is started.

## Procedure<a name="sbcf2af25fc354760b05b7d74ce9e13b1"></a>

**Check whether the node is configured with the DNS client.**

1.  On MRS Manager, click  **Alarm**.
2.  Check the value of  **HostName**  in the detailed alarm information to obtain the name of the host involved in this alarm.
3.  Use PuTTY to log in to the node for which the alarm is generated as user  **root**.
4.  Run the  **cat /etc/resolv.conf**  command to check whether the DNS client is installed.

    If information similar to the following is displayed, the DNS client is installed and started:

    ```
    namesever 10.2.3.4 
    namesever 10.2.3.4
    ```

    -   If yes, go to  [5](#lb191a844ab6d4334a7854f469033e680).
    -   If no, go to  [7](#lc83c394e9ecc477a8a2851ec03dd4c9b).

5.  <a name="lb191a844ab6d4334a7854f469033e680"></a>Run the  **vi /etc/resolv.conf**  command to comment out the following content using the number signs \(\#\) and save the file:

    ```
    # namesever 10.2.3.4  
    # namesever 10.2.3.4
    ```

6.  Check whether this alarm is cleared after 5 minutes.
    -   If yes, no further action is required.
    -   If no, go to  [7](#lc83c394e9ecc477a8a2851ec03dd4c9b).


**Check whether the node is equipped with the DNS server and the DNS server is started.**

1.  <a name="lc83c394e9ecc477a8a2851ec03dd4c9b"></a>Run the  **service named status**  command to check whether the DNS server is installed on the node:

    If information similar to the following is displayed, the DNS server is installed and started:

    ```
    Checking for nameserver BIND  
    version: 9.6-ESV-R7-P4 
    CPUs found: 8 
    worker threads: 8 
    number of zones: 17 
    debug level: 0 
    xfers running: 0 
    xfers deferred: 0 
    soa queries in progress: 0 
    query logging is ON 
    recursive clients: 4/0/1000 
    tcp clients: 0/100 
    server is up and running
    ```

    -   If yes, go to  [8](#l2b7cfa5ab1b04e5faf7b904a10f25ad9).
    -   If no, go to  [10](#lc85676e511d6403b8b1dc4e80b9b4676).

2.  <a name="l2b7cfa5ab1b04e5faf7b904a10f25ad9"></a>Run the  **service named stop**  command to stop the DNS service.
3.  Check whether this alarm is cleared after 5 minutes.
    -   If yes, no further action is required.
    -   If no, go to  [10](#lc85676e511d6403b8b1dc4e80b9b4676).


**Collect fault information.**

1.  <a name="lc85676e511d6403b8b1dc4e80b9b4676"></a>On MRS Manager, choose  **System**  \>  **Export Log**.
2.  Contact technical support engineers for help, detail see  [technical support](https://docs.otc.t-systems.com/en-us/public/learnmore.html).

## Related Information<a name="sc1f9ae766c9347109805ade7aa47e74e"></a>

N/A

