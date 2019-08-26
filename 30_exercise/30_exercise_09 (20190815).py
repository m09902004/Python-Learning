# -*- coding: utf-8 -*-
"""
  ┌─────────────┐
  │哈哈！你不及格 │
  └─v──────v────┘
  (☞ﾟ∀ﾟ)ﾟ∀ﾟ)☞         ლ(´•д• ̀ლ)
"""

#數學及格
gMath={'Tom','John','Mary','Jimmy','Sunny','Amy'}
#英文及格
gEng={'John','Mary','Tony','Bob','Pony','Tom','Alice'}
#數學及格但英文不及格
print('\n數學及格但英文不及格(1)： ',gMath-gEng)
print('數學及格但英文不及格(2)： ',gMath.difference(gEng))
#數學不及格但英文及格
print('\n數學及格但英文不及格(1)： ',gEng-gMath)
print('數學及格但英文不及格(2)： ',gEng.difference(gMath))
#數學&英文都及格
print('\n數學&英文都及格(1)： ',gMath-(gMath-gEng))
print('數學&英文都及格(2)： ',gMath&gEng)
print('數學&英文都及格(3)： ',gMath.intersection(gEng))
#至少一科及格
print('\n至少一科及格(1)： ',set(list(gMath)+list(gEng-gMath)))
print('至少一科及格(2)： ',gMath|gEng)
print('至少一科及格(3)： ',gMath.union(gEng))
#僅一科及格
print('\n僅一科及格(1)： ',set(list(gMath-gEng)+list(gEng-gMath)))
print('僅一科及格(2)： ',gMath^gEng)
print('僅一科及格(3)： ',gMath.symmetric_difference(gEng))
