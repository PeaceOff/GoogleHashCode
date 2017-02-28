"""5 videos, 2 endpoints, 4 request descriptions, 3 caches 100MB each.
Videos 0, 1, 2, 3, 4 have sizes 50MB, 50MB, 80MB, 30MB, 110MB.
Endpoint 0 has 1000ms datacenter latency and is connected to 3 caches:
The latency (of endpoint 0) to cache 0 is 100ms.
The latency (of endpoint 0) to cache 2 is 200ms.
The latency (of endpoint 0) to cache 1 is 200ms.
Endpoint 1 has 500ms datacenter latency and is not connected to a cache.
1500 requests for video 3 coming from endpoint 0.
1000 requests for video 0 coming from endpoint 1.
500 requests for video 4 coming from endpoint 0.
1000 requests for video 1 coming from endpoint 0."""

class Cache():
    size = 0

    def __init__(self):
        self.endPoints = []
        self.videosRequests = [0] * Videos.totalVideos
        self.sizeUsed = 0
        self.containedVideos = []

    def addEndpoint(self, add):
        self.endPoints.append(add)

    def bestFirst(self):
        if self.sizeUsed == self.size:
            return

        for e in self.endPoints:
            for r in e.requests:
                video_id = Requests.videos[r]
                numver_r = Requests.number[r]
                if(e.dontNeed[Requests.videos[numver_r]] == 1):
                    continue
                self.videosRequests[video_id] += numver_r
        ordered = sorted(range(len(self.videosRequests)), key= lambda k : self.videosRequests[k])

        for i in range(0, len(ordered)):
            index = ordered[-i - 1]
            print ("asdasdasd",index)
            video_Size = Videos.sizes[index]
            size = video_Size + self.sizeUsed
            if index in self.containedVideos:
                continue
            if size <= self.size:
                self.containedVideos.append(index)
                self.sizeUsed = size
                for e in self.endPoints:
                    e.dontNeed[index] = 1
            else:
                break

    def __str__(self):
        ret = ""
        for c in self.containedVideos:
            ret += "{0} ".format(c)
        return ret


class Videos():
    video_id = 0
    sizes = []
    totalVideos = 0
    @staticmethod
    def add_video(size):
        Videos.sizes.append(size)
        Videos.video_id += 1


class Endpoint():
    idCounter=0

    def __init__(self, dc_latency, cache_server_ids, cache_server_lats):
        self.dc_latency = dc_latency
        self.top_letency = dc_latency
        self.cache_servers_id = cache_server_ids
        self.cache_servers_lats = cache_server_lats
        self.idCounter += 1
        self.endpoint_id = self.idCounter
        self.requests = []
        self.dontNeed = [0] * Videos.totalVideos
        self.ordered = []
        self.index = 0
    def addRequest(self, id):
        self.requests.append(id)

    def getBestCacheLatency(self):
        if len(self.ordered) == 0:
            self.ordered = sorted(range(len(self.cache_servers_lats)), key= lambda k : self.cache_servers_lats[k])


        if(self.index + 1 > len(self.cache_servers_id)):
            return -1

        bestId = self.cache_servers_id[self.ordered[self.index]]
        self.index+=1
        return bestId



class Requests():
    req_id = 0
    videos = []
    endpoints = []
    number = []

    @staticmethod
    def addReq(video_id, endpoint_id, n_req):
        Requests.videos.append(video_id)
        Requests.endpoints.append(endpoint_id)
        Requests.number.append(n_req)
        Requests.req_id += 1

    @staticmethod
    def giveAllRequestes(eps):
        for i,e in enumerate(Requests.endpoints):
            endpoint = eps[e]
            endpoint.addRequest(i)



class CacheServer():
    max_capacity = 0
    c_capacity = 0

    def has_space_for(self, c):
        return self.max_capacity <= self.c_capacity + c

    def __init__(self, id):
        self.id = id

g_endpoints = []
g_caches = []
g_videos=[]

file_name_a = "me_at_the_zoo"

def readFile():

    with open(file_name_a + ".in") as f:
        videosN,endpointsN,requestN,descriptionN,cacheN = [int(x) for x in next(f).split()]  # read first line
        Videos.totalVideos = videosN

        Cache.size = cacheN
        number_caches = 0
        for x in next(f).split():
            g_videos.append(int(x))
            Videos.add_video(int(x))

        for x in range(0, endpointsN):

            line = next(f).split()
            latency = int(line[0])
            cacheNumber = int(line[1])
            caches_latency = []
            caches_ids = []

            print latency
            print cacheNumber

            for cache in range(0,cacheNumber):
                cacheDesc = next(f).split()
                cacheId = int(cacheDesc[0])
                if(cacheId > number_caches):
                    number_caches = cacheId

                cacheLatency = int(cacheDesc[1])
                caches_ids.append(cacheId)
                caches_latency.append(cacheLatency)
                print  ("id" ,cacheId)
                print ("cacheid", cache)
                print  cacheLatency

            g_endpoints.append(Endpoint(latency, caches_ids, caches_latency))

        for nCaches in range(0, number_caches):
            g_caches.append(Cache())

        for requestN in range(0,requestN):
            requestDesc = next(f).split()
            print requestDesc
            videoId = int(requestDesc[0])
            endpointId = int(requestDesc[1])
            requestNumber = int(requestDesc[2])
            Requests.addReq(videoId, endpointId, requestNumber)

        Requests.giveAllRequestes(g_endpoints)


def writeToFile():
    cacheN = 0
    cacheIds = []
    for i,c in enumerate(g_caches):
        if c.sizeUsed > 0:
            cacheN +=1
            cacheIds.append(i)

    with open(file_name_a+".out","w") as f:
        f.write("{0}\n".format(cacheN))
        for id in cacheIds:
            f.write("{0} ".format(id))
            f.write(g_caches[id].__str__())
            f.write("\n")


def populate():
    for e in g_endpoints:
        bestCache = e.getBestCacheLatency()-1
        print ("asdasd", bestCache, "L", len(g_caches))
        if(bestCache > -1):
            g_caches[bestCache].addEndpoint(e)

    for c in g_caches:
        c.bestFirst()




readFile()
for i in range(0,5):
    populate()

writeToFile()