import streamlit as st
import time
from PIL import Image


st.title('ろろログ')

st.write('DataFrame')


"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration')
    bar.progress(i + 1) 
    time.sleep(0.2)

'なみだいすき!!'



# graph = graphviz.Digraph()
# graph.edge('run', 'intr')
# graph.edge('intr', 'runbl')
# graph.edge('runbl', 'run')
# st.graphviz_chart(graph)

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69, 139.64],
#     columns=['lat','lon'],
# )
#st.bar_chart(df)
#st.area_chart(df)

# st.map(df)
# st.table(df.style.highlight_max(axis=0))

# if st.checkbox('Show Image'):
#     img = Image.open('sampleimg.jpg')
#     st.image(img, caption='Sample', use_column_width=True)
l_col, r_col = st.columns(2)
button = l_col.button('Push')
if button:
    r_col.write('Come over her')
expander = st.expander('Enquiry')
expander.write("内容をどうぞ")


op = st.slider("how are u?", 0,100,50)
#op = st.text_input('あなたの趣味は？')

# op = st.selectbox(
#     "What's your favorite number",
#     list(range(1,11))
# )

op, 'ですね。'

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """
