# DogTeethAge

The most practical method for estimating dog age is by the examination of his teeth. Unfortunately, human's accuracy of this method decreases sharply after a dog reaches its adulthood. The permanent (adult) teeth are usually all visible by 6 months and after that, the age assessment depends only on the general state of the teeth and gingiva  (tooth wear, cementum, and pulp cavity). Variations in diets, behavior, genetics, as well as diseases and trauma, can all influence those factors and introduce an "uncertainty" that is increasing with ageing.

We hope that with the appropriate database, Deep Learning will be able to provide a more objective estimation of teeth age. 

This is **open research** which means that we are providing both the dataset and the code **before** publishing the paper. If you would like to contribute to this project you can do that through this GitHub page or you can contact us through the email.


## The Data

In the [data directory](https://github.com/department-of-vet-pathology-unizg/dog_age/tree/master/data), we provided maxillas and mandibles images of 44 dogs together with their masks. The [data.csv](https://github.com/department-of-vet-pathology-unizg/dog_age/blob/master/data/Data.csv) file contains the age of every dog. All the data is, of course, anonymized.

The number of images in the database will increase over time


## Image Preprocessing

Raw images have a size of 6000X4000px (24MP), which is too large for a neural network. One way to reduce the image size, while still keeping (most of) the data, is to extract only the teeth from every image. We decided to use masks to extract this data and create "mozaics" - images that contain both the maxilla's and mandible's teeth. 

You can use the mozaics.py file to parse the images and create more suitable training data.
