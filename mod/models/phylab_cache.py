#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-03-13 12:44:28
# @Author  : yml_bright@163.com

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from db import engine, Base

class PhylabCache(Base):
    __tablename__ = 'phylab'
    cardnum = Column(Integer, primary_key=True)
    text = Column(String(1024), nullable=False)
    date = Column(Integer, nullable=False)
