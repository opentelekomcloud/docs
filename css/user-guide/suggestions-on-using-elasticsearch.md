# Suggestions on Using Elasticsearch<a name="css_01_0032"></a>

Elasticsearch is an open-source search engine. This section provides some experience and suggestions on using Elasticsearch for you to better use CSS.

## Improving Indexing Efficiency<a name="section53922812102832"></a>

-   Sending data to Elasticsearch through multiple processes or threads

    A single thread that sends bulk requests is unlikely to max out the indexing capability of a cluster. To maximize utilization of cluster resources, send data through multiple threads or processes, which helps improve data processing efficiency.

    By testing, you can figure out the optimal number of threads for the bulk requests of the same size. The number of threads can be progressively increased until either the load or CPU is saturated in the cluster. You are advised to use the  **nodes stats**  API to view the CPU and load status of a node. You can learn details by viewing the  **os.cpu.percent**,  **os.cpu.load\_average.1m**,  **os.cpu.load\_average.5m**, and  **os.cpu.load\_average.15m**  parameter settings. For details about how to use the  **nodes stats**  API and parameter descriptions, see  [https://www.elastic.co/guide/en/elasticsearch/reference/6.2/cluster-nodes-stats.html\#os-stats](https://www.elastic.co/guide/en/elasticsearch/reference/6.2/cluster-nodes-stats.html#os-stats).

    For example, check whether the load or CPU is saturated if two threads are used during execution of bulk requests. If not saturated, increase threads. If the load or CPU is saturated when the number of threads reaches  _N_, you are advised to use  _N_  threads \(the optimal number according to your testing\) to execute bulk requests to improve indexing efficiency.

-   Increasing the refresh interval

    By default, each shard is automatically refreshed once per second. However, the refresh frequency is not applicable to all scenarios. If you use Elasticsearch to index a great number of log files and want to increase the indexing speed instead of obtaining near-real-time search performance, you can reduce the refresh frequency of each index.

    ```
    PUT /my_logs
    {
      "settings": {
        "refresh_interval": "30s"
      }
    }
    ```

-   Disabling refresh and replicas for initial loads

    If you need to import a large amount of data at a time, it is recommended that you disable refresh and replicas by setting  **refresh\_interval**  to  **-1**  and  **number\_of\_replicas**  to  **0**. After data is imported, set  **refresh\_interval**  and  **number\_of\_replicas**  to the original values.


## Selecting an Appropriate Number of Shards and Replicas<a name="section5630987515348"></a>

During index data creation, you are advised to specify the number of shards and replicas. Otherwise, default settings \(five shards and one replica\) will be used.

The shard quantity is strongly relevant to the indexing speed. Too many or too few shards will lead to slow indexing. If too many shards are specified, numerous files will be opened during retrieval, slowing down the communication between servers. If only a few shards are specified, the index size of a single shard may be too large, also slowing down the indexing speed.

Specify the shard quantity based on the node quantity, disk quantity, and index size. It is recommended that the size of a single shard not exceed 30 GB. The shard size is calculated using the following formula: Size of a shard = Total amount of data/Shard quantity

```
PUT /my_index
{
  "settings": {
    "number_of_shards":   1,
    "number_of_replicas":  0
  }
}
```

## Storing Data in Different Indices<a name="section1581140613444"></a>

Elasticsearch relies on Lucene to index and store data and it suits dense data, which means that all documents have the same field.

-   Avoiding putting unrelated data in the same index

    Do not put documents that have different data structures into the same index. You can consider creating some smaller indices and use fewer shards to store the documents into the indices.

-   Avoiding putting different types in the same index

    It is good practice to put different types into an individual index. However, be aware Elasticsearch does not store documents based on type. Therefore, putting different types into one index will slow down indexing. If your documents do not have similar mappings, use different indices.

-   Avoiding field conflicts between different types in an index

    Elasticsearch does not allow two different types that have fields of the same name but different mappings.


## Creating Indices by Time Range<a name="section3608304314745"></a>

You are advised to create indices to store time-related data, such as log data, by time range, instead of storing all data in a super large index.

For example, you can store data in an index named by year such as logs\_2014 or by month such as logs\_2014-10. When the volume of data becomes very large, store data in an index named by day such as logs\_2014-10-24.

Creating indices by time range has the following advantages:

-   Specifying a suitable number of shards and replicas based on the current volume of data

    You can flexibly set the number of shards and replicas for each index created by time range so that there is no need to set a large shard at the beginning. After the cluster capacity is expanded, the time range can be set to adapt to the cluster scale.

-   Deleting old data by deleting old indices

    ```
    DELETE /logs_2014-09
    ```

-   Switching between indices using the alias mechanism

    The following example illustrates how to delete index  **logs\_2014-09**  from alias mechanism  **logs\_current**  and add index  **logs\_2014-10**.

    ```
    POST /_aliases
    {
      "actions": [
        { "add":    { "alias": "logs_current",  "index": "logs_2014-10" }},
        { "remove": { "alias": "logs_current",  "index": "logs_2014-09" }}
      ]
    }
    ```

-   Optimizing the indices that stop being updated, such as indices generated last week or month, to increase query efficiency

    Combine multiple segments in the  **logs\_2014-09-30**  index into a shard, improving the query efficiency.

    ```
    PUT /logs_2014-09-30/_settings
    { "number_of_replicas": 0 }
    
    POST /logs_2014-09-30/_forcemerge?max_num_segments=1
    
    PUT /logs_2014-09-30/_settings
    { "number_of_replicas": 1 }
    ```


## Optimizing Index Configurations<a name="section1425508814337"></a>

-   Distinguishing between texts and keywords

    In Elasticsearch, the  **string**  field is divided into two new data types: text used for full-text search and keyword used for keyword search.

    You are advised to configure exact-value fields without sub-words, such as tags or enumerated values, as the keyword type.

    ```
    PUT my_index1
    {
      "mappings": {
        "my_type": {
          "properties": {
            "tags": {
              "type":  "keyword"
            },
            "full_name": {
              "type":  "text"
            }
          }
        }
      }
    }
    ```

-   Aggregated statistics based on the text field

    Aggregated statistics based on the text field is not a common requirement. In Elasticsearch, aggregated statistics based on the text field needs to use fielddata \(disabled by default\). Enabling fielddata will consume significant memory.

    You are advised to conduct multifield mapping on the sub-word string to a text field for full-text search and a keyword field for aggregated statistics.

    ```
    PUT my_index2
    {
      "mappings": {
        "my_type": {
          "properties": {
            "full_name": {
              "type": "text",
              "fields": {
                "raw": { 
                  "type":  "keyword"
                }
              }
            }
          }
        }
      }
    }
    ```


## Using Index Templates<a name="section5914550314410"></a>

Elasticsearch allows you to use index templates to control settings and mappings of certain created indices, for example, controlling the shard quantity to 1 and disabling the \_all field. The index template can be used to control which settings can be applied to the created indices.

-   In the index template, you can use the template field to specify a wildcard.
-   In the event of multiple index templates, you can use order to specify the overwriting sequence. The greater the value, the higher the priority.

In the following example, the index matching  **logstash-\***  uses the  **my\_logs**  template, and the priority value of the  **my\_logs**  template is 1.

```
PUT /_template/my_logs 
{
  "template": "logstash-*", 
  "order":    1, 
  "settings": {
    "number_of_shards": 1 
  },
  "mappings": {
    "_default_": { 
      "_all": {
        "enabled": false
      }
    }
  },
  "aliases": {
    "last_3_months": {} 
  }
}
```

## Data Backup and Restoration<a name="section40063217144230"></a>

Elasticsearch replicas provide high availability during runtime, which ensures service continuity even when sporadic data loss occurs.

However, replicas do not provide protection against failures. In the case of a failure, you need a real backup for your cluster so that you have a complete copy to restore data.

To back up cluster data, you can create snapshots to save cluster data to OBS buckets. This backup process is "smart". You are advised to use your first snapshot to store a copy of your data. All subsequent snapshots can save the differences between the existing snapshots and the new data. As the number of snapshots increases, backups are added or deleted accordingly. This means that subsequent backups will be very fast since only a small volume of data needs to be transferred.

## Improving Query Efficiency by Filtering<a name="section2867565144451"></a>

Filters are important because they are fast. They do not calculate relevance \(avoiding the entire scoring phase\) and are easily cached.

Usually, when looking for an exact value, we do not want to score the query. We just want to include/exclude documents, so we will use a constant\_score query to execute the term query in a non-scoring mode and apply a uniform score of one.

```
GET /my_store/products/_search
{
    "query" : {
        "constant_score" : { 
            "filter" : {
                "term" : { 
                    "city" : "London"
                }
            }
        }
    }
}
```

## Retrieving a Large Amount of Data Through the Scroll API<a name="section49009950144620"></a>

In the scenario where a large amount of data is returned, the query-then-fetch process supports pagination with the  **from**  and  **size**  parameters, but within limits. Results are sorted on each shard before being returned. However, with big-enough from values, the sorting process can become very heavy, using vast amounts of CPU, memory, and bandwidth. For this reason, we strongly advise against deep paging.

To avoid deep pagination, we recommend that you use the scroll query to retrieve a large amount of data.

A scroll query is used to retrieve large numbers of documents from Elasticsearch efficiently, without the hindrance in system performance as with deep pagination. Scrolling allows us to do an initial search and to keep pulling batches of results from Elasticsearch until there are no more results left.

## Differences Between Query and Filter<a name="section1034545719364"></a>

Performance difference: In general, a filter will outperform a scoring query. And it will do so consistently.

When used in filtering context, the query is said to be a  **non-scoring**  or  **filtering**  query. That is, the query simply asks the question: Does this document match? The answer is always a simple, binary yes|no.

Typical filtering cases are listed as follows:

-   Is the created time in the range from 2013 to 2014?
-   Does the  **status**  field contain the term "published"?
-   Is the  **lat\_lon**  field within 10 km of a specified point?

When used in a querying context, the query becomes a "**scoring**" query. Similar to its non-scoring sibling, this determines if a document matches and how well the document matches. A typical use for a query is to find documents:

-   Matching the words "full text search"
-   Containing the word "run", but maybe also matching "runs", "running", "jog", or "sprint"
-   Containing the words "quick", "brown", and "fox" – the closer together they are, the more relevant the document
-   Tagged with lucene, search, or java – the more tags, the more relevant the document

## Checking Whether a Query Is Valid<a name="section519218536381"></a>

Queries can become quite complex and, especially when combined with different analyzers and field mappings, can become a bit difficult to follow. The  **validate-query**  API can be used to check whether a query is valid.

For example, on the Kibana Console page, run the following command to check whether the query is valid. In this example, the validate request tells you that the query is invalid.

```
GET /gb/tweet/_validate/query 
{   
 "query": {      
 "tweet" : {       
   "match" : "really powerful"     
  }    
} 
}
```

The response to the preceding validate request tells us that the query is invalid. To find out why it is invalid, add the explain parameter to the query string and execute the following command.

```
GET /gb/tweet/_validate/query?explain 
{
"query": {
   "tweet" : {
  "match" : "really powerful"
  }
  }
 }
```

According to the command output shown in the following, the type of query \(match\) is mixed up with the name of the field \(tweet\).

```
{
  "valid": false,
  "error": "org.elasticsearch.common.ParsingException: no [query] registered for [tweet]"
}
```

The following lists a valid query. You can use the validate request together with the explain parameter to check its validity.

```
GET /gb/tweet/_validate/query?explain 
{    
"query": {    
   "match" : {        
  "tweet" : "really powerful"     
  }  
  }
 }
```

Using the explain parameter has the added advantage of returning a human-readable description of the \(valid\) query, which can be useful for understanding exactly how your query has been interpreted by CSS.

