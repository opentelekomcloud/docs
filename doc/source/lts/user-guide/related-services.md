# Related Services<a name="lts_01_0005"></a>

## VPC<a name="section1064613521526"></a>

LTS can store and analyze logs for Virtual Private Clouds \(VPCs\). After a VPC is associated with the log group and log topics created on LTS, logs about the Network Interface Cards \(NICs\) are uploaded to LTS for preview, search, and storage.

## OBS<a name="section56761229165019"></a>

Object Storage Service \(OBS\) provides object-based massive storage. LTS can transfer logs to OBS buckets for long-term storage.

## IAM<a name="section178961375117"></a>

Identity and Access Management \(IAM\) provides an identity authentication and permission management function. To manage logs, LTS obtains the tenant permissions by invoking the IAM APIs.

## CTS<a name="section1199510402815"></a>

With LTS, you can search for data traces of Cloud Trace Service \(CTS\). If you enable  **Trace Analysis**  on the  **Configure Tracker**  page of the CTS service, data traces recorded by CTS will be synchronized to the LTS server. Then, you can search for the data traces generated in the last seven days using customized filters.

