# -*- coding: utf-8 -*-

from MagicBrain import settings

import random
import os

from PIL import Image

import string

import datetime
import time



class string_with_title(str):
    def __new__(cls, value, title):
        instance = str.__new__(cls, value)
        instance._title = title
        return instance

    def title(self):
        return self._title

    __copy__ = lambda self: self
    __deepcopy__ = lambda self, memodict: self

def howlong(timestamp):
  
    current_timestamp = time.mktime(datetime.datetime.now().timetuple())
    second = current_timestamp - timestamp
    
    year = int(second / 60 / 60 / 24 / 30 / 12)
    
    if year > 0:
      y = year * 12 * 30 * 24 * 60 * 60
      second = second - y
    
    month = int(second / 60 / 60 / 24 / 30)
    
    if month > 0:
      m = month * 30 * 24 * 60 * 60
      second = second - m
    
    day = int(second / 60 / 60 / 24)
    
    if day > 0:
      d = day * 24 * 60 * 60
      second = second - d
    
    hour = int(second / 60 / 60)
    
    if hour > 0:
      h = hour  * 60 * 60
      second = second - h
      
    minute = int(second / 60)
    
    if minute > 0:
      m = minute  * 60
      second = second - m
    
    res = {"year":year, "month":month, "day":day, "hour":hour, "minute":minute, "second":second}
    return res
    

def get_thumbnail_url(image_url, size=300):
    thumbs_part = 'thumbs_' + str(size)
    image_url_parts = image_url.rsplit('/', 1)
    return image_url_parts[0] + '/' + thumbs_part + '/' + image_url_parts[1]

def get_mobile_path(path):
    path = path.rsplit('/', 1)
    return path[0] + '/mobile/' + path[1]

def get_image_original_path(image_path):

    if "/original/" in image_path:
        return image_path

    dirname, filename = os.path.split(image_path)
    dirname = os.path.join(dirname, "original")

    return os.path.join(dirname, filename)

def get_thumbnail_path(image_path, size=300):

    
    thumbs_dir = 'thumbs_' + str(size)
    
    dirname, filename = os.path.split(image_path)
    
    dirname = os.path.join(dirname, thumbs_dir)
   
    if not os.path.exists(dirname):
        print("HEEEEEEELLLLLLOOOOOOOOOOO1011101101010101")
        # os.mkdir(dirname, 0755)
    return os.path.join(dirname, filename)

def create_thumbnail(image_path, size=300): 
    thumb_path = get_thumbnail_path(image_path, size)
    img = Image.open(image_path)
    img.thumbnail((size, size), Image.ANTIALIAS)
    img.save(thumb_path)
    

def gen_unique(count_char = 32):
    abs = "qwertyuioplkjhgfdsazxcvbnmQAZXSWEDCVFRTGBNHYUJMKIOLP1234567890"
    
    res = ""
    for i in range(count_char):
        res += random.choice(abs)
        
    return res  
  
  
def handle_uploaded_file(file_data, suffix, path=settings.TMP_IMAGE_UPLOAD_PATH, thumbwidth=300):
    filename =  gen_unique(16) +"_"+ gen_unique(16)+"_" + gen_unique(16) + "." + suffix
    


    with open(settings.MEDIA_ROOT + path + filename, 'wb+') as destination:
        
        for chunk in file_data.chunks():
            destination.write(chunk)
            
    img = Image.open(settings.MEDIA_ROOT + path + filename)
    img_size = img.size

    if thumbwidth > 0:
        
        create_thumbnail(settings.MEDIA_ROOT + path + filename, thumbwidth)
        thumb = Image.open(settings.MEDIA_ROOT + path + get_thumbnail_path(filename, thumbwidth))
        thumb_size = thumb.size
    else:
        thumb_size = [0,0]
    
    return [filename, thumb_size, img_size]
            
def handle_uploaded_file_tmp(file_data, suffix):
  
    with open(settings.MEDIA_ROOT + settings.TMP_IMAGE_UPLOAD_PATH + filename, 'wb+') as destination:
        for chunk in file_data.chunks():
            destination.write(chunk)
            
    img = Image.open(settings.MEDIA_ROOT + settings.TMP_IMAGE_UPLOAD_PATH + filename)
    img_size = img.size
            
            
    create_thumbnail(settings.MEDIA_ROOT + settings.TMP_IMAGE_UPLOAD_PATH + filename, 640)
    
    thumb = Image.open(settings.MEDIA_ROOT + settings.TMP_IMAGE_UPLOAD_PATH + get_thumbnail_path(filename,640))
    
    thumb_size = thumb.size
    
    return [get_thumbnail_path(filename,640),thumb_size, img_size]

def prepareText(string):
  
  sym = {
      u"←" : u"&larr;",
      u"↑": u"&uarr;",
      u"→": u"&rarr;", 
      u"↓": u"&darr;",
      u"↔": u"&harr;",

      u"♠": u"&spades;",      
      u"♣": u"&clubs;",
      u"♥": u"&hearts;",
      u"\"": u"&quot;",
      
      #u"&": u"&amp;",
      u"<": u"&lt;", 
      u">": u"&gt;", 

      u"…": u"&hellip;",
      u"′": u"&prime;",
      u"″": u"&Prime;",

      u"–": u"&ndash;",
      u"—": u"&mdash;",
      u"‘": u"&lsquo;",
      u"’": u"&rsquo;",
      u"‚": u"&sbquo;",
      u"“": u"&ldquo;",
      u"”": u"&rdquo;",
      u"„": u"&bdquo;",
      u"«": u"&laquo;",
      u"»": u"&raquo;",
      
    }
  
  for key, value in sym.items():
        string = string.replace(key, value)
        
  string = string.replace("\n", "<br>")
  return string
  
  
