# Key Operations on DMS<a name="en-us_topic_0100291679"></a>

Distributed Message Service \(DMS\) is a Kafka-based and high-performance message service that allows multi-user and concurrent access and message queue isolation.

With CTS, you can record operations associated with DMS for future query, audit, and backtrack operations.

**Table  1**  DMS operations that can be recorded by CTS

<a name="table1424737164115"></a>
<table><thead align="left"><tr id="r3407c96968734554ac80493094ff8fcb"><th class="cellrowborder" valign="top" width="29.967003299670036%" id="mcps1.2.4.1.1"><p id="a2128691c982041bbab712edeab28472e"><a name="a2128691c982041bbab712edeab28472e"></a><a name="a2128691c982041bbab712edeab28472e"></a>Operation</p>
</th>
<th class="cellrowborder" valign="top" width="27.947205279472055%" id="mcps1.2.4.1.2"><p id="a8507175035cd4c348416b4bf9e104487"><a name="a8507175035cd4c348416b4bf9e104487"></a><a name="a8507175035cd4c348416b4bf9e104487"></a>Resource Type</p>
</th>
<th class="cellrowborder" valign="top" width="42.085791420857916%" id="mcps1.2.4.1.3"><p id="ae7fdbf6681124e5e967710e5cb5d3738"><a name="ae7fdbf6681124e5e967710e5cb5d3738"></a><a name="ae7fdbf6681124e5e967710e5cb5d3738"></a>Trace Name</p>
</th>
</tr>
</thead>
<tbody><tr id="rb52ca6cd73df4999ad733d90fd960a58"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a0fb9c6f21ff244bd95d89e877ed4abe6"><a name="a0fb9c6f21ff244bd95d89e877ed4abe6"></a><a name="a0fb9c6f21ff244bd95d89e877ed4abe6"></a>Creating a queue</p>
</td>
<td class="cellrowborder" valign="top" width="27.947205279472055%" headers="mcps1.2.4.1.2 "><p id="a7fab21bd7b7c425a86c000e201168749"><a name="a7fab21bd7b7c425a86c000e201168749"></a><a name="a7fab21bd7b7c425a86c000e201168749"></a>queue</p>
</td>
<td class="cellrowborder" valign="top" width="42.085791420857916%" headers="mcps1.2.4.1.3 "><p id="a5e508ae8fcdd43d39a9f8c7233e4664b"><a name="a5e508ae8fcdd43d39a9f8c7233e4664b"></a><a name="a5e508ae8fcdd43d39a9f8c7233e4664b"></a>createQueue</p>
</td>
</tr>
<tr id="r7032089fa24142639ccb3ca3577fe843"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a35a3eed5329d429b92bc0a561c74fecc"><a name="a35a3eed5329d429b92bc0a561c74fecc"></a><a name="a35a3eed5329d429b92bc0a561c74fecc"></a>Deleting a queue</p>
</td>
<td class="cellrowborder" valign="top" width="27.947205279472055%" headers="mcps1.2.4.1.2 "><p id="ada18a4863beb415d95e56c3eadae407d"><a name="ada18a4863beb415d95e56c3eadae407d"></a><a name="ada18a4863beb415d95e56c3eadae407d"></a>queue</p>
</td>
<td class="cellrowborder" valign="top" width="42.085791420857916%" headers="mcps1.2.4.1.3 "><p id="ace714d7a41cd46c1bd22a2c504a4f906"><a name="ace714d7a41cd46c1bd22a2c504a4f906"></a><a name="ace714d7a41cd46c1bd22a2c504a4f906"></a>deleteQueue</p>
</td>
</tr>
<tr id="r1b0a865f2dd0460789bfe5b906ce9f17"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a4133f141133a430fa91fbdc27628e7de"><a name="a4133f141133a430fa91fbdc27628e7de"></a><a name="a4133f141133a430fa91fbdc27628e7de"></a>Creating a consumer group</p>
</td>
<td class="cellrowborder" valign="top" width="27.947205279472055%" headers="mcps1.2.4.1.2 "><p id="a23025d4b532d471e8c81b35ecdea97d2"><a name="a23025d4b532d471e8c81b35ecdea97d2"></a><a name="a23025d4b532d471e8c81b35ecdea97d2"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="42.085791420857916%" headers="mcps1.2.4.1.3 "><p id="a9df92b7a7ff74b44bac6790779a877f0"><a name="a9df92b7a7ff74b44bac6790779a877f0"></a><a name="a9df92b7a7ff74b44bac6790779a877f0"></a>createGroup</p>
</td>
</tr>
<tr id="r4cf2d675496c419fb6e8b0570b2b5589"><td class="cellrowborder" valign="top" width="29.967003299670036%" headers="mcps1.2.4.1.1 "><p id="a7109c58263d844de8aedcecf643a20b2"><a name="a7109c58263d844de8aedcecf643a20b2"></a><a name="a7109c58263d844de8aedcecf643a20b2"></a>Deleting a consumer group</p>
</td>
<td class="cellrowborder" valign="top" width="27.947205279472055%" headers="mcps1.2.4.1.2 "><p id="a473d2a9a5e8f4ffc8c0fbb929a1fd0cd"><a name="a473d2a9a5e8f4ffc8c0fbb929a1fd0cd"></a><a name="a473d2a9a5e8f4ffc8c0fbb929a1fd0cd"></a>group</p>
</td>
<td class="cellrowborder" valign="top" width="42.085791420857916%" headers="mcps1.2.4.1.3 "><p id="a2bdcfa980065417fb808275515ecc40e"><a name="a2bdcfa980065417fb808275515ecc40e"></a><a name="a2bdcfa980065417fb808275515ecc40e"></a>deleteGroup</p>
</td>
</tr>
</tbody>
</table>

