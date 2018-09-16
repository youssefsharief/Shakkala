#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example code using Shakkala library
"""
import os
from shakkala import moshakal

if __name__ == "__main__":
    input_text = "فإن لم يكونا كذلك أتى بما يقتضيه الحال وهذا أولى"
    print(moshakal(input_text, 3))