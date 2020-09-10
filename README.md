# Elevator_Algorithm
maths problem : n exponential


Last winter I wanted to try and learn some Python. So I found a problem to solve with an algorithm. Here it is :

"We need to lift packets up to the first floor with an elevator.

The elevator can carry a maximum of 225lb.

Here's the weight of our packets : 75lb - 105lb - 125lb - 70lb - 90lb - 40lb

Can we lift all of it, going up only three times ?"

It's a mathematical problem meant for 9 years old pupils, to force them to try and correct.

Let's create an algorithm with unknown figures for :

- Max weight the elevator can carry

- Number of packets

- Weight of the packets

Now, how do we get the minimum of come and goes ?

My first idea was : 

Ok, let's write an algorithm that will give me the exact minimum every time. So, let's do this :

 - Take all the packets

 - Try out every combinations of packets

 - Choose the best one(s)

... yes, problem is : so much computing.

Here's an other idea :

 - Let's take the heaviest packet

 - Add the lightest(s) packet(s) until it goes above the maximum weight

 - Remove the last packet added and put it back in the packet pool

 - Repeat until there's no packet left

... It works nice !

I added a little indicator to see mathematically the best figure we could get.

Most of the time, there only one packet more
