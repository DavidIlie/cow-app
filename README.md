# Cow App
As part of my GCSE Computer Science course, I was asked (along with my classmates) to produce an python console application which "calculates" the statistics about the yeilding of cows in a farm. Here is the task below.

```
TASK 1 – Record the yield.
Write a program for TASK 1 to record the milk yields for a week. The program records and stores the
identity code number and the yield every time a cow is milked.

TASK 2 – Calculate the statistics.
Using your recorded data from TASK 1, calculate and display the total weekly volume of milk for the
herd to the nearest whole litre. Calculate and display the average yield per cow in a week to the
nearest whole litre.

TASK 3 – Identify the most productive cow and cows that are producing a low volume of milk.
Extend TASK 2 to identify and display the identity code number and weekly yield of the cow that has
produced the most milk. Also identify and display the identity code numbers of any cows with a yield of
less than 12 litres of milk for four days or more in the week.
```

For the average programmer, this would be normally a simple task. However, if you take a look at the main app file (`app.py`) you would see that its not the case in this situtaion. As python is the programming language that we were told to use, I wanted to expand my knowledge and confidence with using this language. So I completely overexagerated the functionality of this application. The code is perfectly documented insidem so I hope you can get a rough understanding of it if you look through it.

![Gif of the base application running](https://s3.gifyu.com/images/normal-application.gif)

## What does it do?

Apart from the things that were required in the 3 tasks, I implemented a database system which keeps all the data that has been inputted by the user (the farmer in this case) into a JSON file which will be read from whenever the app is run in the future.

There are also command arguments which you can run:

* `-s` or `--speedrun` - It prevents all events where the application waits (at the start or while the "calculations" are going on)

![Gif of the base application running in speedrun mode](https://s3.gifyu.com/images/ezgif-2-51dea15d9fee.gif)

* `-p` or `--pirate` - As we are all lovers of pirate shanties in our classroom. I implemented an option which overrides every single print string into that same string but in Pirate Language using a modified version of the [arrr](https://arrr.readthedocs.io/en/latest/) library.

![Gif of the base application running in pirate mode](https://s3.gifyu.com/images/ezgif-2-4f076b92f016.gif)

## How to run cow-app
It's really simple, the one crucial part is that you need to have python 3.8.5 running (That is the version I know supports this code). Afterwads, you can then run the application with the command below.

```console
python3 app.py
```