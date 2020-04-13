# SSE-KMS<a name="EN-US_TOPIC_0125560445"></a>

In SSE-KMS mode, OBS uses the keys provided by KMS for server-side encryption. When an object encrypted using SSE-KMS is added to a bucket in a region for the first time, OBS creates a default customer master key \(CMK\), which is used to encrypt and decrypt the keys provided by KMS. Only users with the tenant\_admin role can use SSE-KMS interfaces. The SSE-KMS mode does not support the keys created by customers. The bucket ACL and policy do not allow cross-tenant authorized access to objects encrypted using SSE-KMS. OBS does not support KMS with multiple projects.

[Table 1](#table3087586113454)  lists two headers that are added to support SSE-KMS in SSE-KMS mode.

**Table  1**  Headers needed in SSE-KMS mode

<a name="table3087586113454"></a>
<table><thead align="left"><tr id="row163412111385"><th class="cellrowborder" valign="top" width="26.26%" id="mcps1.2.3.1.1"><p id="p13571117387"><a name="p13571117387"></a><a name="p13571117387"></a>Header</p>
</th>
<th class="cellrowborder" valign="top" width="73.74000000000001%" id="mcps1.2.3.1.2"><p id="p1135131112382"><a name="p1135131112382"></a><a name="p1135131112382"></a>Description</p>
</th>
</tr>
</thead>
<tbody><tr id="row51205044113454"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.3.1.1 "><p id="p53967936113454"><a name="p53967936113454"></a><a name="p53967936113454"></a>x-amz-server-side-encryption</p>
</td>
<td class="cellrowborder" valign="top" width="73.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p9326663113454"><a name="p9326663113454"></a><a name="p9326663113454"></a>Indicates that SSE-KMS is used. Objects are encrypted using SSE-KMS.</p>
<p id="p19164125012547"><a name="p19164125012547"></a><a name="p19164125012547"></a>Example:</p>
<p id="p16831109113454"><a name="p16831109113454"></a><a name="p16831109113454"></a>x-amz-server-side-encryption:aws:kms</p>
</td>
</tr>
<tr id="row17262259113454"><td class="cellrowborder" valign="top" width="26.26%" headers="mcps1.2.3.1.1 "><p id="p56065772113454"><a name="p56065772113454"></a><a name="p56065772113454"></a>x-amz-server-side-encryption-aws-kms-key-id</p>
</td>
<td class="cellrowborder" valign="top" width="73.74000000000001%" headers="mcps1.2.3.1.2 "><p id="p45033689113454"><a name="p45033689113454"></a><a name="p45033689113454"></a>Indicates the master key ID of an encrypted object. This header is used in SSE-KMS mode. If the customer does not provide the master key, the default master key will be used.</p>
<p id="p84781716550"><a name="p84781716550"></a><a name="p84781716550"></a>Example:</p>
<p id="p2650023113454"><a name="p2650023113454"></a><a name="p2650023113454"></a>x-amz-server-side-encryption-aws-kms-key-id:arn:aws:kms:sichuan:domainiddomainiddomainiddoma0001:key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0</p>
<p id="p18707114515461"><a name="p18707114515461"></a><a name="p18707114515461"></a>Note:</p>
<p id="p12707104511464"><a name="p12707104511464"></a><a name="p12707104511464"></a>sichuan: indicates the region name. Set the value based on site requirements.</p>
<p id="p8707194594614"><a name="p8707194594614"></a><a name="p8707194594614"></a>domainiddomainiddomainiddoma0001: indicates the tenant ID. Set the value based on site requirements.</p>
<p id="p1270819459463"><a name="p1270819459463"></a><a name="p1270819459463"></a>key/4f1cd4de-ab64-4807-920a-47fc42e7f0d0: indicates the key ID. Set the value based on site requirements.</p>
</td>
</tr>
</tbody>
</table>

**Table  2**  Interfaces to which the newly added headers apply

<a name="table13325310113454"></a>
<table><thead align="left"><tr id="row61931835113454"><th class="cellrowborder" valign="top" width="100%" id="mcps1.2.2.1.1"><p id="p50422727113454"><a name="p50422727113454"></a><a name="p50422727113454"></a>Interface</p>
</th>
</tr>
</thead>
<tbody><tr id="row57709047113454"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p43921203113454"><a name="p43921203113454"></a><a name="p43921203113454"></a>PUT Object</p>
</td>
</tr>
<tr id="row59746514113454"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p7629452113454"><a name="p7629452113454"></a><a name="p7629452113454"></a>POST Object</p>
</td>
</tr>
<tr id="row1556210113454"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p58944196113454"><a name="p58944196113454"></a><a name="p58944196113454"></a>PUT Object - Copy (the newly added headers apply to target objects)</p>
</td>
</tr>
<tr id="row60735723113454"><td class="cellrowborder" valign="top" width="100%" headers="mcps1.2.2.1.1 "><p id="p20646494113454"><a name="p20646494113454"></a><a name="p20646494113454"></a>Initiate Multipart Upload</p>
</td>
</tr>
</tbody>
</table>

OBS supports bucket policies. If you want to restrict server-side encryption for all objects stored in a bucket, you can use bucket policies. For example, if an object upload request does not contain  **x-amz-server-side-encryption:"aws:kms"**, the header for requesting server-side encryption \(SSE-KMS\), the following bucket policy rejects the upload request:

\{

"Version":"2008-10-17",

"Id":"PutObjPolicy",

"Statement":\[\{

"Sid":"DenyUnEncryptedObjectUploads",

"Effect":"Deny",

"Principal":"\*",

"Action":"s3:PutObject",

"Resource":"arn:aws:s3:::YourBucket/\*",

"Condition":\{

"StringNotEquals":\{

"s3:x-amz-server-side-encryption":"aws:kms"

\}

\}

\}

\]

\}

