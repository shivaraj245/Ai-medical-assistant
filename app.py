# importing neccseary modules
import streamlit as st
from pathlib import Path
import google.generativeai as genai


from dotenv import load_dotenv
load_dotenv()

#from apikey import api_key1
# set the page configuration
api_key1 = os.getenv('api_key1')
st.set_page_config(page_title="VitalImage Analytics", page_icon=":robot:")

# config gemini api key
genai.configure(api_key=api_key1)

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 1,
  "top_k": 32,
  "max_output_tokens": 8192,
}

# saftey setting  

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]


system_prompt="""

 As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for renowed hospital .Your expertise is crucial in  identifying any anomolies ,diseases ,or health issues 



 Your Responsibilities include :
1.Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal find

2.Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings

 3.Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including future test or treatments  that are required


 4.Treatment Suggestions: If appropriate, recommend possible treatment options or intervention

 Important Notes: You should respond only when human medical image provided if not respond with "INVALID IMAGE, PLS PROVIDE MEDICAL IMAGE".

 1.Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain ascepts are "unable to determine based on provided iamge"
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decision.


4.Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis  ,adhering to strucre approach ouline above


Please provide me an output with these 4 heading 1)detailed analysis ,2)Findings Report 3)Recommendations and Next Steps 4)Treatment Suggestions


"""

# model configaration 
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)


#set the logo

#set the logo
st.image(r"ai-assistant--that--looks-like--nurse.png", width=150)

#set the title

st.title(" Ai 🤖 Medical Assistant 👨‍⚕⚕️👩‍⚕")

#set the subtitle

st.subheader("An application that can help users to identify medical images")


uploaded_file = st.file_uploader("Upload the medical image for analysis", type=["png", "jpg" , "jpeg"])
if uploaded_file:
    # displaying image 
    st.image(uploaded_file,width=250, caption="Uploaded  medical image")
submit_button=st.button("Generate Analysis")

if submit_button:
    image_data=uploaded_file.getvalue()


    # making image ready
    image_parts = [
           {
             "mime_type": "image/jpeg",
            "data": image_data
            },

            ]
    

    # making inbuilt promt ready
    prompt_parts = [    
       
          image_parts[0],
          system_prompt,
     ]
    
    st.title("Here is the analysis based on image that is")
    # genarating reponse
    response= model.generate_content(prompt_parts)
    st.write(response.text)

   
