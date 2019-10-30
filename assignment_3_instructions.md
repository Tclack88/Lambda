# The chain of commands I did for success

1. Created an empty directory I called `dockertest`

2. Created a docker file `Dockerfile` with the following content
```docker
FROM debian
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl nano -y && \
pip3 install pandas numpy && \
pip3 install -i https://test.pypi.org/simple/ lambdata-tclack && \
python3 -c "import lambdata_tclack; print('success')"
```

3. Build the docker image

`sudo docker build . -t lambdata`

(This takes a few minutes)

4. Run the docker image/environment to ver
sudo docker run -it lambdata /bin/bash


5. opened a python3 interpreter and tested my module

`python3`

here are the commands I ran to test my lambdata module:
```python
sudo docker run -it lambdata /bin/bash
root@de945548ee60:/# python3
Python 3.7.3 (default, Apr  3 2019, 05:39:12) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import lambdata_tclack as lt
>>> import pandas as pd
>>> a = pd.DataFrame({'col 1':[1,2,3],'another column':[4,5,6]})
>>> a
   col 1  another column
0      1               4
1      2               5
2      3               6
>>> from lambdata_tclack.df_utils import ImprovedDataFrame
>>> mya = ImprovedDataFrame(a)
>>> mya
   col 1  another column
0      1               4
1      2               5
2      3               6
>>> mya.simplify_cols()
   col_1  another_column
0      1               4
1      2               5
2      3               6
>>> mya.correctify()
            col 1  another column
0  Mikayla Smells  Mikayla Smells
1  Mikayla Smells  Mikayla Smells
2  Mikayla Smells  Mikayla Smells
>>> mya.simplify_cols().correctify()
            col_1  another_column
0  Mikayla Smells  Mikayla Smells
1  Mikayla Smells  Mikayla Smells
2  Mikayla Smells  Mikayla Smells
>>> 

```
