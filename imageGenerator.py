print("Welcome to Nekix's final project!")
print("This program will help you to create images through OpenAI API.")

# Importing the necessary libraries
import openai

# Setting the API key (You can get your own API key FREE from OpenAI website [URL: https://platform.openai.com/account/api-keys])
openai.api_key = "" # Enter your API key here

# Asking the user to input the prompt
PROMPT = input("Please enter the prompt: ")

# Asking the user to input the image size
print("Image Size Options:")
print("1) 256x256")
print("2) 512x512")
print("3) 1024x1024")

imageSize = int(input("Please enter the image size (1, 2, 3): ")) # Asking the user to input the image size using the options provided

if imageSize == 1:
    imageSize = "256x256"
elif imageSize == 2:
    imageSize = "512x512"
elif imageSize == 3:
    imageSize = "1024x1024"
else:
    print("Invalid image size. Please try again.")
    exit()

print("Creating the image...")

# Asking OpenAI to complete the prompt
response = openai.images.generate( # Creating an image using the OpenAI API
    model="dall-e-2" , # The model that will be used to generate the image
    prompt=PROMPT, # The prompt that the user entered
    n=1, # Number of images to generate
    size=imageSize, # The size of the image
    quality="standard" # The quality of the image
)

# Final result
print("Image created successfully!") 
print(f"Image URL: {response.data[0].url}") # Printing the URL of the image
