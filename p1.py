from PIL import Image
image=Image.open('b3.png')
print(f"original size:{image.size}")
newb3=image.resize((1150,80))
newb3.save('newb3.png')