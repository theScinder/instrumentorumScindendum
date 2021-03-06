""" This script can be used to compare documents using t-distributed stochastic neighbor embedding for dimensionality reduction. To use, replace the urls in the demo with urls pointing to articles you want to compare. 

The name was generated by a recurrent neural network trained on ficitonal sword names from https://en.wikipedia.org/wiki/List_of_fictional_swords#In_Arthurian_fiction"""
# Import packages

# Import numpy, natch
import numpy as np

# For tic-toc funcitonality
import time

# plotting
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
#for 3D plotting
from mpl_toolkits.mplot3d import Axes3D

# You may want to change the dpi settings to suit your screen
myDPI = 120

# For getting websites 
import urllib.request
import urllib
from urllib.error import HTTPError

from bs4 import BeautifulSoup as bs

# For performing TSNE dimensionality reduction
import sklearn
from sklearn.manifold import TSNE



# make an array of web addresses for documents you want to compare
# As a demo, I've selected some articles covering recent scientific breakthroughs in gravitational wave detection and cas9 editing of human embryos. 

# aLIGO third black hole merger detection
myAddys = ['https://www.ligo.caltech.edu/page/press-release-gw170104']
myAddys.append('http://www.thehindu.com/sci-tech/science/us-lab-ligo-strikes-again-detects-a-third-gravitational-wave-merger/article18700551.ece')
myAddys.append('https://richarddawkins.net/2017/06/ligos-third-detection-hints-at-how-black-hole-binaries-are-born/')
myAddys.append('http://www.caltech.edu/news/ligo-detects-gravitational-waves-third-time-78193')
myAddys.append('https://phys.org/news/2017-06-gravitational-insight-black-holes.html')
myAddys.append('https://www.nytimes.com/2017/06/01/science/black-holes-collision-ligo-gravitational-waves.html')
myAddys.append('https://news.northwestern.edu/stories/2017/june/ligo-detects-gravitational-waves-for-third-time/')
myAddys.append('https://www.newscientist.com/article/2133353-ligos-third-detection-hints-at-how-black-hole-binaries-are-born/')
# CRISPR used for editing human embryos in US
myAddys.append('https://www.washingtonpost.com/news/to-your-health/wp/2017/08/02/first-human-embryo-editing-experiment-in-u-s-corrects-gene-for-heart-condition/')
myAddys.append('http://news.nationalgeographic.com/2017/08/human-embryos-gene-editing-crispr-us-health-science/')
myAddys.append('https://www.geekwire.com/2017/oregon-team-uses-crispr-editing-fix-gene-linked-heart-disease-embryos/')
#myAddys.append('https://techcrunch.com/2017/08/02/bravenewcrisprdworld/')
myAddys.append('https://www.sciencenews.org/article/crispr-gene-editing-human-embryos')
myAddys.append('https://futurism.com/first-u-s-human-embryo-gene-editing-experiment-successfully-corrects-a-heart-condition/')
myAddys.append('http://www.nature.com/news/crispr-fixes-disease-gene-in-viable-human-embryos-1.22382')
myAddys.append('http://www.medicaldaily.com/crispr-gene-editing-technology-removes-heart-disease-mutation-embryos-420977')


myScrapes = ['']
myText = ''
for addy in myAddys:
    print(addy)
    #myURL = urllib.request.urlopen(addy)
    req = urllib.request.Request(url=addy,headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    try:
        handler = urllib.request.urlopen(req)
    except HTTPError as e:
        content = e.read()
    myURL = handler #urllib.request.urlopen(myAddy)

    myFit = myURL.read()
    soup = bs(myFit, 'html.parser')
    soupText = soup.get_text()
    myText = myText + soupText
    myScrapes.append(soupText)
    # Scrape all the text into one big string to build the BOW from
myText = ''
for addy in myAddys:
    print(addy)
    #myURL = urllib.request.urlopen(addy)
    req = urllib.request.Request(url=addy,headers={'User-Agent':' Mozilla/5.0 (Windows NT 6.1; WOW64; rv:12.0) Gecko/20100101 Firefox/12.0'})
    try:
        handler = urllib.request.urlopen(req)
    except HTTPError as e:
        content = e.read()
    myURL = handler #urllib.request.urlopen(myAddy)

    myFit = myURL.read()
    soup = bs(myFit, 'html.parser')
    myText = myText + soup.get_text()
    # Create a dictionary bag-of-words for 
wordcount = {}
weirdChar = ['[','{',']','}',':',';','%','/','/','.filename','-','+','=']



for word in myText.split():
    # Check for weird character
    dontAdd = 1
    for wChar in weirdChar:
        if(word.find(wChar) != -1):
            wordcount = wordcount
            dontAdd = 0
            #print('weird character detected')
    # Add word to wordcount dictionary if it seems to be a real weird. 
    if (dontAdd):
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
print(len(wordcount))

if(0):
    for k, v in wordcount.items():
        print(k,v)

# Build bag-of-words Dictionary based on the combined job descriptions
bowDict = {}
for word in wordcount:
    bowDict[word] = 0  
    myTemp = bowDict
X = np.array([[1]])
print(X)
a0 = np.array([[0],[0]])
print(a0)
print(len((a0[1])))

if(1):
    for jd in myScrapes:
        # Scan through each word in each job description, add to worcount vectors for each entry
        for word in jd:
            if word in myTemp:
                myTemp[word] += 1
        # store the BOW vector in the input vector
        X = np.array([[1]])
        for k, v in myTemp.items():
        #    print(k,v)
            X = np.append(X,[[v]],1)
        #print(np.shape(X))
        if (len((a0[0])) > 2):
            #print('etet')
            #print(np.shape(a0))
            #print(np.shape(X))
            a0 = (np.append(a0,X,0))
        else:
            #print('adfad')
            #print(np.shape(a0))
            a0 = X
            #print((np.shape(a0)))
            #print(np.shape(a0))
                

myMax = np.median(a0)

a00 = a0
a0 = a0 / (np.mean(a0) * 2)

# Build a TSNE model and fit to the document bag-of-words data
myModel = TSNE(n_components=2,random_state=0,init='pca')
myFit = myModel.fit_transform(a0)

fig = plt.figure(dpi=myDPI)

ax = fig.add_subplot(111)
ax.scatter(myFit[0:8,0],myFit[0:8,1],color=[0,1,0])
ax.scatter(myFit[8:16,0],myFit[8:16,1],color=[1,0,0])

#ax.scatter(myFit[0:8,0],myFit[0:8,1],myFit[0:8,2],color=[0,1,0])
#ax.scatter(myFit[8:16,0],myFit[8:16,1],myFit[8:16,2],color=[1,0,0])
plt.show()

