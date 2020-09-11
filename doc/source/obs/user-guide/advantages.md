# Advantages<a name="obs_03_0201"></a>

## Comparison Between OBS and On-Premises Storage Servers<a name="section1071910168165"></a>

In this information era, it becomes increasingly difficult for conventional on-premises storage servers to deal with enterprises' explosive data growth.  [Table 1](#table3469342151617)  details a comprehensive comparison between OBS and on-premises storage servers.

**Table  1**  Comparison between OBS and on-premises storage servers

<a name="table3469342151617"></a>
<table><thead align="left"><tr id="row446954214169"><th class="cellrowborder" valign="top" width="17.261726172617262%" id="mcps1.2.4.1.1"><p id="p15470142141617"><a name="p15470142141617"></a><a name="p15470142141617"></a>Item</p>
</th>
<th class="cellrowborder" valign="top" width="39.5039503950395%" id="mcps1.2.4.1.2"><p id="p347084271610"><a name="p347084271610"></a><a name="p347084271610"></a>OBS</p>
</th>
<th class="cellrowborder" valign="top" width="43.23432343234324%" id="mcps1.2.4.1.3"><p id="p647044218162"><a name="p647044218162"></a><a name="p647044218162"></a>On-Premises Storage Server</p>
</th>
</tr>
</thead>
<tbody><tr id="row15470114291617"><td class="cellrowborder" valign="top" width="17.261726172617262%" headers="mcps1.2.4.1.1 "><p id="p194708426169"><a name="p194708426169"></a><a name="p194708426169"></a>Storage capacity</p>
</td>
<td class="cellrowborder" valign="top" width="39.5039503950395%" headers="mcps1.2.4.1.2 "><p id="p1247074217164"><a name="p1247074217164"></a><a name="p1247074217164"></a>OBS provides storage capacity for massive amounts of data. All services and storage nodes are deployed in distributed clusters. You can expand a node or cluster separately, and the storage capacity will never be insufficient.</p>
</td>
<td class="cellrowborder" valign="top" width="43.23432343234324%" headers="mcps1.2.4.1.3 "><p id="p447064213163"><a name="p447064213163"></a><a name="p447064213163"></a>Confined storage space due to limited capacity of hardware devices. You need to purchase extra disks and perform manual expansion. The storage capacity is eventually a limitation.</p>
</td>
</tr>
<tr id="row174707429165"><td class="cellrowborder" valign="top" width="17.261726172617262%" headers="mcps1.2.4.1.1 "><p id="p15470142131611"><a name="p15470142131611"></a><a name="p15470142131611"></a>Security</p>
</td>
<td class="cellrowborder" valign="top" width="39.5039503950395%" headers="mcps1.2.4.1.2 "><p id="p4470194211163"><a name="p4470194211163"></a><a name="p4470194211163"></a>OBS uses the HTTPS/SSL protocol and supports encryption for data uploads. In addition, OBS uses access key IDs (AKs) and secret access keys (SKs) to authenticate user identities. It also leverages <span id="ph116357498592"><a name="ph116357498592"></a><a name="ph116357498592"></a>IAM policies</span>, bucket policies, access control lists (ACLs), and technologies such as uniform resource locator (URL) validation to ensure security for data transmission and access.</p>
</td>
<td class="cellrowborder" valign="top" width="43.23432343234324%" headers="mcps1.2.4.1.3 "><p id="p154702042141610"><a name="p154702042141610"></a><a name="p154702042141610"></a>Exposes the owner and users to security risks such as cyber attacks, technological vulnerabilities, and accidental operations.</p>
</td>
</tr>
<tr id="row3470342131610"><td class="cellrowborder" valign="top" width="17.261726172617262%" headers="mcps1.2.4.1.1 "><p id="p347015420162"><a name="p347015420162"></a><a name="p347015420162"></a>Costs</p>
</td>
<td class="cellrowborder" valign="top" width="39.5039503950395%" headers="mcps1.2.4.1.2 "><p id="p194701442111612"><a name="p194701442111612"></a><a name="p194701442111612"></a>OBS is an out-of-the-box service, which requires zero cost for physical devices. It also provides O&amp;M services.</p>
</td>
<td class="cellrowborder" valign="top" width="43.23432343234324%" headers="mcps1.2.4.1.3 "><p id="p124702042111613"><a name="p124702042111613"></a><a name="p124702042111613"></a>Expensive hardware devices; long-term construction; difficulties in installation; high O&amp;M costs. All these disadvantages of on-premises storage servers can impede the growth of enterprises. In addition, you may incur expenditure for security assurance.</p>
</td>
</tr>
</tbody>
</table>

## OBS Advantages<a name="section156154701515"></a>

-   **Reliable data durability and service continuity**: OBS supports access for hundreds of millions of users.
-   **Multi-level protection and authorization management**: The multiple data protection mechanisms, including versioning, server-side encryption, URL validation, virtual private cloud \(VPC\)-based network isolation, access log audit, and fine-grained permission control, ensure persistent data security.
-   **Unlimited number of objects and high-level concurrency**: With intelligent scheduling and response, optimized data access paths, and technologies such as event notification, transmission acceleration, and big data vertical optimization, you can store hundreds of billions of objects in OBS, and still experience smooth concurrency of hundreds of billions of tasks, ultra-high bandwidth, and low latency.
-   **Easy to use and manage**: OBS provides standard REST APIs, SDKs that support multiple programming languages, and data migration tools, such as OBS Browser to help you quickly move your services to the cloud. You do not need to plan storage capacity beforehand or worry about storage capacity expansion or reduction, because storage resources are available for linear and nearly infinite expansion. 

