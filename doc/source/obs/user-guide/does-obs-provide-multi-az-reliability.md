# Does OBS Provide Multi-AZ Reliability?<a name="obs_faq_0141"></a>

Yes. OBS buckets \(version 3.0 and later\) are Multi-AZ reliable. They can keep resource accessible in terms of force majeure such as natural disasters when an AZ is unavailable.

For buckets of version 3.0 and later, data is automatically stored across AZs to achieve data redundancy in a specific region. However, buckets of versions earlier than 3.0 do not support Multi-AZ reliability. If you want to upgrade a bucket to version 3.0 for higher reliability, please contact the customer service.

You can check the bucket version using either of the following methods:

1.  View the bucket version on OBS Console.

    You can view your bucket version in the basic information area on the bucket's  **Overview**  page. For details, see  [Viewing Basic Information of a Bucket](viewing-basic-information-of-a-bucket-(console).md). For  **Bucket Version**,  **3.0**  indicates the latest version, and  **--**  indicates earlier versions.

2.  Call the HEAD Bucket API to check the bucket version.

    Call the  [HEAD Bucket](https://docs.otc.t-systems.com/api_obs/obs/en-us_topic_0125560467.html)  API. If the response message carries the  **x-obs-version: 3.0**  header, the bucket version is 3.0. If the response message does not carry this header or the header value is not 3.0, the bucket is of an earlier version.


