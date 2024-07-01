import streamlit as st

def option_menu(menu_title, options, icons, menu_icon, default_index=0, orientation="horizontal", 
               styles=None, menu_dims=None, overwrite=False):
    """
    This function creates a Streamlit option menu.
    
    Parameters:
    menu_title (str): The title of the option menu.
    options (list): A list of option names.
    icons (list): A list of icons corresponding to each option.
    menu_icon (str): The icon for the menu.
    default_index (int): The index of the default selected option.
    orientation (str): The orientation of the menu, either "horizontal" or "vertical".
    styles (dict): A dictionary of custom styles for the menu.
    menu_dims (tuple): A tuple of dimensions for the menu.
    overwrite (bool): Whether to overwrite the existing menu.
    
    Returns:
    selected (str): The selected option.
    """
    selected = st.selectbox(
        menu_title,
        options,
        index=default_index,
        format_func=lambda x: f"{icons[options.index(x)]} {x}",
    )
    return selected

