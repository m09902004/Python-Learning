# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:47 2019

@author: ASUS
"""

from bs4 import BeautifulSoup
import requests
import pandas
import os
import re

os.getcwd()

url = 'https://www.taiwanlottery.com.tw/index_new.aspx'

res = requests.get(url).text

soup = BeautifulSoup(res, 'html.parser')

#print(soup.prettify())

bingo = soup.select("div.contents_box01 div.ball_tx.ball_yellow")
winwin = soup.select("div.contents_box06 div.ball_tx.ball_blue")[:12]
power = soup.select("div.contents_box02 div.ball_tx.ball_green")[:12]
bigpot = soup.select("div.contents_box02 div.ball_tx.ball_yellow")[:12]
rb539 = soup.select("div.contents_box03 div.ball_tx.ball_lemon")[:10]
star3 = soup.select("div.contents_box04 div.ball_tx.ball_purple")[:3]
star4 = soup.select("div.contents_box04 div.ball_tx.ball_purple")[3:]

'''
<!--***************BINGO BINGO**************-->
    <div class="contents_box01">
    <div class="ball_tx ball_yellow">
 <!--***************雙贏彩區塊***************-->
    <div class="contents_box06">
    <div class="ball_tx ball_blue">
<!--***************威力彩區塊***************-->
    <div class="contents_box02">
    <div class="ball_tx ball_green">
<!--***************大樂透區塊***************-->
    <div class="contents_box02">
    <div class="ball_tx ball_yellow">
<!--**************今彩539區塊**************-->
    <div class="contents_box03">
    <div class="ball_tx ball_lemon">
<!--**************3星彩區塊**************-->
    <div class="contents_box04">
    <div class="ball_tx ball_purple">
<!--**************4星彩區塊**************-->
    <div class="contents_box04">
    <div class="ball_tx ball_purple">
'''






