# 여기에 다 적자

## Port 뭐 열어야하느다

8080 8081 16686

## Installation Script

```bash
sudo apt-get update && sudo apt-get upgrade -y && sudo apt install containerd -y && sudo apt install docker.io -y && sudo systemctl enable --now docker
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose && docker-compose version
git clone https://github.com/delimitrou/DeathStarBench.git && cd DeathStarBench/socialNetwork/ && sudo docker-compose up -d
sudo apt install python3-pip && pip3 install aiohttp && sudo apt-get install libssl-dev && sudo apt-get install luarocks && sudo luarocks install luasocket && sudo apt-get install libz-dev
```

## aiohttp 해결하기

실행이 안되게 해볼까

## SSH

export AWS_DEFAULT_REGION=us-east-1 export AWS_ACCESS_KEY_ID=ASIASIPHEI4JLOYJONMH export
AWS_SECRET_ACCESS_KEY=mPiyqy+xrc4NOZpgGsdUwJk0QBtJBbAIGI6oaRHK export
AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjEF0aCXVzLWVhc3QtMSJGMEQCICw3W73gy+ggZ5DTJSTIc4/y4AHRb62gp5AM9m169XqrAiAM8FXCSa95aTG7AdY9exRuQR/qsmx4QV8qgU4ADoSDOCqgAgjF//////////8BEAAaDDE1NTY0MDQxNjAxOCIM7VxETiUUY0PsB0vCKvQBDw13/1EGbNLC1l0TB03U2Qdyh5CgwR7+wG9RGycoABkGUGzyihwm6azEPS9CUzi7VGyPyO0e5sPzTRs6mMtDTi71ljOGkshlnV+aWN1NJN93zKhiqsAaxB2tZDWRDtancT8PLXxWOJNfOVhmSMR5zgWzJ/kBbek76n4EDcathtwYT0ERroqmrX/ibSNzz2+M2LyzzOLGZITRXPZJ/tpRcskgi1Jpt2d4a9PaO4njtCZ5AwS1vx7bevDIFZ10O4ISVSQ+0itiXs69Az0u4j82hdnGW0AejT5Ohs0Tendm8+Hl1FHispeUCtRVnN4TtpE+uuvmxzD9kNOKBjqeAWXY/gnNq233JMHjAin79JxVzsk38lTVYHGTqkXI70xWeeD5DsXNINZO5xV7cwocFRU1ylUrIpzopZh4EC5cHO9AzScdC9xx8ZgbGqlOhYLzY+TRSJWDuap5E+R6VvoeTMv42jwjiJ9T0n/XihcG8FuONCCVZsWBAmWRqnEUun57SyHTABWC3dtIJXuDjT4vVYp+m2bEDt9UMMU6n8r2

# Installation 다시

apt list --upgradable sudo apt-get remove docker docker-engine docker.io containerd runc sudo apt-get update sudo
apt-get install apt-transport-https
sudo apt-get install ca-certificates
sudo apt-get install curl
sudo apt-get install gnupg sudo apt-get install lsb-release curl -fsSL https://download.docker.com/linux/ubuntu/gpg |
sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg echo \
"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null sudo apt-get update sudo apt-get
install docker-ce docker-ce-cli containerd.io apt-cache madison docker-ce sudo apt-get install docker-ce=5:20.10.8~3-0~
ubuntu-focal docker-ce-cli=5:20.10.8~3-0~ubuntu-focal containerd.io sudo usermod -aG docker $USER

sudo reboot

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o
/usr/local/bin/docker-compose sudo chmod +x /usr/local/bin/docker-compose

docker-compose --version

git clone https://github.com/delimitrou/DeathStarBench.git
cd DeathStarBench/socialNetwork/

docker-compose up -d

sudo apt install python3-pip pip3 install aiohttp
sudo apt-get install libssl-dev sudo apt-get install luarocks sudo apt-get install libz-dev sudo luarocks install
luasocket

python3 scripts/init_social_graph.py

좀있다 Sudo로 해보자

그리고 안되면 SiNan이 보낸걸로 둘다 해보자

1시간씩 하면 될듯

안되니까 그냥 해보자

## Sudo 버전으로 해보자

sudo apt-get update && sudo apt-get upgrade -y && sudo apt install containerd -y && sudo apt install docker.io -y &&
sudo systemctl enable --now docker sudo curl
-L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o
/usr/local/bin/docker-compose sudo chmod +x /usr/local/bin/docker-compose git
clone https://github.com/delimitrou/DeathStarBench.git && cd DeathStarBench/socialNetwork/ && sudo docker-compose up -d
sudo apt install python3-pip && pip3 install aiohttp && sudo apt-get install libssl-dev && sudo apt-get install luarocks
&& sudo luarocks install luasocket && sudo apt-get install libz-dev

