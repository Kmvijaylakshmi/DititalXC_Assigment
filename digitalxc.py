# -*- coding: utf-8 -*-
"""DigitalXC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CaOc7n5u7t0FrEmsUDqvSsuCF7p76iyC

You will write a python code (preferable) / Java/JavaScript to do the following

a. Read the data from the sheet Input-Data file from the attachment (attached at the bottom)

b. Browse through all the rows under the heading Additional comments (Or comments and
worknotes)

c. Identify the line that says Groups : [code]&lt;I&gt;XXXX &lt;/I&gt;[/code]

d. List all the groups. More than group could be separated by commas

e. Your output should be a list of all the groups, along with the number of occurrences

f. Given below is your sample output (can be a simple text file)

    Group_name                                              Number of occurrences

    Huntingdon and Liz area                                   2

    SML Group GMs                                             1

    Eastend GMs                                               3
"""

import pandas as pd

df = pd.read_excel('/content/coding challenge test.xlsx')
print(df)

df.head()

df.shape

comments = df['Additional comments'].tolist() + df['Comments and Work notes'].tolist()

comments[0]

count = 0
for comment in comments:
  count += comment.count('Groups : [code]<I>SML Group GMs</I>[/code]')
print("The group '[code]<I>XXXX </I>[/code]' occurs",count,"times in the comments.")

df_new = df['Additional comments'].str.split(pat='\n', expand=True)

df_new.groupby([9]).size()

df_grp = df['Additional comments'].apply(lambda st: st[st.find("[code]<I>")+9:st.find("</I>[/code]")])
df_grp1 = df_grp.str.split(pat=',',expand=True).stack().str.strip()

def num_of_occurences(df):
  df_grp = df['Additional comments'].apply(lambda st: st[st.find("[code]<I>")+9:st.find("</I>[/code]")])
  df_grp = df_grp.str.split(pat=',',expand=True).stack().str.strip()
  print(df_grp.value_counts().rename_axis('Group_name').to_frame('Number of occurrences'))

num_of_occurences(df)

