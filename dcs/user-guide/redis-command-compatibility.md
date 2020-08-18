# Redis Command Compatibility<a name="dcs-ug-180522002"></a>

This section describes DCS's compatibility with Redis commands, including supported commands, disabled commands, unsupported scripts and commands of later Redis versions, and restrictions on command usage.

For more information about the command syntax, visit the  [Redis official website](https://redis.io/commands).

DCS for Redis instances support most Redis commands. Any client compatible with the Redis protocol can access DCS.

-   For security purposes, some Redis commands are disabled in DCS. For details, see  [Commands Disabled by DCS for Redis 3.0](#section0341135531914).
-   Some Redis commands have usage restrictions, which are described in  [Other Command Usage Restrictions](#section834293511127).
-   Some Redis commands are supported by Proxy Cluster DCS instances for multi-key operations in the same slot. For details, see  [Table 4](#table7589193113396).

## Commands Supported by DCS for Redis 3.0<a name="section1274616272512"></a>

The following lists commands supported by DCS for Redis 3.0.

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>Commands available since later Redis versions are not supported by earlier versions. Run a command on redis-cli to check whether it is supported by DCS for Redis. If the message "\(error\) ERR unknown command" is returned, the command is not supported.

**Table  1**  Commands supported by DCS for Redis 3.0

<a name="table0944193819332"></a>
<table><thead align="left"><tr id="row194663813313"><th class="cellrowborder" valign="top" width="18.279999999999998%" id="mcps1.2.3.1.1"><p id="p1094616383337"><a name="p1094616383337"></a><a name="p1094616383337"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="81.72%" id="mcps1.2.3.1.2"><p id="p694663819333"><a name="p694663819333"></a><a name="p694663819333"></a>Command</p>
</th>
</tr>
</thead>
<tbody><tr id="row37211830175313"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p1672183019533"><a name="p1672183019533"></a><a name="p1672183019533"></a>Key</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p5762155105314"><a name="p5762155105314"></a><a name="p5762155105314"></a>DEL, DUMP, EXISTS, EXPIRE, MOVE, PERSISI, PTTL, RANDOMKEY, RENAME, RENAMENX, RESTORE, SORT, TTL, TYPE, SCAN, OBJIECT</p>
</td>
</tr>
<tr id="row5946163816334"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p4946133853313"><a name="p4946133853313"></a><a name="p4946133853313"></a>String</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p3252132482111"><a name="p3252132482111"></a><a name="p3252132482111"></a>APPEND, BITCOUNT, BITOP, BITPOS, DECR, DECRBY, GET, GETRANGE, GETSET, INCR, INCRBY, INCRBYFLOAT, MGET, MSET, MSETNX, PSETEX, SET, SETBIT, SETEX, SETNX, SETRANGE, STRLEN</p>
</td>
</tr>
<tr id="row694611389336"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p11946113833315"><a name="p11946113833315"></a><a name="p11946113833315"></a>Hash</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p1494623873315"><a name="p1494623873315"></a><a name="p1494623873315"></a>HDEL, HEXISTS, HGET, HGETALL, HINCRBY, HINCRBYFLOAT, HKEYS, HMGET, HMSET, HSET, HSETNX, HVALS, HSCAN</p>
</td>
</tr>
<tr id="row1594612388339"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p17946163811337"><a name="p17946163811337"></a><a name="p17946163811337"></a>List</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p18946183820334"><a name="p18946183820334"></a><a name="p18946183820334"></a>BLPOP, BRPOP, BRPOPLRUSH, LINDEX, LINSERT, LLEN, LPOP, LPUSHX, LRANGE, LREM, LSET, LTRIM, RPOP, RPOPLPU, RPOPLPUSH, RPUSH, RPUSHX</p>
<div class="note" id="note13541148141"><a name="note13541148141"></a><a name="note13541148141"></a><span class="notetitle"> NOTE: </span><div class="notebody"><p id="p1655101471417"><a name="p1655101471417"></a><a name="p1655101471417"></a>Proxy Cluster Redis 3.0 instances do not support <strong id="b1179782042816"><a name="b1179782042816"></a><a name="b1179782042816"></a>BLPOP</strong>, <strong id="b18992102292818"><a name="b18992102292818"></a><a name="b18992102292818"></a>BRPOP</strong>, and <strong id="b5763162572811"><a name="b5763162572811"></a><a name="b5763162572811"></a>BRPOPLRUSH</strong> commands.</p>
</div></div>
</td>
</tr>
<tr id="row194633814335"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p3946438103314"><a name="p3946438103314"></a><a name="p3946438103314"></a>Set</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p16946133815330"><a name="p16946133815330"></a><a name="p16946133815330"></a>SADD, SCARD, SDIFF, SDIFFSTORE, SINTER, SINTERSTORE, SISMEMBER, SMEMBERS, SMOVE, SPOP, SRANDMEMBER, SREM, SUNION, SUNIONSTORE, SSCAN</p>
</td>
</tr>
<tr id="row89461538113320"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p1494673863312"><a name="p1494673863312"></a><a name="p1494673863312"></a>Sorted set</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p139461238103311"><a name="p139461238103311"></a><a name="p139461238103311"></a>ZADD, ZCARD, ZCOUNT, ZINCRBY, ZRANGE, ZRANGEBYSCORE, ZRANK, ZREMRANGEBYRANK, ZREMRANGEBYCORE, ZREVRANGE, ZREVRANGEBYSCORE, ZREVRANK, ZSCORE, ZUNIONSTORE, ZINTERSTORE, ZSCAN, ZRANGEBYLEX</p>
</td>
</tr>
<tr id="row1766372119455"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p13658915134611"><a name="p13658915134611"></a><a name="p13658915134611"></a>HyperLogLog</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p665810154468"><a name="p665810154468"></a><a name="p665810154468"></a>PFADD, PFCOUNT, PFMERGE</p>
</td>
</tr>
<tr id="row1131012916454"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p116581815154614"><a name="p116581815154614"></a><a name="p116581815154614"></a>Pub/Sub</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p8658115134612"><a name="p8658115134612"></a><a name="p8658115134612"></a>PSUBSCRIBE, PUBLISH, PUBSUB, PUNSUBSCRIBE, SUBSCRIBE, UNSUBSCRIBE</p>
</td>
</tr>
<tr id="row5687435124513"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p13659315204619"><a name="p13659315204619"></a><a name="p13659315204619"></a>Transaction</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p965941511461"><a name="p965941511461"></a><a name="p965941511461"></a>DISCARD, EXEC, MULTI, UNWATCH, WATCH</p>
</td>
</tr>
<tr id="row85577413456"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p11659151511462"><a name="p11659151511462"></a><a name="p11659151511462"></a>Connection</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p7659515104617"><a name="p7659515104617"></a><a name="p7659515104617"></a>AUTH, ECHO, PING, QUIT, SELECT</p>
</td>
</tr>
<tr id="row3817847104513"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p1365991517464"><a name="p1365991517464"></a><a name="p1365991517464"></a>Server</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p156591815164612"><a name="p156591815164612"></a><a name="p156591815164612"></a>FLUSHALL, FLUSHDB, DBSIZE, TIME, INFO, KEYS, CLIENT KILL, CLIENT LIST, CLIENT GETNAME, CLIENT SETNAME, CONFIG GET, MONITOR, SLOWLOG, ROLE</p>
<div class="note" id="note1545101541112"><a name="note1545101541112"></a><a name="note1545101541112"></a><span class="notetitle"> NOTE: </span><div class="notebody"><a name="ul9976201671911"></a><a name="ul9976201671911"></a><ul id="ul9976201671911"><li>Proxy Cluster Redis 3.0 instances do not support CLIENT commands, including <strong id="b182271137112917"><a name="b182271137112917"></a><a name="b182271137112917"></a>CLIENT KILL</strong>, <strong id="b142091355294"><a name="b142091355294"></a><a name="b142091355294"></a>CLIENT GETNAME</strong>, <strong id="b1114063312918"><a name="b1114063312918"></a><a name="b1114063312918"></a>CLIENT LIST</strong>, <strong id="b8134133111298"><a name="b8134133111298"></a><a name="b8134133111298"></a>CLIENT SETNAME</strong>, <strong id="b12238929142913"><a name="b12238929142913"></a><a name="b12238929142913"></a>CLIENT PAUSE</strong>, and <strong id="b4404172712299"><a name="b4404172712299"></a><a name="b4404172712299"></a>CLIENT REPLY</strong>.</li><li>Proxy Cluster Redis 3.0 instances do not support the <strong id="b1212075252810"><a name="b1212075252810"></a><a name="b1212075252810"></a>MONITOR</strong> command.</li></ul>
</div></div>
</td>
</tr>
<tr id="row19877165134514"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p106591715134615"><a name="p106591715134615"></a><a name="p106591715134615"></a>Scripting</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p66590159468"><a name="p66590159468"></a><a name="p66590159468"></a>EVAL, EVALSHA, SCRIPT EXISTS, SCRIPT FLUSH, SCRIPT KILL, SCRIPT LOAD</p>
</td>
</tr>
<tr id="row676019555454"><td class="cellrowborder" valign="top" width="18.279999999999998%" headers="mcps1.2.3.1.1 "><p id="p11659161510469"><a name="p11659161510469"></a><a name="p11659161510469"></a>Geo</p>
</td>
<td class="cellrowborder" valign="top" width="81.72%" headers="mcps1.2.3.1.2 "><p id="p2065981520468"><a name="p2065981520468"></a><a name="p2065981520468"></a>GEOADD, GEOHASH, GEOPOS, GEODIST, GEORADIUS, GEORADIUSBYMEMBER</p>
</td>
</tr>
</tbody>
</table>

## Commands Disabled by DCS for Redis 3.0<a name="section0341135531914"></a>

Redis APIs of single-node and master/standby DCS instances are compatible with open-source Redis for data access. For ease of use and security purposes, some management operations cannot be initiated from a Redis client. Related commands are listed in  [Table 2](#table31856418216).

**Table  2**  Redis commands disabled in single-node and master/standby Redis 3.0 instances

<a name="table31856418216"></a>
<table><thead align="left"><tr id="row121851542218"><th class="cellrowborder" valign="top" width="26.889999999999997%" id="mcps1.2.3.1.1"><p id="p21856412218"><a name="p21856412218"></a><a name="p21856412218"></a>Command</p>
</th>
<th class="cellrowborder" valign="top" width="73.11%" id="mcps1.2.3.1.2"><p id="p118534122114"><a name="p118534122114"></a><a name="p118534122114"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1185104172116"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p71868414214"><a name="p71868414214"></a><a name="p71868414214"></a><strong id="b157567171292"><a name="b157567171292"></a><a name="b157567171292"></a>Key</strong></p>
</td>
</tr>
<tr id="row818614420213"><td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.3.1.1 "><p id="p2018674102116"><a name="p2018674102116"></a><a name="p2018674102116"></a>MIGRATE</p>
</td>
<td class="cellrowborder" valign="top" width="73.11%" headers="mcps1.2.3.1.2 "><p id="p101866412214"><a name="p101866412214"></a><a name="p101866412214"></a>Transfers a key from one Redis instance to another.</p>
</td>
</tr>
<tr id="row11186174192114"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p1218620411211"><a name="p1218620411211"></a><a name="p1218620411211"></a><strong id="b34478071018"><a name="b34478071018"></a><a name="b34478071018"></a>Server</strong></p>
</td>
</tr>
<tr id="row1418644192118"><td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.3.1.1 "><p id="p718674122116"><a name="p718674122116"></a><a name="p718674122116"></a>SLAVEOF</p>
</td>
<td class="cellrowborder" valign="top" width="73.11%" headers="mcps1.2.3.1.2 "><p id="p518616452118"><a name="p518616452118"></a><a name="p518616452118"></a>Changes the replication settings of a replica on the fly.</p>
</td>
</tr>
<tr id="row1218616462120"><td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.3.1.1 "><p id="p201861048219"><a name="p201861048219"></a><a name="p201861048219"></a>SHUTDOWN</p>
</td>
<td class="cellrowborder" valign="top" width="73.11%" headers="mcps1.2.3.1.2 "><p id="p81861449213"><a name="p81861449213"></a><a name="p81861449213"></a>Stops all the clients and quits the Redis process.</p>
</td>
</tr>
<tr id="row1318619432118"><td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.3.1.1 "><p id="p14186144192110"><a name="p14186144192110"></a><a name="p14186144192110"></a>LASTSAVE</p>
</td>
<td class="cellrowborder" valign="top" width="73.11%" headers="mcps1.2.3.1.2 "><p id="p0187247216"><a name="p0187247216"></a><a name="p0187247216"></a>Returns the time of the last successful data persistence to disk.</p>
</td>
</tr>
<tr id="row10187548212"><td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.3.1.1 "><p id="p618774152110"><a name="p618774152110"></a><a name="p618774152110"></a>DEBUG commands</p>
</td>
<td class="cellrowborder" valign="top" width="73.11%" headers="mcps1.2.3.1.2 "><p id="p101871843214"><a name="p101871843214"></a><a name="p101871843214"></a>Debugging command that should not be used by clients.</p>
</td>
</tr>
<tr id="row118724102115"><td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.3.1.1 "><p id="p51871542211"><a name="p51871542211"></a><a name="p51871542211"></a>COMMAND</p>
</td>
<td class="cellrowborder" valign="top" width="73.11%" headers="mcps1.2.3.1.2 "><p id="p21871747216"><a name="p21871747216"></a><a name="p21871747216"></a>Returns array reply of details about all Redis commands.</p>
</td>
</tr>
<tr id="row151881440219"><td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.3.1.1 "><p id="p31888415219"><a name="p31888415219"></a><a name="p31888415219"></a>SAVE</p>
</td>
<td class="cellrowborder" valign="top" width="73.11%" headers="mcps1.2.3.1.2 "><p id="p81881545213"><a name="p81881545213"></a><a name="p81881545213"></a>Performs a synchronous save on disk, producing a point in time snapshot of all the data inside the Redis instance, in the form of an RDB file.</p>
</td>
</tr>
<tr id="row16188184202119"><td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.3.1.1 "><p id="p1218864142114"><a name="p1218864142114"></a><a name="p1218864142114"></a>BGSAVE</p>
</td>
<td class="cellrowborder" valign="top" width="73.11%" headers="mcps1.2.3.1.2 "><p id="p318817422118"><a name="p318817422118"></a><a name="p318817422118"></a>Asynchronously saves the database on disk.</p>
</td>
</tr>
<tr id="row61884492120"><td class="cellrowborder" valign="top" width="26.889999999999997%" headers="mcps1.2.3.1.1 "><p id="p13188134192120"><a name="p13188134192120"></a><a name="p13188134192120"></a>BGREWRITEAOF</p>
</td>
<td class="cellrowborder" valign="top" width="73.11%" headers="mcps1.2.3.1.2 "><p id="p1018854172120"><a name="p1018854172120"></a><a name="p1018854172120"></a>Starts an Append Only File (AOF) rewrite process.</p>
</td>
</tr>
</tbody>
</table>

In additional to these commands, Proxy Cluster Redis 3.0 instances do not support the commands listed in  [Table 3](#table122021410155210).

**Table  3**  Redis commands disabled in Proxy Cluster Redis 3.0 instances

<a name="table122021410155210"></a>
<table><thead align="left"><tr id="row1720216106523"><th class="cellrowborder" valign="top" width="27.589999999999996%" id="mcps1.2.3.1.1"><p id="p15203121011520"><a name="p15203121011520"></a><a name="p15203121011520"></a>Command</p>
</th>
<th class="cellrowborder" valign="top" width="72.41%" id="mcps1.2.3.1.2"><p id="p12031210125213"><a name="p12031210125213"></a><a name="p12031210125213"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row1720313107525"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p10203171035220"><a name="p10203171035220"></a><a name="p10203171035220"></a><strong id="b13203181085212"><a name="b13203181085212"></a><a name="b13203181085212"></a>Server</strong></p>
</td>
</tr>
<tr id="row1203710135214"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p7203151045211"><a name="p7203151045211"></a><a name="p7203151045211"></a>SYNC</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p112033107522"><a name="p112033107522"></a><a name="p112033107522"></a>An internal command used for full replication.</p>
</td>
</tr>
<tr id="row42031810105212"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p1920341016527"><a name="p1920341016527"></a><a name="p1920341016527"></a>PSYNC</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p152032010155219"><a name="p152032010155219"></a><a name="p152032010155219"></a>An internal command used for partial replication.</p>
</td>
</tr>
<tr id="row5805623151117"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p61081236141115"><a name="p61081236141115"></a><a name="p61081236141115"></a>MONITOR</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p61087368112"><a name="p61087368112"></a><a name="p61087368112"></a>Streams back every command processed by the Redis server for debugging.</p>
</td>
</tr>
<tr id="row1558613521219"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p145865531219"><a name="p145865531219"></a><a name="p145865531219"></a>CLIENT commands</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p19267341181213"><a name="p19267341181213"></a><a name="p19267341181213"></a>CLIENT KILL, CLIENT GETNAME, CLIENT LIST, CLIENT SETNAME, CLIENT PAUSE, and CLIENT REPLY.</p>
</td>
</tr>
<tr id="row756631621316"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p1756612163131"><a name="p1756612163131"></a><a name="p1756612163131"></a>OBJECT</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p175661916181318"><a name="p175661916181318"></a><a name="p175661916181318"></a>Debugging command that should not be used by clients.</p>
</td>
</tr>
<tr id="row133501498148"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p1835118920142"><a name="p1835118920142"></a><a name="p1835118920142"></a>ROLE</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p143511491149"><a name="p143511491149"></a><a name="p143511491149"></a>Returns the role of the instance node.</p>
</td>
</tr>
<tr id="row7203181085211"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p1920471075214"><a name="p1920471075214"></a><a name="p1920471075214"></a><strong id="b020414100522"><a name="b020414100522"></a><a name="b020414100522"></a>Transaction</strong></p>
</td>
</tr>
<tr id="row17204191025219"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p920418108522"><a name="p920418108522"></a><a name="p920418108522"></a>DISCARD</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p3204111012520"><a name="p3204111012520"></a><a name="p3204111012520"></a>Flushes all previously queued commands in a transaction.</p>
</td>
</tr>
<tr id="row6204181015529"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p16204111065214"><a name="p16204111065214"></a><a name="p16204111065214"></a>EXEC</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p10204201075218"><a name="p10204201075218"></a><a name="p10204201075218"></a>Executes all previously queued commands in a transaction.</p>
</td>
</tr>
<tr id="row1820451025219"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p152041410115216"><a name="p152041410115216"></a><a name="p152041410115216"></a>MULTI</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p13204121085214"><a name="p13204121085214"></a><a name="p13204121085214"></a>Marks the start of a transaction block.</p>
</td>
</tr>
<tr id="row102041810125212"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p18204101019521"><a name="p18204101019521"></a><a name="p18204101019521"></a>UNWATCH</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p1720441045214"><a name="p1720441045214"></a><a name="p1720441045214"></a>Flushes all the previously watched keys for a transaction.</p>
</td>
</tr>
<tr id="row7204141016520"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p1720410108527"><a name="p1720410108527"></a><a name="p1720410108527"></a>WATCH</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p62041710195210"><a name="p62041710195210"></a><a name="p62041710195210"></a>Marks the given key or keys to be watched. If the key or keys are modified by other commands before WATCH is executed, the transaction is interrupted.</p>
</td>
</tr>
<tr id="row020491065217"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p10204151012521"><a name="p10204151012521"></a><a name="p10204151012521"></a><strong id="b192041210165213"><a name="b192041210165213"></a><a name="b192041210165213"></a>Connection</strong></p>
</td>
</tr>
<tr id="row1820515105525"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p16205110125211"><a name="p16205110125211"></a><a name="p16205110125211"></a>SELECT</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p7205141095216"><a name="p7205141095216"></a><a name="p7205141095216"></a>Selects the Redis database. Note: Parameters of the <strong id="b872710585208"><a name="b872710585208"></a><a name="b872710585208"></a>SELECT</strong> command can only be set to <strong id="b1874755812018"><a name="b1874755812018"></a><a name="b1874755812018"></a>0</strong>.</p>
</td>
</tr>
<tr id="row42051410115210"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p19205910145216"><a name="p19205910145216"></a><a name="p19205910145216"></a><strong id="b19262936143018"><a name="b19262936143018"></a><a name="b19262936143018"></a>Key</strong></p>
</td>
</tr>
<tr id="row16205171015220"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p122053102526"><a name="p122053102526"></a><a name="p122053102526"></a>MOVE</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p1520517106521"><a name="p1520517106521"></a><a name="p1520517106521"></a>Moves <em id="i84292874413"><a name="i84292874413"></a><a name="i84292874413"></a>key</em> of the currently selected database to the specified destination database.</p>
</td>
</tr>
<tr id="row6205910105213"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p112051910145212"><a name="p112051910145212"></a><a name="p112051910145212"></a><strong id="b162051910125218"><a name="b162051910125218"></a><a name="b162051910125218"></a>Cluster</strong></p>
</td>
</tr>
<tr id="row52051810155210"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p102051710185211"><a name="p102051710185211"></a><a name="p102051710185211"></a>CLUSTER</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p16205131095215"><a name="p16205131095215"></a><a name="p16205131095215"></a>Used for cluster management.</p>
</td>
</tr>
<tr id="row8205910185213"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p52051310195213"><a name="p52051310195213"></a><a name="p52051310195213"></a><strong id="b74941335191114"><a name="b74941335191114"></a><a name="b74941335191114"></a>codis</strong> (Proxy Cluster)</p>
</td>
</tr>
<tr id="row16205161015521"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p182052010185218"><a name="p182052010185218"></a><a name="p182052010185218"></a>TIME</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p152055105526"><a name="p152055105526"></a><a name="p152055105526"></a>Returns the current server time.</p>
</td>
</tr>
<tr id="row720517103527"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p520551018521"><a name="p520551018521"></a><a name="p520551018521"></a>SLOTSINFO</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p320591011527"><a name="p320591011527"></a><a name="p320591011527"></a>Returns the number of slots and the size of each slot in Redis.</p>
</td>
</tr>
<tr id="row92055103522"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p102061010165218"><a name="p102061010165218"></a><a name="p102061010165218"></a>SLOTSDEL</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p132062101529"><a name="p132062101529"></a><a name="p132062101529"></a>Deletes all key-value pairs in multiple slots in Redis.</p>
</td>
</tr>
<tr id="row182062105522"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p16206610155217"><a name="p16206610155217"></a><a name="p16206610155217"></a>SLOTSMGRTSLOT</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p2206121065215"><a name="p2206121065215"></a><a name="p2206121065215"></a>Randomly migrates a key-value pair in a slot to the destination.</p>
</td>
</tr>
<tr id="row4206210105218"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p5206171085217"><a name="p5206171085217"></a><a name="p5206171085217"></a>SLOTSMGRTONE</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p22061810185218"><a name="p22061810185218"></a><a name="p22061810185218"></a>Migrates a specified key-value pair to the destination.</p>
</td>
</tr>
<tr id="row520691018524"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p1720621095218"><a name="p1720621095218"></a><a name="p1720621095218"></a>SLOTSCHECK</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p1120615105526"><a name="p1120615105526"></a><a name="p1120615105526"></a>Checks whether slots meet the following consistency requirements:</p>
<a name="ul620615109523"></a><a name="ul620615109523"></a><ul id="ul620615109523"><li>All the keys in the slots have a corresponding value in the database.</li><li>All the keys in the database have a value in the corresponding slot.</li></ul>
</td>
</tr>
<tr id="row15206111075219"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p17206181015216"><a name="p17206181015216"></a><a name="p17206181015216"></a>SLOTSMGRTTAGSLOT</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p1720691005220"><a name="p1720691005220"></a><a name="p1720691005220"></a>Migrates all key-value pairs with the same tag as a randomly selected key in a slot.</p>
</td>
</tr>
<tr id="row0206141013527"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p1920621075213"><a name="p1920621075213"></a><a name="p1920621075213"></a>SLOTSMGRTTAGONE</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p52063104528"><a name="p52063104528"></a><a name="p52063104528"></a>Migrates all key-value pairs with the same tag as a specified key.</p>
</td>
</tr>
<tr id="row13206131015520"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p7207111016527"><a name="p7207111016527"></a><a name="p7207111016527"></a><strong id="b157211531161217"><a name="b157211531161217"></a><a name="b157211531161217"></a>List</strong></p>
</td>
</tr>
<tr id="row102071610185212"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p6207111045211"><a name="p6207111045211"></a><a name="p6207111045211"></a>BLPOP</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p620781020521"><a name="p620781020521"></a><a name="p620781020521"></a>The blocking version of <strong id="b1557317216296"><a name="b1557317216296"></a><a name="b1557317216296"></a>LPOP</strong> because it blocks the connection when there are no elements to pop from any of the given lists until the specified timeout has expired or a non-empty element is popped.</p>
</td>
</tr>
<tr id="row12207710165210"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p9207121005211"><a name="p9207121005211"></a><a name="p9207121005211"></a>BRPOP</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p112073108521"><a name="p112073108521"></a><a name="p112073108521"></a>The blocking version of <strong id="b6204125773320"><a name="b6204125773320"></a><a name="b6204125773320"></a>RPOP</strong> because it blocks the connection when there are no elements to pop from any of the given lists until the specified timeout has expired or a non-empty element is popped.</p>
</td>
</tr>
<tr id="row720751025216"><td class="cellrowborder" valign="top" width="27.589999999999996%" headers="mcps1.2.3.1.1 "><p id="p82075109523"><a name="p82075109523"></a><a name="p82075109523"></a>BRPOPLPUSH</p>
</td>
<td class="cellrowborder" valign="top" width="72.41%" headers="mcps1.2.3.1.2 "><p id="p920716106520"><a name="p920716106520"></a><a name="p920716106520"></a>The blocking variant of <strong id="b6668135213211"><a name="b6668135213211"></a><a name="b6668135213211"></a>RPOPLPUSH</strong>. When <em id="i425821934517"><a name="i425821934517"></a><a name="i425821934517"></a>source</em> contains elements, this command behaves exactly like <strong id="b6730205716323"><a name="b6730205716323"></a><a name="b6730205716323"></a>RPOPLPUSH</strong>.</p>
</td>
</tr>
</tbody>
</table>

## Restricted Redis Commands<a name="section552371784313"></a>

Some Redis commands are supported by Proxy Cluster DCS instances for multi-key operations in the same slot. For details, see  [Table 4](#table7589193113396).

**Table  4**  Redis commands restricted in Proxy Cluster DCS instances.

<a name="table7589193113396"></a>
<table><thead align="left"><tr id="row17608931153912"><th class="cellrowborder" valign="top" width="23%" id="mcps1.2.3.1.1"><p id="p861118318394"><a name="p861118318394"></a><a name="p861118318394"></a>Category</p>
</th>
<th class="cellrowborder" valign="top" width="77%" id="mcps1.2.3.1.2"><p id="p8613631123915"><a name="p8613631123915"></a><a name="p8613631123915"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row19615103153914"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p106175313396"><a name="p106175313396"></a><a name="p106175313396"></a><strong id="b146761846134318"><a name="b146761846134318"></a><a name="b146761846134318"></a>Set</strong></p>
</td>
</tr>
<tr id="row17106110145518"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p19106150185520"><a name="p19106150185520"></a><a name="p19106150185520"></a>SINTER</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p3106100135510"><a name="p3106100135510"></a><a name="p3106100135510"></a>Returns the members of the set resulting from the intersection of all the given sets.</p>
</td>
</tr>
<tr id="row73718155114"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p114032111112"><a name="p114032111112"></a><a name="p114032111112"></a>SINTERSTORE</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p9142182113117"><a name="p9142182113117"></a><a name="p9142182113117"></a>Equal to <strong id="b19978134242410"><a name="b19978134242410"></a><a name="b19978134242410"></a>SINTER</strong>, but instead of returning the result set, it is stored in <em id="i19101154912444"><a name="i19101154912444"></a><a name="i19101154912444"></a>destination</em>.</p>
</td>
</tr>
<tr id="row171510522410"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1948711618517"><a name="p1948711618517"></a><a name="p1948711618517"></a>SUNION</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1491146259"><a name="p1491146259"></a><a name="p1491146259"></a>Returns the members of the set resulting from the union of all the given sets.</p>
</td>
</tr>
<tr id="row12312808552"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1431280205512"><a name="p1431280205512"></a><a name="p1431280205512"></a>SUNIONSTORE</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p103125020559"><a name="p103125020559"></a><a name="p103125020559"></a>Equal to <strong id="b0807182119254"><a name="b0807182119254"></a><a name="b0807182119254"></a>SUNION</strong>, but instead of returning the result set, it is stored in <em id="i2081253134412"><a name="i2081253134412"></a><a name="i2081253134412"></a>destination</em>.</p>
</td>
</tr>
<tr id="row2380115517419"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p10822802518"><a name="p10822802518"></a><a name="p10822802518"></a>SDIFF</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p68251301752"><a name="p68251301752"></a><a name="p68251301752"></a>Returns the members of the set resulting from the difference between the first set and all the successive sets.</p>
</td>
</tr>
<tr id="row116991015517"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1169915035516"><a name="p1169915035516"></a><a name="p1169915035516"></a>SDIFFSTORE</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p369980185510"><a name="p369980185510"></a><a name="p369980185510"></a>Equal to <strong id="b13963164952518"><a name="b13963164952518"></a><a name="b13963164952518"></a>SDIFF</strong>, but instead of returning the result set, it is stored in <em id="i1950885754414"><a name="i1950885754414"></a><a name="i1950885754414"></a>destination</em>.</p>
</td>
</tr>
<tr id="row141351113558"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1013613113559"><a name="p1013613113559"></a><a name="p1013613113559"></a>SMOVE</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1913611145515"><a name="p1913611145515"></a><a name="p1913611145515"></a>Moves <strong id="b1557216852619"><a name="b1557216852619"></a><a name="b1557216852619"></a>member</strong> from the set at <strong id="b133530158269"><a name="b133530158269"></a><a name="b133530158269"></a>source</strong> to the set at <em id="i6398162104520"><a name="i6398162104520"></a><a name="i6398162104520"></a>destination</em>.</p>
</td>
</tr>
<tr id="row9622143120393"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p156255312391"><a name="p156255312391"></a><a name="p156255312391"></a><strong id="b83161220152314"><a name="b83161220152314"></a><a name="b83161220152314"></a>Sorted Set</strong></p>
</td>
</tr>
<tr id="row69805945518"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1798069175510"><a name="p1798069175510"></a><a name="p1798069175510"></a>ZUNIONSTORE</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p898017916552"><a name="p898017916552"></a><a name="p898017916552"></a>Computes the union of <em id="i139199144519"><a name="i139199144519"></a><a name="i139199144519"></a>numkeys</em> sorted sets given by the specified keys.</p>
</td>
</tr>
<tr id="row0148510195511"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1714817109555"><a name="p1714817109555"></a><a name="p1714817109555"></a>ZINTERSTORE</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p514891019556"><a name="p514891019556"></a><a name="p514891019556"></a>Computes the intersection of <em id="i183041313164518"><a name="i183041313164518"></a><a name="i183041313164518"></a>numkeys</em> sorted sets given by the specified keys.</p>
</td>
</tr>
<tr id="row562993110397"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p163019319397"><a name="p163019319397"></a><a name="p163019319397"></a><strong id="b86751046195717"><a name="b86751046195717"></a><a name="b86751046195717"></a>HyperLogLog</strong></p>
</td>
</tr>
<tr id="row53222122556"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p103221712195513"><a name="p103221712195513"></a><a name="p103221712195513"></a>PFCOUNT</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p832261217556"><a name="p832261217556"></a><a name="p832261217556"></a>Returns the approximated cardinality computed by the HyperLogLog data structure stored at the specified variable.</p>
</td>
</tr>
<tr id="row13494131216558"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p9494312185518"><a name="p9494312185518"></a><a name="p9494312185518"></a>PFMERGE</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p10494012175517"><a name="p10494012175517"></a><a name="p10494012175517"></a>Merges multiple HyperLogLog values into a unique value.</p>
</td>
</tr>
<tr id="row56371731203918"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p14638531113917"><a name="p14638531113917"></a><a name="p14638531113917"></a><strong id="b825815381589"><a name="b825815381589"></a><a name="b825815381589"></a>Key</strong></p>
</td>
</tr>
<tr id="row546318184557"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p1646551816552"><a name="p1646551816552"></a><a name="p1646551816552"></a>RENAME</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p174484012185"><a name="p174484012185"></a><a name="p174484012185"></a>Renames <em id="i13476924194518"><a name="i13476924194518"></a><a name="i13476924194518"></a>key</em> to <em id="i10961229184518"><a name="i10961229184518"></a><a name="i10961229184518"></a>newkey</em>.</p>
</td>
</tr>
<tr id="row15638318135519"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p463891815516"><a name="p463891815516"></a><a name="p463891815516"></a>RENAMENX</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p76381518115516"><a name="p76381518115516"></a><a name="p76381518115516"></a>Renames <em id="i894518509451"><a name="i894518509451"></a><a name="i894518509451"></a>key</em> to <em id="i5992034104516"><a name="i5992034104516"></a><a name="i5992034104516"></a>newkey</em> if <em id="i1678954010457"><a name="i1678954010457"></a><a name="i1678954010457"></a>newkey</em> does not yet exist.</p>
</td>
</tr>
<tr id="row582015183557"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p12822161814557"><a name="p12822161814557"></a><a name="p12822161814557"></a>BITOP</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p5822518125516"><a name="p5822518125516"></a><a name="p5822518125516"></a>Performs a bitwise operation between multiple keys (containing string values) and stores the result in the destination key.</p>
</td>
</tr>
<tr id="row152120198553"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p221141914551"><a name="p221141914551"></a><a name="p221141914551"></a>RPOPLPUSH</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p1921171914557"><a name="p1921171914557"></a><a name="p1921171914557"></a>Returns and removes the last element (tail) of the list stored at source, and pushes the element at the first element (head) of the list stored at <em id="i1486713261431"><a name="i1486713261431"></a><a name="i1486713261431"></a>destination</em>.</p>
</td>
</tr>
<tr id="row15642731143912"><td class="cellrowborder" colspan="2" valign="top" headers="mcps1.2.3.1.1 mcps1.2.3.1.2 "><p id="p12644153110392"><a name="p12644153110392"></a><a name="p12644153110392"></a><strong id="b131401432083"><a name="b131401432083"></a><a name="b131401432083"></a>String</strong></p>
</td>
</tr>
<tr id="row09952219550"><td class="cellrowborder" valign="top" width="23%" headers="mcps1.2.3.1.1 "><p id="p7995152113554"><a name="p7995152113554"></a><a name="p7995152113554"></a>MSETNX</p>
</td>
<td class="cellrowborder" valign="top" width="77%" headers="mcps1.2.3.1.2 "><p id="p13995152115516"><a name="p13995152115516"></a><a name="p13995152115516"></a>Sets the given keys to their respective values.</p>
</td>
</tr>
</tbody>
</table>

>![](public_sys-resources/icon-note.gif) **NOTE:** 
>While running commands that take a long time to run, such as  **FLUSHALL**, DCS instances may not respond to other commands and may change to the faulty state. After the command finishes executing, the instance will return to normal.

## Other Command Usage Restrictions<a name="section834293511127"></a>

**Key commands:**

In case of a large amount of cached data, running a  **Keys**  command may block the execution of other commands for a long time or occupy exceptionally large memory. Therefore, when running a  **Keys**  command, describe the exact pattern and do not use fuzzy  **keys \***.  **keys \***  can be used during commissioning or when the number of keys does not exceed 5 million. Otherwise, the service cannot run properly.

**Server commands:**

-   While running commands that take a long time to run, such as  **FLUSHALL**, DCS instances may not respond to other commands and change to the faulty state. After the command finishes executing, the instance will return to normal.
-   When the  **FLUSHDB**  or  **FLUSHALL**  command is run, execution of other service commands may be blocked for a long time in case of a large amount of cached data.

**EVAL and EVALSHA commands:**

-   When the  **EVAL**  or  **EVALSHA**  command is run, at least one key must be contained in the command parameter. Otherwise, the error message "ERR eval/evalsha numkeys must be bigger than zero in redis cluster mode" is displayed.
-   When the  **EVAL**  or  **EVALSHA**  command is run, a Proxy Cluster DCS Redis instance uses the first key to compute slots. Ensure that the keys to be operated in your code are in the same slot. For details, visit  [https://redis.io/commands](https://redis.io/commands).
-   For the  **EVAL**  command:
    -   You are advised to learn the Lua script features of Redis before running the  **EVAL**  command. For details, see  [https://redis.io/commands/eval](https://redis.io/commands/eval).
    -   The execution timeout time of a Lua script is 5 seconds. Time-consuming statements such as long-time sleep and large loop statements should be avoided.
    -   When calling a Lua script, do not use random functions to specify keys. Otherwise, the execution results are inconsistent on the master and standby nodes.


**Others:**

-   The time limit for executing a Redis command is 15 seconds. To prevent other services from failing, a master/replica switchover will be triggered after the command execution times out.
-   Proxy Cluster DCS Redis instances created before July 10, 2018 must be upgraded to support the following commands:

    SINTER, SDIFF, SUNION, PFCOUNT, PFMERGE, SINTERSTORE, SUNIONSTORE, SDIFFSTORE, SMOVE, ZUNIONSTORE, ZINTERSTORE, EVAL, EVALSHA, BITOP, RENAME, RENAMENX, RPOPLPUSH, MSETNX, SCRIPT LOAD, SCRIPT KILL, SCRIPT EXISTS, SCRIPT FLUSH.