이거 안되면

오 일단 initi_social graph 실행은 됨

제발 되라

오 된다

![img.png](img.png)

![img_1.png](img_1.png)

일단 좀만 수자

## Sinan껄로 해야함

Script를 정리를 하자

    1 sudo apt-get update && sudo apt-get upgrade -y && sudo apt install containerd -y && sudo apt install docker.io
-y && sudo systemctl enable --now docker
    2  docker --version
    3  sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    4  sudo chmod +x /usr/local/bin/docker-compose && docker-compose version
    5  sudo chmod +x /usr/local/bin/docker-compose
    6  docker-compose version
    7  docker-compose --version
    8  docker-compose
    9  docker-compose --version
   10  curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
   11  sudo chmod +x /usr/local/bin/docker-compose
   12  docker-compose --version
   13  sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   14  sudo chmod +x /usr/local/bin/docker-compose
   15  docker-compose --version
   16  git clone https://github.com/delimitrou/DeathStarBench.git
   17  cd DeathStarBench/socialNetwork/
   18  docker-compose up -d
   19  sudo docker-compose up -d
   20  sudo apt install python3-pip
   21  pip3 install aiohttp
   22  sudo apt-get install libssl-dev
   23  sudo apt-get install luarocks
   24  sudo apt-get install libz-dev
   25  sudo luarocks install luasocket
   26  ls -rlt
   27  python3 scripts/init_social_graph.py
   28  cd make
   29  cd wrk2/
   30  make -j8

## Installation Script

```bash

sudo apt-get update && sudo apt-get upgrade -y && sudo apt install containerd -y && sudo apt install docker.io -y && sudo systemctl enable --now docker && docker --version


sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose --version

git clone https://github.com/delimitrou/DeathStarBench.git && cd DeathStarBench/socialNetwork/ && sudo docker-compose up -d

sudo apt install python3-pip && pip3 install aiohttp && sudo apt-get install libssl-dev && sudo apt-get install luarocks && sudo apt-get install libz-dev && sudo luarocks install luasocket

python3 scripts/init_social_graph.py

cd wrk2/ && make -j$(nproc)
```

# 이제 뭐를 해야하지?

1. 젤 쉬운 것부터 하자
다 돌려보고 뭐가뭐가 Invoke가 되는지 정리를 해야겠다.  Service가 5개가 있다고 말을 해주고  하면 될듯
2. 이거 금욜에 해도 충분할듯 -> 오늘 좀더 해야할꺼같은디.

## Jaeger - 16686

![img_2.png](img_2.png)

cd wrk2
./wrk -D exp -t 1 -c 1 -d 1 -L -s ./scripts/social-network/compose-post.lua
http://localhost:8080/wrk2-api/post/compose -R 1


![img_3.png](img_3.png)

5초는 해야 결과가 나오네

./wrk -D exp -t 5 -c 5 -d 5 -L -s ./scripts/social-network/compose-post.lua
http://localhost:8080/wrk2-api/post/compose -R 5


# 이제 분석을 해보자

총 5가지를 한다면 이렇게 하면 될꺼같은데

뭐 인지 찾아보자

OpenWhisk 버전에서 찾아보자

compose_post


read_home_timeline_pipeline
    read_home_timeline', 'read_post

read_user_timeline_pipeline
    read_user_timeline', 'read_post

3개만 하자


# 목표가 뭐지?

Frequency 보면 되지

일단 Graph 보고 맞는지 확인을 해보자


# Compose Post Service

Nginx Web Server

compose-post-service	8	6.07ms	0.76ms	0.15ms	2.25ms	0.83ms	0.10ms	-0.20ms	0.17ms	27.07%
nginx-web-server	3	8.73ms	2.91ms	2.76ms	3.07ms	0.83ms	0.28ms	0.14ms	0.51ms	26.94%
text-service	3	2.08ms	0.69ms	0.41ms	0.98ms	0.61ms	0.20ms	0.15ms	0.30ms	19.68%
user-timeline-service	3	1.20ms	0.40ms	0.10ms	0.62ms	0.62ms	0.21ms	0.05ms	0.47ms	20.30%
home-timeline-service	3	1.54ms	0.51ms	0.16ms	0.78ms	0.32ms	0.11ms	0.03ms	0.16ms	10.31%
url-shorten-service	2	0.95ms	0.47ms	0.42ms	0.53ms	0.53ms	0.26ms	0.11ms	0.42ms	17.08%
user-mention-service	2	0.51ms	0.25ms	0.24ms	0.27ms	0.27ms	0.13ms	0.02ms	0.24ms	8.62%
post-storage-service	2	0.71ms	0.36ms	0.33ms	0.38ms	0.38ms	0.19ms	0.04ms	0.33ms	12.26%
social-graph-service	2	0.91ms	0.46ms	0.45ms	0.47ms	0.47ms	0.23ms	0.02ms	0.45ms	15.16%
user-service	1	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.26%
media-service	1	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.23%
unique-id-service	1	0.02ms	0.02ms	0.02ms	0.02ms	0.02ms	0.02ms	0.02ms	0.02ms	0.52%

