# StatefulUC

A Class instance to Flet UserControl have many tools for make re-render and manage state's

You can use like the pure UserControl without any problems, and it's canbe SYNC or ASYNC

### ⚠️ Important:

If you set it `ASYNC` and the page is `SYNC `. And you will get `ValueError` say you uses a wrong Page Type

### Basic Usage

```python

```

...

First we Import flet as ft and import the `StatefulUC` from stateful_flet

And we make new StatefulUC Class and we called him `App` and we super the init.

And make new `state` have the True Value and save it in the `self.myState` .

In `build` we made some simple ui that's select the colors and values from the state : " 'blue' if state is True else 'black' "

And make the button when clicked will change the value from True to False and like that by using `self.myState.set(...)`

State get's you using lambda and function for set the value by get the returned value from it

In our example: `lambda v: not v` .

It's will give the `v` and the v is the state value and we return `not v` that's make True to False, and False to True

When the value setted the Statful will be re-rendered by re-render the build content and update the control

**And congratulations you have simple stateful application in flet**
