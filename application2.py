import streamlit as st
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dummy analysis functions
def analyze_lgr(fits_data):
    st.write("Running analysis for LGR...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGR Analysis completed.")
    st.session_state.form_submitted = False

def analyze_ux(fits_data):
    st.write("Running analysis for UX...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("UX Analysis completed.")
    st.session_state.form_submitted = False

def analyze_uy(fits_data):
    st.write("Running analysis for UY...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("UY Analysis completed.")
    st.session_state.form_submitted = False

def analyze_uz(fits_data):
    st.write("Running analysis for UZ...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("UZ Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lge(fits_data):
    st.write("Running analysis for LGE...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGE Analysis completed.")
    st.session_state.form_submitted = False

def analyze_bx(fits_data):
    st.write("Running analysis for BX...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("BX Analysis completed.")
    st.session_state.form_submitted = False

def analyze_by(fits_data):
    st.write("Running analysis for BY...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("BY Analysis completed.")
    st.session_state.form_submitted = False

def analyze_bz(fits_data):
    st.write("Running analysis for BZ...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("BZ Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lgne(fits_data):
    st.write("Running analysis for LGNE...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGNE Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lgp(fits_data):
    st.write("Running analysis for LGP...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGP Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lgtg(fits_data):
    st.write("Running analysis for LGTG...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGTG Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lgn1(fits_data):
    st.write("Running analysis for LGN1...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGN1 Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lgn2(fits_data):
    st.write("Running analysis for LGN2...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGN2 Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lgn3(fits_data):
    st.write("Running analysis for LGN3...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGN3 Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lgn4(fits_data):
    st.write("Running analysis for LGN4...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGN4 Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lgn5(fits_data):
    st.write("Running analysis for LGN5...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGN5 Analysis completed.")
    st.session_state.form_submitted = False

def analyze_lgn6(fits_data):
    st.write("Running analysis for LGN6...")
    st.write('Plotting Output')

    # geeting  the index of each coordinate
    x_indices = [round(float(fits_data[0].header['CRVAL1']) + i * fits_data[0].header['CDELT1'], 6) for i in range(fits_data[0].header['NAXIS1'])]
    y_indices = [round(float(fits_data[0].header['CRVAL2']) + i * fits_data[0].header['CDELT2'], 6) for i in range(fits_data[0].header['NAXIS2'])]
    z_index = lst.index(z_value)


    value_to_find_x1 = x_start_value  # Replace with your value
    x_start = x_indices.index(value_to_find_x1)
    #st.write(f"The value {value_to_find_x1} is at index {x_start}.")

    value_to_find_x2 = x_end_value  # Replace with your value
    x_end = x_indices.index(value_to_find_x2)
    #st.write(f"The value {value_to_find_x2} is at index {x_end}.")

    value_to_find_y1 = y_start_value  # Replace with your value
    y_start = y_indices.index(value_to_find_y1)
    #st.write(f"The value {value_to_find_y1} is at index {y_start}.")

    value_to_find_y2 = y_end_value  # Replace with your value
    y_end = y_indices.index(value_to_find_y2)
    #st.write(f"The value {value_to_find_y2} is at index {y_end}.")


    st.write(f"Analysis of Quantity on Z value : {z_value} Mm , X range from : {x_start_value} Mm to {x_end_value} Mm and Y range from : {y_start_value} Mm to {y_end_value} Mm")

    # Plotting the data
    fig, ax = plt.subplots(1, 2, figsize=(20, 10), dpi=800)
    fig_1, ax_1 = plt.subplots(figsize=(10, 8), dpi=800)
    im_1 = ax_1.imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation='bilinear')
    fig_1.colorbar(im_1, ax=ax_1, label='Quantity (units in header)')
    ax_1.set_title(f"Quantity at z = {z_value} Mm")
    ax_1.set_xlabel("x-axis")
    ax_1.set_ylabel("y-axis")


    # Full plot
    ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap, interpolation = 'bilinear')
    ax[0].set_title(f"Full Plot: Quantity at z = {z_value} Mm")
    ax[0].set_xlabel("x-axis")
    ax[0].set_ylabel("y-axis")
    fig.colorbar(ax[0].imshow(xy_data[z_index, :, :], origin='lower', cmap = selected_cmap), ax=ax[0], label='Quantity (units in header)')

    # Highlight the zoomed-in region on the full plot
    rect = patches.Rectangle(
        (x_start, y_start),  # Bottom-left corner of the rectangle
        x_end - x_start,  # Width
        y_end - y_start,  # Height
        linewidth=2,
        edgecolor='cyan',
        facecolor='none',
    )
    ax[0].add_patch(rect)

    # Zoomed-in region plot
    zoomed_data = xy_data[z_index, y_start:y_end, x_start:x_end]
    ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap, interpolation='bilinear')
    ax[1].set_title(f"Zoomed-In Region: x=({x_start_value}, {x_end_value}), y=({y_start_value}, {y_end_value})")
    ax[1].set_xlabel("x-axis (zoomed)")
    ax[1].set_ylabel("y-axis (zoomed)")
    fig.colorbar(ax[1].imshow(zoomed_data, origin='lower', cmap = selected_cmap), ax=ax[1], label='Quantity (units in header)')

    # Display the plot in Streamlit and print Basic Analysis
    st.pyplot(fig)
    st.markdown(f"Quantity at **-----({x_start_value},{y_start_value}) is {xy_data[z_index,y_start,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_start_value},{y_end_value}) is {xy_data[z_index,y_end,x_start]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_start_value}) is {xy_data[z_index,y_start,x_end]} UNITS---** ")
    st.markdown(f"Quantity at **-----({x_end_value},{y_end_value}) is {xy_data[z_index,y_end,x_end]} UNITS---** ")
    st.markdown(f"<p style='text-align: center;'>The min value in whole plane at {z_value} is  {np.min(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value in whole plane at {z_value} is  {np.max(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value in whole plane at {z_value} is  {np.mean(xy_data[z_index,:,:])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The min value of selected part  is  {np.min(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The max value of selected part  is  {np.max(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>The mean value of selected part  is  {np.mean(xy_data[z_index, y_start:y_end, x_start:x_end])}</p>", unsafe_allow_html=True)
    st.markdown(f"<u>Plot at z =  {z_value} without annotations </u>", unsafe_allow_html=True)
    st.pyplot(fig_1)
    st.write("LGN6 Analysis completed.")
    st.session_state.form_submitted = False



if __name__ == '__main__':
    # Dictionary of file name options and corresponding analysis functions
    analysis_functions = {
    "lgr" : analyze_lgr,
    "ux"  : analyze_ux,
    "uy"  : analyze_uy,
    "uz"  : analyze_uz,
    "lge" : analyze_lge,
    "bx"  : analyze_bx, 
    "by"  : analyze_by,
    "bz"  : analyze_bz,
    "lgne": analyze_lgne,
    "lgp" : analyze_lgp,
    "lgtg": analyze_lgtg,
    "lgn1": analyze_lgn1,
    "lgn2": analyze_lgn2,
    "lgn3": analyze_lgn3,
    "lgn4": analyze_lgn4,
    "lgn5": analyze_lgn5,
    "lgn6": analyze_lgn6
    }

    # Streamlit App
    st.title("Bi_Frost File Analysis")

    st.markdown("**IMPORTANT**  If any error are encountered press ----> R")

    st.markdown('<a href="https://sdc.uio.no/search/simulations?sim=en024048_hion&prod=%2Clgr%2Cux%2Cuy%2Cuz%2Clge%2Cbx%2Cby%2Cbz%2Clgne%2Clgp%2Clgtg%2Clgn1%2Clgn2%2Clgn3%2Clgn4%2Clgn5%2Clgn6&step_start=385&step_stop=385&step_stride=1" target="_blank">Download your Bifrost file from this link Only</a>', unsafe_allow_html=True)
    st.write('lgr  :	log10(mass density)')
    st.write('ux :	bulk velocity in x')
    st.write('uy :	bulk velocity in y')
    st.write('uz :	bulk velocity in z')
    st.write('lge :	log10(internal energy)')
    st.write('bx :	magnetic field strength in x')
    st.write('by :	magnetic field strength in y')
    st.write('bz :	magnetic field strength in z')
    st.write('lgne :	log10(electron density)')
    st.write('lgp :	log10(gas pressure)')
    st.write('lgtg :	log10(temperature)')
    st.write('lgn1 :	log10(population density in ground state of hydrogen)')
    st.write('lgn2 :	log10(population density in n=2 state of hydrogen)')
    st.write('lgn3 :	log10(population density in n=3 state of hydrogen)')
    st.write('lgn4 :	log10(population density in n=4 state of hydrogen)')
    st.write('lgn5 :	log10(population density in n=4 state of hydrogen)')
    st.write('lgn6 :	log10(population density of protons)')
    

    # Upload FITS file
    uploaded_file = st.file_uploader("Upload your FITS file", type=["fits"])


    if uploaded_file:
        # Read the FITS file
        fits_data = fits.open(uploaded_file)
        xy_data = fits_data[0].data
        z_coords = fits_data[1].data
        lst = z_coords.tolist()
        file_name = uploaded_file.name.split('.')[0]
        st.write(f"File uploaded: {file_name}.fits")

        if "form_submitted" not in st.session_state:
            st.session_state.form_submitted = False
        
        if "z_value" not in st.session_state:
            st.session_state.z_value = 0.01893768087029457
        if "x_start_value" not in st.session_state:
            st.session_state.x_start_value = 0.619047
        if "x_end_value" not in st.session_state:
            st.session_state.x_end_value = 1.047618
        if "y_start_value" not in st.session_state:
            st.session_state.y_start_value = 0.619047
        if "y_end_value" not in st.session_state:
            st.session_state.y_end_value = 1.047618
        if "selected_cmap" not in st.session_state:
            st.session_state.selected_cmap = 'inferno'



        with st.form("slider_form"):
            cmap_options = ['magma', 'inferno', 'plasma', 'viridis', 'cividis', 'twilight', 'twilight_shifted', 'turbo', 'Blues', 'BrBG', 'BuGn', 'BuPu', 'CMRmap', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PRGn', 'PiYG', 'PuBu', 'PuBuGn', 'PuOr', 'PuRd', 'Purples', 'RdBu', 'RdGy', 'RdPu', 'RdYlBu', 'RdYlGn', 'Reds', 'Spectral', 'Wistia', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd', 'afmhot', 'autumn', 'binary', 'bone', 'brg', 'bwr', 'cool', 'coolwarm', 'copper', 'cubehelix', 'flag', 'gist_earth', 'gist_gray', 'gist_heat', 'gist_ncar', 'gist_rainbow', 'gist_stern', 'gist_yarg', 'gnuplot', 'gnuplot2', 'gray', 'hot', 'hsv', 'jet', 'nipy_spectral', 'ocean', 'pink', 'prism', 'rainbow', 'seismic', 'spring', 'summer', 'terrain', 'winter', 'Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b', 'tab20c', 'magma_r', 'inferno_r', 'plasma_r', 'viridis_r', 'cividis_r', 'twilight_r', 'twilight_shifted_r', 'turbo_r', 'Blues_r', 'BrBG_r', 'BuGn_r', 'BuPu_r', 'CMRmap_r', 'GnBu_r', 'Greens_r', 'Greys_r', 'OrRd_r', 'Oranges_r', 'PRGn_r', 'PiYG_r', 'PuBu_r', 'PuBuGn_r', 'PuOr_r', 'PuRd_r', 'Purples_r', 'RdBu_r', 'RdGy_r', 'RdPu_r', 'RdYlBu_r', 'RdYlGn_r', 'Reds_r', 'Spectral_r', 'Wistia_r', 'YlGn_r', 'YlGnBu_r', 'YlOrBr_r', 'YlOrRd_r', 'afmhot_r', 'autumn_r', 'binary_r', 'bone_r', 'brg_r', 'bwr_r', 'cool_r', 'coolwarm_r', 'copper_r', 'cubehelix_r', 'flag_r', 'gist_earth_r', 'gist_gray_r', 'gist_heat_r', 'gist_ncar_r', 'gist_rainbow_r', 'gist_stern_r', 'gist_yarg_r', 'gnuplot_r', 'gnuplot2_r', 'gray_r', 'hot_r', 'hsv_r', 'jet_r', 'nipy_spectral_r', 'ocean_r', 'pink_r', 'prism_r', 'rainbow_r', 'seismic_r', 'spring_r', 'summer_r', 'terrain_r', 'winter_r', 'Accent_r', 'Dark2_r', 'Paired_r', 'Pastel1_r', 'Pastel2_r', 'Set1_r', 'Set2_r', 'Set3_r', 'tab10_r', 'tab20_r', 'tab20b_r', 'tab20c_r']
            selected_cmap = st.selectbox("Select Colormap", cmap_options, index = cmap_options.index(st.session_state.selected_cmap))            
            z_value =       st.select_slider("Select z-position", options = lst, value = st.session_state.z_value)
            # Sliders for x and y range
            x_start_value = st.slider("X-axis Start",   min_value = float(fits_data[0].header['CRVAL1']),           max_value = float(fits_data[0].header['CRVAL1'] + (fits_data[0].header['NAXIS1'] -1)*(fits_data[0].header['CDELT1']))           , step = fits_data[0].header['CDELT1'] , format = "%.6f" , value = st.session_state.x_start_value)
            x_end_value   = st.slider("X-axis End",     min_value = float(fits_data[0].header['CRVAL1']),           max_value = float(fits_data[0].header['CRVAL1'] + (fits_data[0].header['NAXIS1'] -1)*(fits_data[0].header['CDELT1']))           , step = fits_data[0].header['CDELT1'] , format = "%.6f" , value = st.session_state.x_end_value)
            y_start_value = st.slider("Y-axis Start",   min_value = float(fits_data[0].header['CRVAL2']),           max_value = float(fits_data[0].header['CRVAL2'] + (fits_data[0].header['NAXIS2'] -1)*(fits_data[0].header['CDELT2']))           , step = fits_data[0].header['CDELT2'] , format = "%.6f" , value = st.session_state.y_start_value)
            y_end_value   = st.slider("Y-axis End",     min_value = float(fits_data[0].header['CRVAL2']),           max_value = float(fits_data[0].header['CRVAL2'] + (fits_data[0].header['NAXIS2'] -1)*(fits_data[0].header['CDELT2']))           , step = fits_data[0].header['CDELT2'] , format = "%.6f" , value = st.session_state.y_end_value)
            #analysis_option = st.selectbox(f"Select analysis for {file_name}.fits", ["Run Analysis"])
            if x_start_value >= x_end_value or y_start_value >= y_end_value:
                st.write('Please keep x2 > x1 or y2 > y1 or plot will be Blank')
            submitted = st.form_submit_button("Run Analysis")
        
        
      
        # Show dropdown with options based on file name (e.g., bz, ux, uy, uz)
        for key in analysis_functions:
            if key in file_name:
                st.markdown(f" {key} :  **Found your file related quantity** , Please Run the Analysis")
                # Run analysis when button is clicked
                # if st.button("Run Analysis"):
                analysis_function = analysis_functions[key]
                #analysis_function(fits_data)  # Call the selected analysis function
                break
            else:
                #st.write(f' {key} :  not your file related quantity, Searching Please wait')
                continue
    
        if submitted:
            st.session_state.form_submitted = True

        if st.session_state.form_submitted:
            st.session_state.z_value = z_value
            st.session_state.x_start_value = x_start_value
            st.session_state.x_end_value = x_end_value
            st.session_state.y_start_value = y_start_value
            st.session_state.y_end_value = y_end_value
            st.session_state.selected_cmap = selected_cmap
            if 'lg' in key:
                xy_data = 10 ** xy_data
                analysis_function(fits_data)
            else:    
                analysis_function(fits_data)  
        else:
            st.markdown("press **'Run Analysis'** above")
        st.markdown("**TO RERUN ANALYSIS PRESS BELOW, ADJUST NEW VALUES IN SLIDER, THEN PRESS **'RUN ANLYSIS'** AGAIN**")
        if st.button('RE RUN  ANALYSIS'):
            st.session_state.z_value = z_value
            st.session_state.x_start_value = x_start_value
            st.session_state.x_end_value = x_end_value
            st.session_state.y_start_value = y_start_value
            st.session_state.y_end_value = y_end_value
            st.session_state.selected_cmap = selected_cmap
            st.rerun()
    st.write('If you want to Clear the Screen , or see any error in your results ,press Below Button')
    if st.button("Press to clear the Plots/Reset_Form"):
        st.session_state.z_value = 0.01893768087029457
        st.session_state.x_start_value = 0.619047
        st.session_state.x_end_value = 1.047618
        st.session_state.y_start_value = 0.619047
        st.session_state.y_end_value = 1.047618
        st.session_state.selected_cmap = 'inferno'
        st.session_state.form_submitted = False
        st.rerun()