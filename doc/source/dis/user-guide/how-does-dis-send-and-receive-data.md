# How Does DIS Send and Receive Data?<a name="dis_faq_0003"></a>

1.  Create a DIS stream, and obtain your Access Key ID/Secret Access Key \(AK/SK\) from the Identity and Access Management \(IAM\) service.
2.  Obtain and decompress the DIS SDK package.

    After obtaining the software package, verify its integrity. For details about the verification method, see  [How Do I Check Software Package Integrity?](how-do-i-check-software-package-integrity.md).

    -   To obtain the DIS SDK software package, visit the following website:

        [https://dis.obs.eu-de.otc.t-systems.com/dis/download/dis-sdk-1.2.3.zip](https://dis.obs.eu-de.otc.t-systems.com/dis/download/dis-sdk-1.2.3.zip)

    -   To obtain the integrity check file of the DIS SDK software package, visit the following website:

        [https://dis.obs.eu-de.otctest.t-systems.com/dis/download/dis-sdk-1.2.3.zip.sha256sum](https://dis.obs.eu-de.otctest.t-systems.com/dis/download/dis-sdk-1.2.3.zip.sha256sum)

3.  Create a project and configure the user AK/SK, endpoint, project ID, region, stream name, and partition quantity.
4.  After the configuration is completed, run the application to send data.
5.  Create a project and configure the user AK/SK, endpoint, project, region, stream name, partition ID, and startingSequenceNumber.
6.  After the configuration is completed, run the application to receive data.

