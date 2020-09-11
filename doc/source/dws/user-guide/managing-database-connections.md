# Managing Database Connections<a name="dws_01_0039"></a>

## Scenario<a name="section17619740162122"></a>

This section describes how to manage database connections to optimize database performance when the number of users and applications that can connect to the database is limited.

## Viewing the Maximum Number of Connections<a name="section63237288162656"></a>

1.  Use the SQL client tool to connect to the database in a cluster.
2.  Run the following command:

    **SHOW max\_connections;**

    The following information shows that the maximum number of database connections is  **200**  by default.

    ```
    max_connections
    ----------------- 
    200
    (1 row)
    ```


## Viewing the Number of Used Connections<a name="section51149057162719"></a>

1.  Use the SQL client tool to connect to the database in a cluster.
2.  View the number of connections in scenarios described in  [Table 1](#tecae727d5c1d47f897891d48c13a5589).

    **Table  1**  Viewing the number of connections

    <a name="tecae727d5c1d47f897891d48c13a5589"></a>
    <table><thead align="left"><tr id="r179959cf45364cf58c799bda03c7bb64"><th class="cellrowborder" valign="top" width="31.41%" id="mcps1.2.3.1.1"><p id="ae171f1cd533b4726b49baf1132425434"><a name="ae171f1cd533b4726b49baf1132425434"></a><a name="ae171f1cd533b4726b49baf1132425434"></a><strong id="b3780005091637"><a name="b3780005091637"></a><a name="b3780005091637"></a>Description</strong></p>
    </th>
    <th class="cellrowborder" valign="top" width="68.58999999999999%" id="mcps1.2.3.1.2"><p id="a28ea6d3b74bd402e9d3dcfeeb2e0746f"><a name="a28ea6d3b74bd402e9d3dcfeeb2e0746f"></a><a name="a28ea6d3b74bd402e9d3dcfeeb2e0746f"></a><strong id="b997270598115138"><a name="b997270598115138"></a><a name="b997270598115138"></a>Command</strong></p>
    </th>
    </tr>
    </thead>
    <tbody><tr id="rf78f73de6ad54b2a8e09f2d3382d3dbd"><td class="cellrowborder" valign="top" width="31.41%" headers="mcps1.2.3.1.1 "><p id="afb7e4b301e2843e7a08a5ff536ddbeed"><a name="afb7e4b301e2843e7a08a5ff536ddbeed"></a><a name="afb7e4b301e2843e7a08a5ff536ddbeed"></a>View the maximum number of sessions connected to a specific user.</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.58999999999999%" headers="mcps1.2.3.1.2 "><p id="ab8dd33c527184267906ad039a6609f45"><a name="ab8dd33c527184267906ad039a6609f45"></a><a name="ab8dd33c527184267906ad039a6609f45"></a>Run the following command to view the maximum number of sessions connected to user <strong id="b865093478115336"><a name="b865093478115336"></a><a name="b865093478115336"></a>dbadmin</strong>. <span class="parmvalue" id="parmvalue1796574260115424"><a name="parmvalue1796574260115424"></a><a name="parmvalue1796574260115424"></a><b>-1</b></span> indicates that the number of sessions connected to user <strong id="b2043011165115517"><a name="b2043011165115517"></a><a name="b2043011165115517"></a>dbadmin</strong> is not limited.</p>
    <pre class="screen" id="screen5384699191838"><a name="screen5384699191838"></a><a name="screen5384699191838"></a>postgres=# SELECT ROLNAME,ROLCONNLIMIT FROM PG_ROLES WHERE ROLNAME='dbadmin';
     rolname  | rolconnlimit
    ----------+--------------
     dwsadmin |           -1
    (1 row)</pre>
    </td>
    </tr>
    <tr id="rb9364ee1488746ba915d61980913738b"><td class="cellrowborder" valign="top" width="31.41%" headers="mcps1.2.3.1.1 "><p id="a84b65df54eb7428fb4beefcf68b01d51"><a name="a84b65df54eb7428fb4beefcf68b01d51"></a><a name="a84b65df54eb7428fb4beefcf68b01d51"></a>View the number of session connections that have been used by a user.</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.58999999999999%" headers="mcps1.2.3.1.2 "><p id="a7bbf9e48551c4e42bc4e3d96f03ef5f9"><a name="a7bbf9e48551c4e42bc4e3d96f03ef5f9"></a><a name="a7bbf9e48551c4e42bc4e3d96f03ef5f9"></a>Run the following command to view the number of session connections that have been used by <strong id="b125312233611565"><a name="b125312233611565"></a><a name="b125312233611565"></a>dbadmin</strong>. <span class="parmvalue" id="parmvalue1935199523115611"><a name="parmvalue1935199523115611"></a><a name="parmvalue1935199523115611"></a><b>1</b></span> indicates the number of session connections that have been used by <strong id="b745440350115630"><a name="b745440350115630"></a><a name="b745440350115630"></a>dbadmin</strong>.</p>
    <pre class="screen" id="screen32646809135149"><a name="screen32646809135149"></a><a name="screen32646809135149"></a>postgres=# SELECT COUNT(*) FROM V$SESSION WHERE USERNAME='dbadmin';
    
     count
    -------
         1
    (1 row)</pre>
    </td>
    </tr>
    <tr id="r889ca3da3fd94fac8d7084502eb05337"><td class="cellrowborder" valign="top" width="31.41%" headers="mcps1.2.3.1.1 "><p id="a299da3745d0b40e48789114e0fa70011"><a name="a299da3745d0b40e48789114e0fa70011"></a><a name="a299da3745d0b40e48789114e0fa70011"></a>View the maximum number of sessions connected to a specific database.</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.58999999999999%" headers="mcps1.2.3.1.2 "><p id="ac7ab9e1f26c84b959f03594e27683d08"><a name="ac7ab9e1f26c84b959f03594e27683d08"></a><a name="ac7ab9e1f26c84b959f03594e27683d08"></a>Run the following command to view the maximum number of sessions that are allowed to connect to database <strong id="b1058998606115824"><a name="b1058998606115824"></a><a name="b1058998606115824"></a>postgres</strong>. <span class="parmvalue" id="parmvalue389108586115837"><a name="parmvalue389108586115837"></a><a name="parmvalue389108586115837"></a><b>-1</b></span> indicates that the number of sessions connected to database <strong id="b55587509011593"><a name="b55587509011593"></a><a name="b55587509011593"></a>postgres</strong> is not limited.</p>
    <pre class="screen" id="s116628f616314f27a5a02cd806cf7e23"><a name="s116628f616314f27a5a02cd806cf7e23"></a><a name="s116628f616314f27a5a02cd806cf7e23"></a>postgres=# SELECT DATNAME,DATCONNLIMIT FROM PG_DATABASE WHERE DATNAME='postgres';
    
     datname  | datconnlimit
    ----------+--------------
     postgres |           -1
    (1 row)</pre>
    </td>
    </tr>
    <tr id="r1d23eb9755ed45379a778f04d1a7ceea"><td class="cellrowborder" valign="top" width="31.41%" headers="mcps1.2.3.1.1 "><p id="af67879da387345dc9470f0d5872e160c"><a name="af67879da387345dc9470f0d5872e160c"></a><a name="af67879da387345dc9470f0d5872e160c"></a>View the number of session connections that have been used by a database.</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.58999999999999%" headers="mcps1.2.3.1.2 "><p id="adc65e02e0fde4ae2ae7bda282f3eb6a4"><a name="adc65e02e0fde4ae2ae7bda282f3eb6a4"></a><a name="adc65e02e0fde4ae2ae7bda282f3eb6a4"></a>Run the following command to view the number of session connections that have been used by <strong id="b1270571750115942"><a name="b1270571750115942"></a><a name="b1270571750115942"></a>postgres</strong>. <span class="parmvalue" id="parmvalue704494337115950"><a name="parmvalue704494337115950"></a><a name="parmvalue704494337115950"></a><b>1</b></span> indicates the number of connections that have been used by <strong id="b10474119711202"><a name="b10474119711202"></a><a name="b10474119711202"></a>postgres</strong>.</p>
    <pre class="screen" id="screen502887401659"><a name="screen502887401659"></a><a name="screen502887401659"></a>postgres=# SELECT COUNT(*) FROM PG_STAT_ACTIVITY WHERE DATNAME='postgres';
     count 
    -------
         1
    (1 row)</pre>
    </td>
    </tr>
    <tr id="rc9f924a62f4e4ea8b06e58653f1f3a90"><td class="cellrowborder" valign="top" width="31.41%" headers="mcps1.2.3.1.1 "><p id="aa5d31760ef1d4425bd3e68793c11148c"><a name="aa5d31760ef1d4425bd3e68793c11148c"></a><a name="aa5d31760ef1d4425bd3e68793c11148c"></a>View the number of session connections that have been used by all users.</p>
    </td>
    <td class="cellrowborder" valign="top" width="68.58999999999999%" headers="mcps1.2.3.1.2 "><p id="a1df256201d644b6cbaa4a5984fd7b554"><a name="a1df256201d644b6cbaa4a5984fd7b554"></a><a name="a1df256201d644b6cbaa4a5984fd7b554"></a>Run the following command to view the number of session connections that have been used by all users:</p>
    <pre class="screen" id="sf5d5e911ba2f485bba92984f0375526a"><a name="sf5d5e911ba2f485bba92984f0375526a"></a><a name="sf5d5e911ba2f485bba92984f0375526a"></a>postgres=# SELECT COUNT(*) FROM V$SESSION;
     count
    -------
         10
    (1 row)</pre>
    </td>
    </tr>
    </tbody>
    </table>


