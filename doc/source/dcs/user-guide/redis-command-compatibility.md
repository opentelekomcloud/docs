# Redis Command Compatibility<a name="EN-US_TOPIC_0237964757"></a>

DCS is built on the Redis engine and supports the majority of Redis commands. Any clients that support Redis can access DCS. For security purposes, certain Redis commands are disabled in DCS. For more information about Redis commands, visit  [http://redis.io/commands](http://redis.io/commands).

>![](/images/icon-note.gif) **NOTE:**   
>-   DCS is compatible with Redis 3.0 and supports the GEO command of Redis 3.2. However, DCS does not support certain commands and scripts added in Redis 3.2 and 4.0, which are listed in  [Table 4](#table52388255).  
>-   Some Redis commands, such as  **FLUSHALL**, take a long time to run. While running these commands, DCS instances may not respond to other commands and change to the faulty state. However, after the command finishes executing, the instance will return to normal.  
>-   The time limit for executing a Redis command is 1 minute. After the execution of a command times out, your client will be automatically disconnected from the server.  

## DCS Instances in Single-Node or Master/Standby Mode<a name="section41198408"></a>

**Table  1**  Redis commands disabled in single-node and master/standby DCS instances

<a name="table18929475"></a>
<table><thead align="left"><tr id="row1362898"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p43285934"><a name="p43285934"></a><a name="p43285934"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p16499799"><a name="p16499799"></a><a name="p16499799"></a>Commands</p>
</th>
</tr>
</thead>
<tbody><tr id="row61415348"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p8587310"><a name="p8587310"></a><a name="p8587310"></a>Keys</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p24483500"><a name="p24483500"></a><a name="p24483500"></a>MIGRATE</p>
</td>
</tr>
<tr id="row19024912"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p64622928"><a name="p64622928"></a><a name="p64622928"></a>Server</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p67074697"><a name="p67074697"></a><a name="p67074697"></a>SLOWLOG, SLAVEOF, SHUTDOWN, SAVE, MONITOR, LASTSAVE, DEBUG SEGFAULT, DEBUG OBJECT, CONFIG SET, CONFIG REWRITE, CONFIG RESETSTAT, COMMAND INFO, COMMAND GETKEYS, COMMAND COUNT, COMMAND, BGSAVE, BGREWRITEAOF</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-notice.gif) **NOTICE:**   
>Redis clients receive "\(error\) ERR unknown command" from DCS and probably exhibit unpredictable behavior after running the disabled commands. DCS cannot control their behavior. For example, if the  **MONITOR**  command is run, redis-cli will keep waiting for monitoring results even after receiving "\(error\) ERR unknown command" from DCS and refuse to run other commands during the wait period.  

## DCS Instances in Cluster Mode<a name="section35241358"></a>

DCS instances in cluster mode do not support the following commands:

-   Redis commands disabled for single-node and master/standby DCS instances
-   Commands listed in  [Table 2](#table49788159)

**Table  2**  Redis commands disabled in cluster DCS instances

<a name="table49788159"></a>
<table><thead align="left"><tr id="row35932926"><th class="cellrowborder" valign="top" width="20%" id="mcps1.2.3.1.1"><p id="p24885883"><a name="p24885883"></a><a name="p24885883"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="80%" id="mcps1.2.3.1.2"><p id="p2490624"><a name="p2490624"></a><a name="p2490624"></a>Commands</p>
</th>
</tr>
</thead>
<tbody><tr id="row414006"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p33534532"><a name="p33534532"></a><a name="p33534532"></a>Server</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p31942611"><a name="p31942611"></a><a name="p31942611"></a>SYNC, PSYNC</p>
</td>
</tr>
<tr id="row19048051"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p66497125"><a name="p66497125"></a><a name="p66497125"></a>Script</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p17558060"><a name="p17558060"></a><a name="p17558060"></a>SCRIPT DEBUG</p>
</td>
</tr>
<tr id="row23804819"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p49142196"><a name="p49142196"></a><a name="p49142196"></a>Transaction</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p21094941"><a name="p21094941"></a><a name="p21094941"></a>DISCARD, EXEC, MULTI, UNWATCH, WATCH</p>
</td>
</tr>
<tr id="row55636749"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p10282806"><a name="p10282806"></a><a name="p10282806"></a>Connection</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p27600956"><a name="p27600956"></a><a name="p27600956"></a>SELECT</p>
<div class="note" id="note47082013"><a name="note47082013"></a><a name="note47082013"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p class="NotesTextinTable" id="p21084934"><a name="p21084934"></a><a name="p21084934"></a>Parameters of the SELECT command can only be set to <strong id="b55546680"><a name="b55546680"></a><a name="b55546680"></a>0</strong>.</p>
</div></div>
</td>
</tr>
<tr id="row30158076"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p26885128"><a name="p26885128"></a><a name="p26885128"></a>Keys</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p30211727"><a name="p30211727"></a><a name="p30211727"></a>MOVE, RESTORE</p>
</td>
</tr>
<tr id="row3470093"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p12642139"><a name="p12642139"></a><a name="p12642139"></a>Cluster</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p17380313"><a name="p17380313"></a><a name="p17380313"></a>CLUSTER</p>
</td>
</tr>
<tr id="row22205089"><td class="cellrowborder" valign="top" width="20%" headers="mcps1.2.3.1.1 "><p id="p53781803"><a name="p53781803"></a><a name="p53781803"></a>codis</p>
</td>
<td class="cellrowborder" valign="top" width="80%" headers="mcps1.2.3.1.2 "><p id="p61358777"><a name="p61358777"></a><a name="p61358777"></a>PSUBSCRIBE(), PUBLISH, PUNSUBSCRIBE, SUBSCRIBE, RANDOMKEY, UNSUBSCRIBE, TIME, SLOTSINFO, SLOTSDEL, SLOTSMGRTSLOT, SLOTSMGRTONE, SLOTSCHECK, SLOTSMGRTTAGSLOT, SLOTSMGRTTAGONE</p>
</td>
</tr>
</tbody>
</table>

[Table 3](#table55973123)  lists the commands supported by cluster DCS instances for multi-key operations in the same slot.

**Table  3**  Commands supported by cluster DCS instances for multi-key operations in the same slot

<a name="table55973123"></a>
<table><thead align="left"><tr id="row45408440"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p54205018"><a name="p54205018"></a><a name="p54205018"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p28530324"><a name="p28530324"></a><a name="p28530324"></a>Commands</p>
</th>
</tr>
</thead>
<tbody><tr id="row29254927"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p20838899"><a name="p20838899"></a><a name="p20838899"></a>Set</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p10229222"><a name="p10229222"></a><a name="p10229222"></a>SINTERSTORE, SINTER, SUNIONSTORE, SUNION, SDIFFSTORE, SDIFF, SMOVE</p>
</td>
</tr>
<tr id="row24954142"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p8019630"><a name="p8019630"></a><a name="p8019630"></a>SortedSet</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p45610274"><a name="p45610274"></a><a name="p45610274"></a>ZUNIONSTORE, ZINTERSTORE</p>
</td>
</tr>
<tr id="row7839285"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p31002363"><a name="p31002363"></a><a name="p31002363"></a>HyperLogLog</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p28163481"><a name="p28163481"></a><a name="p28163481"></a>PFCOUNT, PFMERGE</p>
</td>
</tr>
<tr id="row52144745"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p62974848"><a name="p62974848"></a><a name="p62974848"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p689026"><a name="p689026"></a><a name="p689026"></a>BLPOP, BRPOP, BRPOPLPUSH</p>
</td>
</tr>
<tr id="row6201240"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p32538408"><a name="p32538408"></a><a name="p32538408"></a>Keys</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p18365401"><a name="p18365401"></a><a name="p18365401"></a>RENAME, RENAMENX, BITOP, RPOPLPUSH</p>
</td>
</tr>
<tr id="row31070885"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p33713770"><a name="p33713770"></a><a name="p33713770"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p46460835"><a name="p46460835"></a><a name="p46460835"></a>MSETNX</p>
</td>
</tr>
</tbody>
</table>

>![](/images/icon-notice.gif) **NOTICE:**   
>-   Redis clients receive "\(error\) ERR unknown command" from DCS and probably exhibit unpredictable behavior after running the disabled commands. DCS cannot control their behavior. For example, if the  **PSUBSCRIBE**,  **SUBSCRIBE**, or  **MONITOR**  command is run, redis-cli will keep waiting for responses from DCS even after receiving "\(error\) ERR unknown command" from DCS and refuse to run other commands during the wait period.  
>-   When the  **FLUSHDB**  or  **FLUSHALL**  command is run, execution of other service commands may be blocked for a long time in case of a large amount of cached data.  
>-   When the  **KEYS**  command is run, execution of other service commands may be blocked for a long time or even extra high memory may be occupied in case of a large amount of cached data. Therefore, when running the  **KEYS**  command, describe the exact pattern and do not use fuzzy  **keys \***.  **keys \***  can be used during commissioning or when the number of keys does not exceed 5 million. Otherwise, the service cannot run properly.  
>-   The hash tag mechanism can be used to ensure that multiple keys belong to the same slot. For details, visit  [https://redis.io/topics/cluster-spec](https://redis.io/topics/cluster-spec).  
>-   When the  **EVAL**  or  **EVALSHA**  command is run, a DCS cluster uses the first key to compute slots. Ensure that the keys to be operated in your code are in the same slot. For details, visit  [http://redis.io/commands](http://redis.io/commands).  
>-   For the  **EVAL**  command:  
>-   You are advised to learn the Lua script feature of Redis before running the  **EVAL**  command.  
>-   The execution timeout time of a Lua script is 5 seconds. Time-consuming statements such as long-time sleep and large loop statements should be avoided.  
>-   When calling a Lua script, do not use random functions to specify keys. Otherwise, the execution results are inconsistent on the master and standby nodes.  
>-   Cluster instances purchased before July 10, 2018 must be upgraded to support the following commands:  
>    SINTER, SDIFF, SUNION, PFCOUNT, PFMERGE, SINTERSTORE, SUNIONSTORE, SDIFFSTORE, SMOVE, BLPOP, BRPOP, BRPOPLPUSH, ZUNIONSTORE, ZINTERSTORE, EVAL, EVALSHA, BITOP, RENAME, RENAMENX, RPOPLPUSH, MSETNX, SCRIPT LOAD, SCRIPT KILL, SCRIPT EXISTS, SCRIPT FLUSH.  

## Commands and Scripts That Are Added in Later Redis Versions but Not Supported by DCS<a name="section17401426589"></a>

**Table  4**  Commands and scripts that are added in later Redis versions but not supported by DCS

<a name="table52388255"></a>
<table><thead align="left"><tr id="row23894041"><th class="cellrowborder" valign="top" width="35%" id="mcps1.2.3.1.1"><p id="p56369192"><a name="p56369192"></a><a name="p56369192"></a>Command/Script</p>
</th>
<th class="cellrowborder" valign="top" width="65%" id="mcps1.2.3.1.2"><p id="p2501835"><a name="p2501835"></a><a name="p2501835"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1322091"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="p39980527"><a name="p39980527"></a><a name="p39980527"></a>SPOP</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="p17197248"><a name="p17197248"></a><a name="p17197248"></a>Command used to control the number of randomly deleted elements. This command is added in Redis 3.2. Parameter not supported: <strong id="b20557504"><a name="b20557504"></a><a name="b20557504"></a>count</strong>.</p>
</td>
</tr>
<tr id="row50799813"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="p21144166"><a name="p21144166"></a><a name="p21144166"></a>HSTRLEN</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="p34955917"><a name="p34955917"></a><a name="p34955917"></a>Command used to return the value length of hash data. This command is added in Redis 3.2.</p>
</td>
</tr>
<tr id="row46167797"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="p48604061"><a name="p48604061"></a><a name="p48604061"></a>BITFIELD</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="p44614845"><a name="p44614845"></a><a name="p44614845"></a>Command used to calculate character strings as arrays of binary digits. This command is added in Redis 3.2.</p>
</td>
</tr>
<tr id="row65989290"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="p43532274"><a name="p43532274"></a><a name="p43532274"></a>SWAPDB</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="p36453319"><a name="p36453319"></a><a name="p36453319"></a>Command used to exchange the two databases specified in a DCS Redis instance. This command is added in Redis 4.0.</p>
</td>
</tr>
<tr id="row59644417"><td class="cellrowborder" valign="top" width="35%" headers="mcps1.2.3.1.1 "><p id="p66468500"><a name="p66468500"></a><a name="p66468500"></a>MEMORY</p>
</td>
<td class="cellrowborder" valign="top" width="65%" headers="mcps1.2.3.1.2 "><p id="p15239399"><a name="p15239399"></a><a name="p15239399"></a>Command used to query and manage the memory usage, for example, query the memory usage of a key, query the details of overall memory usage, apply for memory release, query the internal status of a memory allocator. This command is added in Redis 4.0.</p>
</td>
</tr>
</tbody>
</table>

