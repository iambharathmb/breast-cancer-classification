import numpy as np
import streamlit as st
import keras

# load the saved model
model = keras.models.load_model("beast-cancer-model.h5")
    
# creating a function for prediction
def beast_cancer_prediction(input_data):
   
    # changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

    # Prediction
    prediction = model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0] == 0):
        return 'The Tumor is Malignant'
    else:
        return 'The Person is Benign'
    
def main():
    # giving a title
    st.title("Beast Cancer Classification Web App")
    
    # getting the input data from users
    mean_radius = st.text_input (" Mean Radius ")
    mean_texture = st.text_input (" Mean Texture")
    mean_perimeter = st.text_input (" Mean Perimeter ")
    mean_area = st.text_input (" Mean Area ")
    mean_smoothness = st.text_input (" Mean Somoothness ")
    mean_compactness = st.text_input (" Mean Compactness ")
    mean_concavity = st.text_input (" Mean Concavity ")
    mean_concave_points = st.text_input (" Mean Concave Points ")
    mean_symmetry = st.text_input (" Mean Symmetry ")
    mean_fractal_dimension = st.text_input (" Mean Fractal Dimension")
    radius_error = st.text_input (" Radius Error")
    texture_error = st.text_input (" Texture Error ")
    perimeter_error = st.text_input (" Perimeter Error ")
    area_error = st.text_input (" Area Error ")
    smoothness_error = st.text_input (" Smoothness Error ")
    compactness_error = st.text_input ("Compactness Error ")
    concavity_error = st.text_input (" Concavity Error ")
    concave_points_error = st.text_input (" Concave Points Error ")
    symmetry_error = st.text_input (" Symmerty Error ")
    fractal_dimension_error = st.text_input (" Fractry Dimention Error ")
    worst_radius = st.text_input (" Worst Radius ")
    worst_texture = st.text_input (" Worst Texture ")
    worst_perimeter = st.text_input (" Worst Perimeter ")
    worst_area = st.text_input (" Worst Area ")
    worst_smoothness = st.text_input (" Worst Smoothness ")
    worst_compactness = st.text_input (" Worst Compactness ")
    worst_concavity = st.text_input (" Worst Concavitity ")
    worst_concave_points = st.text_input (" Worst Concave Points ")
    worst_symmetry = st.text_input (" Worst Symmetry")
    worst_fractal_dimension = st.text_input (" Worst Fractal Dimension ")
    
    # code for prediction
    predication = ''
    
    # craeting button for prediction
    if st.button('Result'):
        prediction = beast_cancer_prediction([
            mean_radius,
            mean_texture,
            mean_perimeter,
            mean_area,
            mean_smoothness,
            mean_compactness,
            mean_concavity,
            mean_concave_points,
            mean_symmetry,
            mean_fractal_dimension,
            radius_error,
            texture_error,
            perimeter_error,
            area_error,
            smoothness_error,
            compactness_error,
            concavity_error,
            concave_points_error,
            symmetry_error,
            fractal_dimension_error,
            worst_radius,
            worst_texture,
            worst_perimeter,
            worst_area,
            worst_smoothness,
            worst_compactness,
            worst_concavity,
            worst_concave_points,
            worst_symmetry,
            worst_fractal_dimension
        ])
        
    st.success(prediction)
            
if __name__ == '__main__':
    main()