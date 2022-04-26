# All the installs and imports needed for the word cloud script and uploader widget

!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

# This is the uploader widget that allows you upload a text file. N.B: Only text files are allowed as shown in the encoding in line 25

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

    
    
_upload()

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words that were used to process the text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "in", "for", "not", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    file_contents_dict = {}
    file_contents_lower = file_contents.lower()
    file_contents_temp_list = file_contents_lower.split()
    file_contents_list = list()
    
    
    for item in file_contents_temp_list: #checking if the item is an alphabet and removing the ones that aren't
        if item.isalpha():
            file_contents_list.append(item)
            
            
    for item in file_contents_list:
        if item not in uninteresting_words:
            if item not in file_contents_dict.keys():
                file_contents_dict[item] = 1
            else:
                file_contents_dict[item] += 1
                
#         else:
#         for word in uninteresting_words:
#             if word in file_contents_list:
#                 file_contents_list.remove(word)
                
#     for word in file_contents_list:
#         if word not in file_contents_dict.keys():
#                 file_contents_dict[word] = 1
#         elif word in files_content_dict.keys():
#                 file_contents_dict[word] += 1
                
                

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(file_contents_dict)
    return cloud.to_array()
    print(file_contents_dict)
    
# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
