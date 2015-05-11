#coding=utf-8
from flask import Flask,request,render_template,redirect,escape,Markup
from re import template

app=Flask(__name__)
from app import views
