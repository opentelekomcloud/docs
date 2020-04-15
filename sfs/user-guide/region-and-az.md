# Region and AZ<a name="sfs_01_0002"></a>

## Concept<a name="en-us_topic_0184026189_section388255972712"></a>

A region and availability zone \(AZ\) identify the location of a data center. You can create resources in a specific region and AZ.

-   A region is a physical data center, which is completely isolated to improve fault tolerance and stability. The region that is selected during resource creation cannot be changed after the resource is created.
-   An AZ is a physical location where resources use independent power supplies and networks. A region contains one or more AZs that are physically isolated but interconnected through internal networks. Because AZs are isolated from each other, any fault that occurs in an AZ will not affect other AZs.

[Figure 1](#en-us_topic_0184026189_fig8747114281212)  shows the relationship between regions and AZs.

**Figure  1**  Regions and AZs<a name="en-us_topic_0184026189_fig8747114281212"></a>  
![](figures/regions-and-azs.png "regions-and-azs")

## Selecting a Region<a name="en-us_topic_0184026189_section67281149192216"></a>

Select a region closest to your target users for low network latency and quick access.

## Selecting an AZ<a name="en-us_topic_0184026189_section193971112578"></a>

When deploying resources, consider your applications' requirements on disaster recovery \(DR\) and network latency.

-   For high DR capability, deploy resources in different AZs within the same region.
-   For low network latency, deploy resources in the same AZ.

## Regions and Endpoints<a name="en-us_topic_0184026189_section1110135820407"></a>

Before you use an API to call resources, specify its region and endpoint. For more details, see  [Regions and Endpoints](https://docs.otc.t-systems.com/en-us/endpoint/index.html).