def transliterate(string):
 
    capital_letters = {u'А': u'A',
                       u'Б': u'B',
                       u'В': u'V',
                       u'Г': u'G',
                       u'Д': u'D',
                       u'Е': u'E',
                       u'Ё': u'E',
                       u'З': u'Z',
                       u'И': u'I',
                       u'Й': u'Y',
                       u'К': u'K',
                       u'Л': u'L',
                       u'М': u'M',
                       u'Н': u'N',
                       u'О': u'O',
                       u'П': u'P',
                       u'Р': u'R',
                       u'С': u'S',
                       u'Т': u'T',
                       u'У': u'U',
                       u'Ф': u'F',
                       u'Х': u'H',
                       u'Ъ': u'',
                       u'Ы': u'Y',
                       u'Ь': u'',
                       u'Э': u'E',}
 
    capital_letters_transliterated_to_multiple_letters = {u'Ж': u'Zh',
                                                          u'Ц': u'Ts',
                                                          u'Ч': u'Ch',
                                                          u'Ш': u'Sh',
                                                          u'Щ': u'Sch',
                                                          u'Ю': u'Yu',
                                                          u'Я': u'Ya',}
 
 
    lower_case_letters = {u'а': u'a',
                       u'б': u'b',
                       u'в': u'v',
                       u'г': u'g',
                       u'д': u'd',
                       u'е': u'e',
                       u'ё': u'e',
                       u'ж': u'zh',
                       u'з': u'z',
                       u'и': u'i',
                       u'й': u'y',
                       u'к': u'k',
                       u'л': u'l',
                       u'м': u'm',
                       u'н': u'n',
                       u'о': u'o',
                       u'п': u'p',
                       u'р': u'r',
                       u'с': u's',
                       u'т': u't',
                       u'у': u'u',
                       u'ф': u'f',
                       u'х': u'h',
                       u'ц': u'ts',
                       u'ч': u'ch',
                       u'ш': u'sh',
                       u'щ': u'sch',
                       u'ъ': u'',
                       u'ы': u'y',
                       u'ь': u'',
                       u'э': u'e',
                       u'ю': u'yu',
                       u'я': u'ya',}
 
    spec_char = [":", ".", ";","|", "/", "\\", "%", "*", "@", "\"","?","!", ",", "&", "^", "$",  "'", "#", "=","<", ">", "[", "]" , "{", "}", "(", ")", "+", " " ]
 
    capital_and_lower_case_letter_pairs = {}
 
    for capital_letter, capital_letter_translit in capital_letters_transliterated_to_multiple_letters.iteritems():
        for lowercase_letter, lowercase_letter_translit in lower_case_letters.iteritems():
            capital_and_lower_case_letter_pairs[u"%s%s" % (capital_letter, lowercase_letter)] = u"%s%s" % (capital_letter_translit, lowercase_letter_translit)
 
    for dictionary in (capital_and_lower_case_letter_pairs, capital_letters, lower_case_letters):
 
        for cyrillic_string, latin_string in dictionary.iteritems():
            string = string.replace(cyrillic_string, latin_string)
 
    for cyrillic_string, latin_string in capital_letters_transliterated_to_multiple_letters.iteritems():
        string = string.replace(cyrillic_string, latin_string.upper())
 
    for char in spec_char:
        string = string.replace(char,"_")

    string = string.split("_")
    while u'' in string:
        string.remove(u'')

    while '' in string:
        string.remove('')

    string = '_'.join(string)

    return string
  
####################################################################################  
  
filterKeyString = [u"для",u"это",u"что",u"и",u"как",u"так",u"уже",u"при",u"быть",
		   u"если",u"тут",u"его",u"все",u"есть",u"либо",u"нам",u"того",u"может",
		   u"этом",u"кто",u"нас",u"по",u"сути",u"потому", u"вас", u"который", u"всех", u"будет", u"ваше", u"имеет", u"вам", u"нельзя", u"хотя", u"тому", u"лет", u"вашей", 
		   u"эти", u"тем", u"тех", u"чем", u"больше", u"вида", u"менее", u"здесь", u"над", u"весь", u"этих", u"нужно", u"под", u"однако", u"этой", u"ведь", u"или", u"ему", u"ради", u"будут", u"только",
		   u"там", u"было", u"том", u"которые", u"чуть", u"вот", u"они", u"можно", u"более", u"были", u"просто", u"всё", u"них", u"своя", u"ничего", u"чтож", u"тот", u"нет", u"где", u"очень", u"про", u"многое", u"собой"] 

####################################################################################  

def searchRepeat(content):
  words = {}
  strip = string.whitespace + string.punctuation + string.digits + "\"'"

  rowList = content.split('\n') 

  for line in rowList:
    for word in line.lower().split():
      word = word.strip(strip)

      if word not in filterKeyString:
        if len(word) > 2:
            words[word] = words.get(word, 0) + 1
			    
  pairs = words.items()
  pairs.sort(key=lambda x: x[1], reverse=True)

  keystring = ""
		
  for p in pairs[:10]:
    keystring = keystring + p[0] +", "

  keystring = keystring[:len(keystring) - 2]
  
  return keystring