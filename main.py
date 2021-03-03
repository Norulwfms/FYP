import streamlit as st
import pandas as pd 

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

st.markdown(
	"""
	<style>
	.main {
	background-colour #F5F5F5 
	}
	</style>
	""",
	unsafe_allow_html=True
	)



with header: 
	st.title('Welcome to Radiology Department')
	st.markdown('Hospital Canselor Tuanku Muhriz (HCTM), Universiti Kebangsaan Malaysia')


with dataset: 
	st.header('CXR')
	st.markdown('* **Source of data:** Open source; OpenI and LUMEN')
	
	cxr_data = pd.read_csv('Data/data.csv')
	st.write(cxr_data.head())

	st.subheader('Atelectasis Disease')
	pulocation_dist = pd.DataFrame(cxr_data['dx'].value_counts()).head(100)
	st.bar_chart(pulocation_dist)

with features: 
	st.header('Atelectasis')

	st.markdown('* **Definition:** It is a condition in which the airways and air sacs in the lung collapse or do not expand properly. It can be happen when there is an airway blockage, or when the pressure outside the lung keeps it from expanding, or when there is not enough surfactant for the lung to expand normally.')
	st.markdown('* **Radiographic findings:** Increased opacity of the affected lung field and loss of volume.')
	st.markdown('* **Mechanism:** Airway obstruction, altered alveolar surface tension and compression of lung tissues. For instance, excess mucus clots, blood stasis or aspirated foreign objects. The gas between the alveoli distal to the obstruction and trapped. It is then absorbed by the pulmonary blood flowing through the area and resulting in alveolar collapsed.')
	st.markdown('* **Type of atelectasis:** Post-obstructive, compressive, dependent or passive and cicatrization.')
	st.markdown('* **Possible causes:** Musuc plugm foreign body aspirated, tumor inside the airway, injury due to chest trauma, pleural effusion, pneumonia, pneumothorax, scarring of lung tissues and deflate lung.')
	st.markdown('* **Symptoms:** Difficulty in breathing, rapid or shallow breathing, wheezing, cough, dyspnea, tachypnea, asymmetric chest movement and reduced breath sounds in the affected lung field.')
	

with model_training: 
	st.header('Preliminary Report')
	st.text('CXR Training Model')

	sel_col, disp_col = st.beta_columns(2)

	input_feature = sel_col.text_input('Indications:')
	input_feature = sel_col.text_input('Findings:')
	input_feature = sel_col.text_input('Impression:')
	input_feature = sel_col.text_input('No of CXR:')

	