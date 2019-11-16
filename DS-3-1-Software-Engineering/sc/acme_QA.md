# ACME Q&A

### What, in your opinion, is an important part of code reviews? That is, what is something you pay attention to when you review code, and that you appreciate when others do the same for your code?

The most important part of code reviews is prociding feedback for readability, and the following is my (and general pep8) readability reccomendations which should be looked out for:

Having clear variable names is absolutely necessary; apart from short "obvious" count syntaxes,(eg. for `i in range(10)`) it's very important that we don't have arbitrary variables, like x,y,z, but instead we have descriptive variable names like "product\_width". It's important to keep all imports at the top followed by definitions. All the runnable code should be present at the bottom. In general, lines should not be too long. The default terminal size on most machines is about 80 charactrs so it's a good rule of thumb to keep the line lengths less than this.


### We have an awful lot of computers here, and it gets pretty confusing with slightly different things running on all of them. How could containers help us improve this situation? Docker can run their own environments they are separate from the operating system.

Containers can establish the baseline environment for a code to run perfectly. One system may have different versions of python libraries (numpy, sk-learn etc.). It's possible that these libraries are later updated and no longer support interdependancies. (an idea that comes to mind is the new version of seaborn being unable to display a pandas output. in class we needed to revert to a forer version). But much more detailed than specific python libraries, we are able to specify the OPERATING SYSTEM. Most importabtly, docker makes for an ideal fix to the "works on my computer" problem by speeding up the testing. One simply needs to run the docker environment then test the product, no need for lengthy installs or setting up virtual environments
