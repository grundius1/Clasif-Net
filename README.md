# Final-Project image-clasifier

![neural-net](./images/neural-net.png)


## project description

this project is an image clasifier, based on the CIFAR10 dataset with 10 clases which are:

- airplanes 
![airplane1](./images/200.png)
- automobiles 
![automobile1](./images/61.png)
- birds
![bird1](./images/64.png) 
- cats
![cat1](./images/102.png) 
- deers
![deer1](./images/131.png)
- dogs
![do1](./images/108.png) 
- frogs
![frog1](./images/24.png) 
- horses
![horse1](./images/321.png) 
- ships
![ship1](./images/253.png) 
- trucks
![ship1](./images/68.png)



## libraries used
the list of libraries used are:
- os
- argparse
- sys
- keras
- tensorflow
- csv
- tqdm

## usage
the code work wit argparse, you can ask for predict one file or all the files in a folder:
- file:
``` python3 main.py --fil <filepath>```
- folder: 
``` python3 main.py --fol <folderpath>```


## neural net
the neural net used now has a 77% accuracy in validation


## further steps
increase the neural network accuracy
