import numpy as np
import matplotlib.pyplot as plt

# Parameters for the image size
height = 100
width = 200

# Generate an image with random RGB values
random_image = np.random.rand(height, width, 3)

# Display the generated random image
plt.imshow(random_image)
plt.title("Random RGB Image")
plt.axis('off')  # Hide axis
#plt.show()

# Create gradient mask with (1,200,1)
array = np.arange(1,0,-0.005)
array = array.reshape(1,200,1)
print(array)

gradient_image = array * random_image
plt.imshow(gradient_image)
plt.title("Random RGB Image with gradient")
plt.axis('off')  # Hide axis
#plt.show()


y_center, x_center = height // 2, width // 2

y,x = np.ogrid[:height, :width]
distance_from_center = np.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)
distance_from_center = distance_from_center / 50
print(x_center, "and", y_center)
distance_from_center = np.where(distance_from_center == 0,1,distance_from_center)
distance_from_center = distance_from_center ** -1
print(distance_from_center[0,0])
distance_from_center = distance_from_center.reshape(100,200,1)
vignette = distance_from_center * random_image
plt.imshow(vignette)
plt.title("Vignette")
plt.axis('off')
plt.show()