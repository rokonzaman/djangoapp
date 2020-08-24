#!/bin/bash
sed "s/tagVersion/$1/g" django.yml > django-deployment.yml
