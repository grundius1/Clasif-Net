# Final-Project image-clasifier

![neural-net](./images/neural-net.png)


## project description

this project is an image clasifier, based on the CIFAR10 dataset with 10 clases which are:

- airplanes 
![airplane1](./images/200.png) ![airplane2](./images/214.png) ![airplane3](./images/221.png)
- automobiles 
![automobile1](./images/61.png) ![automobile2](./images/62.png) ![automobile3](./images/65.png)
- birds
![bird1](./images/64.png) ![bird2](./images/91.png) ![bird3](./images/109.png) 
- cats
![cat1](./images/102.png) ![cat2](./images/142.png) ![cat3](./images/143.png) 
- deers
![deer1](./images/131.png) ![deer2](./images/146.png) ![deer3](./images/150.png)
- dogs
![do1](./images/108.png) ![deer2](./images/129.png) ![deer3](./images/149.png)
- frogs
![frog1](./images/24.png) ![frog2](./images/26.png) ![frog3](./images/73.png)
- horses
![horse1](./images/321.png) ![horse2](./images/322.png) ![horse3](./images/330.png) 
- ships
![ship1](./images/253.png) ![horse2](./images/260.png) ![horse3](./images/281.png)
- trucks
![ship1](./images/68.png) ![horse2](./images/72.png) ![horse3](./images/77.png)



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
