
# coding: utf-8

# ## This program resizes any cropped images into 40x40 pixel images

# In[ ]:


import os
import cv2
import matplotlib.pyplot as plt


# In[2]:


def resizer(image):

    width = 40
    height = 40
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized


# In[3]:


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename), cv2.IMREAD_UNCHANGED)
        if img is not None:
            images.append(img)
    return images


# In[4]:


collection = load_images_from_folder('./a/') 
#collection = load_images_from_folder('your directory here') 


# ## Preview

# In[5]:


collection[0].shape # before resize


# In[6]:


plt.imshow(collection[0]) #before resize


# In[7]:


result = []

for i in range(len(collection)):
    #img = cv2.imread(collection[i], cv2.IMREAD_UNCHANGED)
    output = resizer(collection[i])
    result.append(output)


# ## Preview

# In[10]:


result[0].shape #after resizing


# In[9]:


plt.imshow(result[0]) #after resizing


# In[18]:


print(os.listdir('./'))


# Caution: make the `result` folder first before run cell below. 

# In[19]:


for i in range(len(result)):
    filename = './result/image-'+str(i)+'.jpg'
    cv2.imwrite(filename, result[i])