Frequency 라고는 할수가 없네

![img_4.png](img_4.png)

![img_5.png](img_5.png)


# HOME TIME LINE SERVICE

cd wrk2 && ./wrk -D exp -t 5 -c 5 -d 5 -L -s ./scripts/social-network/read-home-timeline.lua 
http://localhost:8080/wrk2-api/home-timeline/read -R 5

![img_6.png](img_6.png)

![img_7.png](img_7.png)

nginx-web-server	3	4.49ms	1.50ms	0.74ms	2.20ms	2.01ms	0.67ms	0.55ms	0.81ms	91.33%
home-timeline-service	2	0.28ms	0.14ms	0.08ms	0.19ms	0.19ms	0.09ms	0.08ms	0.10ms	8.49%
post-storage-service	1	0.00ms	0.00ms	0.00ms	0.00ms	0.00ms	0.00ms	0.00ms	0.00ms	0.18%

# USER TIME LINE SERVICE

![img_8.png](img_8.png)

nginx-web-server	3	4.03ms	1.34ms	1.05ms	1.83ms	1.06ms	0.35ms	0.10ms	0.68ms	57.70%
user-timeline-service	3	0.89ms	0.30ms	0.01ms	0.77ms	0.77ms	0.26ms	0.01ms	0.66ms	41.91%
post-storage-service	1	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.01ms	0.38%


### API를 Multi Function을 적어봐야겠다.

일단 C++, LUA, PY 이거 3개를 다 전화해봐야겠다.

gen-c++ 은 뭘까


gen-cpp

ComposePostService

    ComposePostHandler
        Redis
        ThriftClient

    UploadText
    UploadMedia
    UploadUniqueId
    UploadCreator
    UploadUrls
    UploadUserMentions
    _ComposeAndUpload
    _UploadPostHelper
    _UploadUserTimelineHelper
    _UploadHomeTimelineHelper


HomeTimelineService
    ReadHomeTimeline

MediaService
    UploadMedia

PostStorageService
    StorePost
    ReadPost
    ReadPosts

SocialGraphService
    GetFollowers
    GetFollowees
    Follow
    UnFollow
    FollowWithUserName
    UnfollowWithUserName
    InsertUser

TextService
    UploadText

UniqueidService
    UploadUniqueId
    HashMacAddressPid
    GetMachineId

UrlShortenService
    UploadUrls
    GetExtendedUrls
    _GenRandomStr

UserMentionService
    UploadUserMentions

UserService
    (Social Netowrk)
        GetCounter
        GetRandomString
    RegisterUser
    RegisterUserWithId
    UploadCreaterWithUserId
    UploadCreatorWithUsername
    Login
    GetUserId
    HasMacAddressPid
    GetMachineId

UserTimelineService
    WriteUserTimeline
    ReadUserTimeline

WriteHomeTimelineService -> No Header
    OnReceivedWorker
    HeartbeatSend
    WorkerThread


                                 
## 2020-10-18

일단 Instance 시키자

지수꺼 

