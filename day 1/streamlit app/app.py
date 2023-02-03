
# import module
import streamlit as st

# Title
st.title("Welcome to Nilay's Home page  !!!")

# Header
st.header("This is a header")
 
# Subheader
st.subheader("This is a subheader")

# Text
st.text("Hello Digital Regensys!!!")


# Markdown
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("### This is a markdown")


#Success, Info, Warning, Error, Exception:

# success
st.success("Success")
 
# success
st.info("Information")
 
# success
st.warning("Warning")
 
# success
st.error("Error")

 
#Using write function, we can also display code in coding format. This is not possible using st.text(”).

# Write text
st.text("range(10)")

st.write("Text with write")
 
# Writing python inbuilt function range()
st.write(range(10))



# Display Images
 
# import Image from pillow to open images
from PIL import Image
img = Image.open("car.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img,width=50)


#A checkbox returns a boolean value. When the box is checked, it returns a True value else returns a False value.

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'

x=st.checkbox("I Agree")
if x:
    # display the text if the checkbox returns True value
    st.text("User have acepted the conditions")


    
# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
gender = st.radio("Select Gender: ", ('Male', 'Female','Third Gender'))
 
# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (gender == 'Male'):
    st.success("Male")
elif gender == 'Female':
    st.success("Female")
else:
    st.success("Third Gender")


# Selection box
 
# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
 
# print the selected hobby
st.write("Your hobby is: ", hobby)

# multi select box
 
# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])
 
# write the selected options
st.write("You selected", len(hobbies), 'hobbies')
st.write("You selected", hobbies)

#st.button() returns a boolean value. It returns a True value when clicked else returns False.

# Create a simple button that does nothing
submit_btn=st.button("Submit")
 
# Create a button, that when clicked, shows a text
if(submit_btn):
    st.text("User has submitted the data.")


# Text Input
 
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name")
 
# display the name when the submit button is clicked
# .title() is used to get the input text string
z=st.button("Submit name")
if(z):
    result ="your name is "+name.title()
    st.success(result)


# slider
 
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
age = st.slider("Select car age", 10, 200)
 
# print the level
# format() is used to print value
# of a variable at a specific position
y=st.button("Submit car age")
if(y):
    st.success('Selected age: '+str(age))
