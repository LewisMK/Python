from sys import path

path.append('..\\Packages\\extra2.zip')

#we can put all modules in the tree structure (directory) in a zip file
#python sees it as a file still
#this feature helps to save program space/size by having the package as a zip file

import extra.iota
print(extra.iota.FunI())

import extra.good.best.sigma

from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())


#We can make this process easier using aliasing

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())


#When adding an absolute path, always use \\ between different levels e.g. user\\python\\module\\
