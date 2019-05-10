PROM Pong
---------

`python3 src/test_SerialSevenSeg.py`

There are a bunch of other test files. test_Serial will work without music and the seven seg. Though it'll have issues if the i2c devices aren't connected. 

`Pong.py` is the main game class which deals with instantiating all the of the game objects and the update / render functions. Look at `Game.py` to see the parent type. Should be pretty easy to make other games using Game.py and GameObject.py and the other classes around it. 
