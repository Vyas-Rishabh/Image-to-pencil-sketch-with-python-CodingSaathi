#!/usr/bin/env python
# coding: utf-8

# # Image to pencil sketch with python

# In[8]:


# import the library
import cv2
import matplotlib.pyplot as plt


# In[9]:


# get the image file name and location here
img_file = 'bird.jpg'
original_image = cv2.imread(img_file)


# In[10]:


# # Convert BGR image to RGB
original_img_rgb = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)


# In[11]:


# Display the original image
plt.imshow(original_img_rgb)
plt.axis('off')
plt.title('Original Image')
plt.show()


# In[12]:


# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)


# In[13]:


plt.imshow(gray_image)
plt.axis('off')
plt.title('Grayscale Image')
plt.show()


# In[14]:


# Invert the grayscale image
inverted_gray_image = cv2.bitwise_not(gray_image)


# In[16]:


plt.imshow(inverted_gray_image)
plt.axis('off')
plt.title('Inverted Gray Image')
plt.show()


# In[17]:


# Blur the inverted image using the GaussianBlur function
blurred_image = cv2.GaussianBlur(inverted_gray_image, (111, 111), 0)


# In[18]:


plt.imshow(blurred_image)
plt.axis('off')
plt.title('Blurred Image')
plt.show()


# In[19]:


# Invert the blurred image
inverted_blurred_image = cv2.bitwise_not(blurred_image)


# In[20]:


plt.imshow(inverted_blurred_image)
plt.axis('off')
plt.title('Blurred Image')
plt.show()


# In[21]:


# Create the pencil sketch image by dividing the grayscale image by the inverted blurred image
pencil_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)


# In[24]:


plt.imshow(pencil_sketch)
plt.axis('off')
plt.show()


# In[25]:


# Convert pencil sketch to RGB
pencil_sketch_rgb = cv2.cvtColor(pencil_sketch, cv2.COLOR_GRAY2RGB)


# In[26]:


# Display the pencil sketch
plt.imshow(pencil_sketch_rgb)
plt.axis('off')
plt.title('Pencil Sketch')
plt.show()


# You can find this project on <a href="https://github.com/Vyas-Rishabh/Image-to-pencil-sketch-with-python-CodingSaathi"><b>GitHub.</b></a>
