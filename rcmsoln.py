import os
import pandas as pd
import google.generativeai as genai

# Configure API key (replace with your actual key)
API_KEY = "AIzaSyDRl_lDKeGiuzfdxElSCWSgKnfujm0XOdw"  # Replace with your actual API key (if needed)
genai.configure(api_key=API_KEY) # Assuming genai has a configure statement that accepts the key
text_model = genai.GenerativeModel("gemini-pro")

file_path = "D:\\work\\aimlds\\rcm\\solution\\usecase7\\top_usecase7.csv"
output_file_path = "D:\\work\\aimlds\\rcm\\solution\\result.txt"

os.remove(output_file_path)
with open(output_file_path, "w") as output_file:

  # Load DataFrame
  dftop7 = pd.read_csv(file_path)
  dftop7.rename(columns={"Rndrng_Prvdr_City": "City",
                        "Providers_in_city": "Provider",
                        "services_in_city": "Service",
                        "states": "State",
                        "average_medicare_payout": "Medicare_Payout"}, inplace=True)
  
  dftop7_copy = dftop7.copy()  
  # Get the unique count of Providers and Services within each City
  provider_counts = dftop7_copy.groupby(['City'])['Provider'].nunique().reset_index(name='Provider_count')
  service_counts = dftop7_copy.groupby(['City'])['Service'].nunique().reset_index(name='Service_count')

  # Merge the two dataframes to get the final result
  result = pd.merge(provider_counts, service_counts, on='City')

  # Print the result
  #print(result, file=output_file)
  #print('result: {result}', file=output_file)
  prompt = 'Unique Providers are : {provider_counts} and Service counts are : {service_counts}'
  print({prompt}, file=output_file)
# Response generation using genai (replace with your logic)
  chat_session = text_model.start_chat()
# Send the message using the chat session's send_message method
  response_chat = chat_session.send_message(prompt)
  response_text = response_chat.text
  print(response_text, file=output_file)

 # print(f"\nPrompt: {prompt}", file=output_file)
 # print(f"Response: {response_text}", file=output_file)

  # Analyze data by City
  dftop7_groupbyCity = dftop7.groupby("City")

  # Grouped data aggregation (if results are not empty)
  if len(dftop7_groupbyCity) != 0:
    dftop7_groupbyCityAgg = dftop7_groupbyCity.agg({"Provider": "nunique", "Service": "nunique"})
    print("\ndftop7_groupbyCityAgg exists\n", file=output_file)
    #print(dftop7_groupbyCityAgg, file=output_file)
  else:
    print("Warning: 'dftop7_groupbyCity' dataframe might be empty or the dataframe has no entries for grouping by City.", file=output_file)

  # Prompt for analysis (assuming City is a column name)
  #prompt1 = f"In \n {dftop7_groupbyCityAgg} \n, how many unique Providers and Services are available within a specific City?"
  #dftop7

  prompt1 = f"\n In dataframe dftop7, how many unique Providers (Provider_count) and Services are available within a specific City?"
  print(prompt1, file=output_file)
  # Send the message using the chat session's send_message method
  response_chat1 = chat_session.send_message(prompt1)
  response_text1 = response_chat1.text
  print(response_text1, file=output_file)

  print(f"\nPrompt: {prompt1}", file=output_file)
  print(f"Response: {response_text1}", file=output_file)

  # Prompt for analysis (assuming City is a column name)
  #prompt2 = f"Analyze DataFrame /n {dftop7} /n. On average, how much Medicare_Payout is generated?"
  prompt2 = f"In DataFrame {dftop7}, what is average Medicare_Payout?"
  print(prompt2, file=output_file)
  # Send the message using the chat session's send_message method
  response_chat2 = chat_session.send_message(prompt2)
  response_text2 = response_chat2.text
  print(response_text2, file=output_file)

  print(f"\nPrompt: {prompt2}", file=output_file)
  print(f"Response: {response_text1}", file=output_file)

  #prompt3 = f"Analyze DataFrame {dftop7}. Which top cities Providers can consider moving to in order to increase their Medicare_Payout?"
  prompt3 = f"In dataframe {dftop7}, which cities have the highest average Medicare payout?"
  print(prompt3, file=output_file)
  # Send the message using the chat session's send_message method
  response_chat3 = chat_session.send_message(prompt3)
  response_text3 = response_chat3.text
  print(response_text3, file=output_file)

  print(f"\nPrompt: {prompt3}", file=output_file)
  print(f"Response: {response_text3}", file=output_file)