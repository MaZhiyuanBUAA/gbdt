# -*- coding: utf-8 -*-
"""
Created on Fri May 06 14:07:11 2016

@author: Richard
"""
import datetime
import math
import numpy as np

def get_x0(t,f):
	start = t[0]
	end = t[0]
	for i in xrange(len(f)):
		if f[i] == 'a':
			end = t[i]
			break
	d = float((end-start).seconds)/60

	return math.sqrt(d)

def get_x1(t,f):
	start = t[0]
	end = t[-1]
	d = float((end-start).seconds)/60
	return math.sqrt(d)

def get_x2(t,f):
	max = 0.0
	for i in xrange(len(t)-1):
		start = t[i]
		end = t[i+1]
		d = float((end-start).seconds)/60
		if d >= max:
			max = d
	return math.sqrt(max)

def get_x3(t,f):
	end = t[-1]
	for i in xrange(len(t)):
		if f[i] == 'v':
			start = t[i]
	d = float((end-start).seconds)/60
	return math.sqrt(d)

def get_x4(t,f):
	start = t[0]
	end = t[-1]
	d = float((end-start).seconds)/60*len(t)
	return math.sqrt(d)

def get_x5(visitor_t):
	start = visitor_t[0]    
	end = visitor_t[-1]
	d = float((end-start).seconds)/60*len(visitor_t)
	return math.sqrt(d)


def get_x6(agent_t):
	if not agent_t:
		return 0.0
	start = agent_t[0]
	end = agent_t[-1]
	d = float((end-start).seconds)/60*len(agent_t)
	return math.sqrt(d)

def get_x7(visitor_t):
	start = visitor_t[0]
	end = visitor_t[-1]
	d = float((end-start).seconds)/60
	return math.sqrt(d)

def get_x8(agent_t):
	if not agent_t:
		return 0.0
	start = agent_t[0]
	end = agent_t[-1]
	d = float((end-start).seconds)/60
	return math.sqrt(d)

def get_x9(ds):
	if ds.find('5分钟') > 0 or ds.find('五分钟') > 0:
		return 1.0
	else:
		return 0.0

def time_feature(dialog):
	dialog_t = []
	dialog_f = []
	visitor_t = []
	agent_t = []
	x = np.zeros(10)
	for sentence in dialog:
		t = sentence.split('|')[0].strip()
		t = t.replace('：',':')
		t = t[:19]
		if not t.strip():
			continue
		dialog_t.append(datetime.datetime.strptime(t,'%Y-%m-%d %H:%M:%S'))
		if sentence.find('Visitor') >0:
			dialog_f.append('v')
			visitor_t.append(datetime.datetime.strptime(t,'%Y-%m-%d %H:%M:%S'))    
		else:
			dialog_f.append('a')
			agent_t.append(datetime.datetime.strptime(t,'%Y-%m-%d %H:%M:%S'))

	x[0] = get_x0(dialog_t,dialog_f)
	x[1] = get_x1(dialog_t,dialog_f)
	x[2] = get_x2(dialog_t,dialog_f)
	x[3] = get_x3(dialog_t,dialog_f)
	#平均句对话时间
	x[4] = get_x4(dialog_t,dialog_f)
	#visitor对话平均时间
	x[5] = get_x5(visitor_t)
	#agent对话平均时间
	x[6] = get_x6(agent_t)    
	#visitor对话总时间
	x[7] = get_x7(visitor_t)
	#agent对话总时间
	x[8] = get_x8(agent_t)

	x[9] = get_x9(''.join(dialog))

	return x

class feature3(object):

	def extractF3(self, dialogs):
		f3 = list()
		for dialog in dialogs:
			f3.append(time_feature(dialog))
		return f3

