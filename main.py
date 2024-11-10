from psd_tools import PSDImage
import warnings
from PIL import Image



#to supress warnings from psd_tools because of newer PS version (files)
warnings.filterwarnings("ignore", category=UserWarning, module="psd_tools")

#Loading the PSD
selected_image = PSDImage.open('house_example.psd')
#selected_image.composite().save('house_example_output.png')

#for layer in selected_image:
#    print(layer)
#    layer_image = layer.composite()

for index, layer in enumerate(selected_image):
    print(f'Index: {index}; Layer: {layer}')