export AWS_DEFAULT_REGION=us-east-1
export AWS_ACCESS_KEY_ID=ASIAY2UKOB7MGLFVBEV3
export AWS_SECRET_ACCESS_KEY=hD6BfM3xosMlJiroI5rBBx40IU7x1pzypdlsd8fR
export AWS_SESSION_TOKEN=IQoJb3JpZ2luX2VjECYaCXVzLWVhc3QtMSJHMEUCIDbZFk/acSk6eNfoB1rQEtuk6RbXMZ611SQvtstZ59tjAiEAjM/950tKaaSOmUJ8p+szCqH1czzVY5HuBQHOPhgqidwqoAIIrv//////////ARAAGgw2MDY5NTQ0NTkwOTYiDBfB7DC5Pslvp1/Jeir0AfRZ9whwjiyx5sBKpMEFEaW/g9ASK0hYlLcT6BQTe7sji9sZERiNHq6TGLU6EU4cBPfjSM08clvHCxsmDj8h/nuqJKVBdzLn0mWLao8owTPBDNLfnbaSDlx6/KBVGt0tbA1AyPplaPi8CSF58qW7clWqEEav7NGM8nPhJw2v/wZZjBcgqm/pkRjvSud/E/wbZw3/ZbJ0qlg5V6NFWSEwIpzu362Sr+HDJ8jon2HCVQqA3lFXXl9i62hfQf4aq5ETd3cQ5PazaTHDl1sfvNEbZa4pKfYzseAq2+2ULMA727ZvIYOR4qP1TMHkWfOrPi0YLGkmE78w0cm3iwY6nQHod01bRbkupgJIHnbmIFoltE8gMMl4vwzOqqWRThAcdIRk0F7xgzEZqKKlcorW1cUjRK551+DhgYwWHSby029LPJYf9Eg4F4p3GVparKqSxcwt20IAYgqtSkEDs4Xkt2rO+kFXv8MyyBSN62Go+Xg76lt5t56UEqqf3VjwDE52AVEr1sHvaaMSiQY9R3P/UiGBDDQIwCRPGB2GjO6Q

Ubuntu 써야함 

20.04 인거같은디

m5.2xlarge

8080 8081 16686
                 

                                                                 
2xlarge 안되네 

4xlarge 해야하겠네 

해보는 중 됬으면 좋겠구먼

여기가 젤 나을수도 잘 보이고 모니터도 크고 괜찮은거같네 


## Installation 정보

m5.4xlarge

8080 8081 16686

> Installation Script

```bash

sudo apt-get update && sudo apt-get upgrade -y && sudo apt install containerd -y && sudo apt install docker.io -y && sudo systemctl enable --now docker && docker --version

sudo apt install python3-pip -y && pip3 install aiohttp && sudo apt-get install libssl-dev -y && sudo apt-get install luarocks -y && sudo apt-get install libz-dev -y && sudo luarocks install luasocket

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose --version

git clone https://github.com/delimitrou/DeathStarBench.git && cd DeathStarBench/socialNetwork/ && sudo docker-compose up -d

python3 scripts/init_social_graph.py

cd wrk2/ && make -j$(nproc)
```

> Trace IP

<instance_ip>:16686


> Running workload


cd wrk2 && ./wrk -D exp -t 5 -c 5 -d 5 -L -s ./scripts/social-network/read-home-timeline.lua http://localhost:8080/wrk2-api/home-timeline/read -R 5

설마 4xlarge 다음은 뭐지?

안되네;; 8xlarge를 해보자 

r5.4xlarge 를 해보자 

0 upgraded, 0 newly installed, 0 to remove and 8 not upgraded.

여기서 오류가 나네 

r5.4xlarge 에서 다시 설치 스크립트 순서를 바꿔보자 -> 

> Instance 

r5.4xlarge 

sudo apt-get update && sudo apt-get upgrade -y && sudo apt install containerd -y && sudo apt install docker.io -y && sudo systemctl enable --now docker && docker --version

sudo apt install python3-pip -y && pip3 install aiohttp && sudo apt-get install libssl-dev -y && sudo apt-get install luarocks -y && sudo apt-get install libz-dev -y && sudo luarocks install luasocket

> Installation Script  - 순서를 바꾸면 되는거같네 

```bash

sudo apt-get update && sudo apt-get upgrade -y && sudo apt install containerd -y && sudo apt install docker.io -y && sudo systemctl enable --now docker && docker --version

sudo apt install python3-pip -y && pip3 install aiohttp && sudo apt-get install libssl-dev -y && sudo apt-get install luarocks -y && sudo apt-get install libz-dev -y && sudo luarocks install luasocket

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose && docker-compose --version

git clone https://github.com/delimitrou/DeathStarBench.git && cd DeathStarBench/socialNetwork/ && sudo docker-compose up -d

python3 scripts/init_social_graph.py

cd wrk2/ && make -j$(nproc)
```

> Workload 실행하기  - ReadHomeTimeline

./wrk -D exp -t 5 -c 5 -d 5 -L -s ./scripts/social-network/read-home-timeline.lua http://localhost:8080/wrk2-api/home-timeline/read -R 5


> ComposePostService 실행해보기 
                                                                                                                                        
./wrk -D exp -t 5 -c 5 -d 5 -L -s ./scripts/social-network/compose-post.lua http://localhost:8080/wrk2-api/post/compose -R 5

그림만 보면 

![img_9.png](img_9.png)

어떤 Function 인지 알수가없네

이상하네

Log를 보면 ComposePost 의 UploadText를 알수가없네




















