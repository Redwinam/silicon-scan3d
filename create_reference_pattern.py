import numpy as np
import cv2

# A4 size in pixels at 300 DPI
width = int(8.27 * 300)  # A4 width in inches * 300 DPI
height = int(11.69 * 300)  # A4 height in inches * 300 DPI

# Create a white background
img = np.ones((height, width), dtype=np.uint8) * 255

# Function to draw random dots
def draw_random_dots(img, num_dots, min_radius, max_radius):
    for _ in range(num_dots):
        x = np.random.randint(max_radius, width - max_radius)
        y = np.random.randint(max_radius, height - max_radius)
        radius = np.random.randint(min_radius, max_radius)
        cv2.circle(img, (x, y), radius, 0, -1)

# Function to draw random triangles
def draw_random_triangles(img, num_triangles, min_size, max_size):
    for _ in range(num_triangles):
        center_x = np.random.randint(max_size, width - max_size)
        center_y = np.random.randint(max_size, height - max_size)
        size = np.random.randint(min_size, max_size)
        
        pts = np.array([
            [center_x, center_y - size],
            [center_x - size, center_y + size],
            [center_x + size, center_y + size]
        ], np.int32)
        
        cv2.fillPoly(img, [pts], 0)

# Draw reference markers in corners
margin = 100
cv2.rectangle(img, (margin, margin), (margin + 100, margin + 100), 0, -1)
cv2.rectangle(img, (width - margin - 100, margin), (width - margin, margin + 100), 0, -1)
cv2.rectangle(img, (margin, height - margin - 100), (margin + 100, height - margin), 0, -1)
cv2.rectangle(img, (width - margin - 100, height - margin - 100), (width - margin, height - margin), 0, -1)

# Draw patterns
draw_random_dots(img, 300, 3, 8)  # Small dots
draw_random_dots(img, 100, 10, 20)  # Medium dots
draw_random_triangles(img, 50, 20, 40)  # Random triangles

# Add some text for scale reference
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'A4 Reference Pattern', (width//2 - 200, 50), font, 1.5, 0, 2)
cv2.putText(img, 'Place object in center', (width//2 - 150, height//2), font, 1, 0, 2)

# Save the image
cv2.imwrite('reference_pattern.png', img)
