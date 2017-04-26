# Galaxy Cloud instances

A [Galaxy Instance 1](https://github.com/ibivu/B4TM-Galaxy-2017/tree/master/docker#galaxy-instance-1---on-port-8880) is running separately on two servers, each of which has 12 CPUs and 80 GB memeory. Each group will be allocated only one of the servers. Optionally, you may finish Part 1 of the assignment there, if Docker does not work normally in your computer; likewise, you may run Heinz for Part 2 there, if your computer cannot handle the computation.

**Due to the limited computation resources, each group should run only one  (Heinz) job  at any given time.**

## Galaxy cloud instance list

Name     | URL                                   | Group No.
:------: | :-----------------------------------: |:-----:
Server A |galaxy-a.bioinformatician.science:8880 | odd numbers
Server B |galaxy-b.bioinformatician.science:8880 | even numbers

Group 1,3,5,7 ... should use Server A

Group 2,4,6,8 ... should use Server B

## How to run Heinz on Galaxy cloud instance

1. Download the input data of Heinz from your local Galaxy instance.
2. Upload these data into the Galaxy cloud instance. 
3. Run Heinz tool on the Galaxy cloud instance.
4. Wait. Make sure not to submit more than one Heinz job per group at any time.
