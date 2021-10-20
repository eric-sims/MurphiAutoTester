# MurphiAutoTester
Rewrite a .m (CMurphi) file and recompile it for 3 different scenarios I have coded into it.

For my research, I was working on applying the notion of the Dining philosophers problem to a model checking software called CMurphi with it's own Murphi language. I was testing three ways that the diners would "eat", one where each diner would immediately pick up and put down both forks, another where every diner picks up their left except one that picks up the right, and finally another where all diners are left handed.

While not wanting to write out three different ".m" files and manually changing the number of philosophers, while manually recording the test results, I decided to automate the process while working from one file. The way it works is that it can rewrite where I have defined the number of philosiphers, and it can also comment out/in the three different scenarios. It has to recompile the file every time. Then, it automatically records the results that I need in a nice file for me to observe.
