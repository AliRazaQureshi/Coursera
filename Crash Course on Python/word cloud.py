# Here are all the installs and imports you will need for your word cloud script and uploader widget
!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import io
import sys


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", \
                           "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                           "been", "being", \
                           "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when",
                           "where", "how", \
                           "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very",
                           "can", "will", "just"]

    # LEARNER CODE START HERE
    file_contents = file_contents.split()
    # removing uninteresting words
    Clean_file = []
    for content in file_contents:
        if content.lower() not in uninteresting_words:
            Clean_file.append(content)

    # removing puntuations
    new_file_contents = []
    for content in Clean_file:
        content = list(content)
        for char in content:
            if char in punctuations:
                content.remove(char)
        new_file_contents.append(''.join(content))

    # converting file contents list to dictionary
    dict_file_contents = {}
    for word in new_file_contents:
        if word in dict_file_contents:
            dict_file_contents[word] += 1
        else:
            dict_file_contents[word] = 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(dict_file_contents)
    return cloud.to_array()

# Display your wordcloud image
file_contents = "If your word cloud image did not appear, go back and rework your `calculate_frequencies` function until you get the desired output.  Definitely check that you passed your frequecy count dictionary into the `generate_from_frequencies` function of `wordcloud`. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!"
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()