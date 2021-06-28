#!/usr/bin/env python
# coding=utf-8


# Copyright (C) 2021 Amal Santhosh , amalsanp@gmail.com

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
"""
Description of this extension
"""

import inkex
import pytesseract
from PIL import Image
import cairosvg
import os



class OcrOutputExtension(inkex.OutputExtension):

    def add_arguments(self, pars):
        pars.add_argument("--my_option", type=inkex.Boolean,\
            help="An example option, put your options here")

    def effect(self):
        try:
            cairosvg.svg2png(url=self.file_io.name, write_to='read.png')
            im = Image.open('read.png')
            text = pytesseract.image_to_string(im,lang ='eng')
            inkex.errormsg(text.rstrip())
            os.remove('read.png')
        except:
            return
    def save(self,stream):
        pass

if __name__ == '__main__':
    OcrOutputExtension().run()
