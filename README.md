# pomodoro
A pomodoro timer in your terminal

Call from anywhere in terminal by linking to path

```
    ln -s /path/to/pomodoro/pomodoro.py ~/bin/pomodoro
```

```
usage: pomodoro [-h] [-w WORK_LENGTH] [-b BREAK_LENGTH] [-n NUMBER_OF_CYCLES]

A pomodoro timer in your terminal

optional arguments:
  -h, --help            show this help message and exit
  -w WORK_LENGTH, --work_length WORK_LENGTH
                        Length of working session in minutes. Default is 25
  -b BREAK_LENGTH, --break_length BREAK_LENGTH
                        Length of break in minutes. Default is 5 mins
  -n NUMBER_OF_CYCLES, --number_of_cycles NUMBER_OF_CYCLES
                        Number of cycles. Default is 4
```     

It plays sound using pygame module, so that needs to be downloaded if you intend to use this. Or you could replace the code with some other sound player.

## TODO
- Replace the sleep with a multithread listener, that allows for pause functionality.
