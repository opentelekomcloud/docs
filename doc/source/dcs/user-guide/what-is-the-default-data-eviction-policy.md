# What Is the Default Data Eviction Policy?<a name="EN-US_TOPIC_0237964744"></a>

Data is evicted from the cache based on the user-defined space limit in order to make space for new data.

By default, data is not evicted from DCS instances. In the current version of DCS, you can select an eviction policy.

When maxmemory is reached, you can select one of the following six eviction policies:

-   noeviction

    When the memory limit is reached, DCS instances return errors to clients and no longer process write requests or other requests that could result in more memory being used. However, DEL and a few more exception requests can continue to be processed.

-   allkeys-lru

    DCS instances try to evict the least recently used keys first, in order to make space for new data.

-   volatile-lru

    DCS instances try to evict the least recently used keys with an expire set first, in order to make space for new data.

-   allkeys-random

    DCS instances evict random keys in order to make space for new data.

-   volatile-random

    DCS instances evict random keys with an expire set, in order to make space for new data.

-   volatile-ttl

    DCS instances evict keys with an expire set, and try to evict keys with a shorter time to live \(TTL\) first, in order to make space for new data.


>![](/images/icon-note.gif) **NOTE:**   
>If the configured policy is volatile-lru, volatile-random, or volatile-ttl, and no keys match the configured policy, the eviction behavior will match noeviction.  

