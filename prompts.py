import pandas as p
import random
import streamlit as st
import streamlit_ext as ste
from tabulate import tabulate

cell_groups = ["Rock Guitar", "Maracas", "Drums", "DJ Board", "Kalimba", 
               "Recorders", "Uke", "Bongos", "Harp", "Tambourines"]
prompts = [
           "Prompt 1",
           "Prompt 2",
           "Prompt 3",
           "Prompt 4",
           "Prompt 5",
           "Prompt 6",
           "Prompt 7",
           "Prompt 8",
           "Prompt 9",
           "Prompt 10"
        ]

top_level_container = st.container()
info_container = st.container()
bottom_container = st.container()

def show_tables():
    cell_groups_df = p.DataFrame(cell_groups)
    cell_groups_df.columns = ["Cell Groups"]

    prompts_df = p.DataFrame(prompts)
    prompts_df.columns = ["Prompts"]

        
    c1,c2 = info_container.columns([1,3])
    with c1:            
        cg_str = ''
        st.markdown("### Cell Groups")
        for group in cell_groups:
            cg_str += f'- {group}\n'
        st.markdown(cg_str)
    with c2:
        prompts_str = ''
        st.markdown("### Prompts")
        for pr in prompts:
            prompts_str += f'- {pr}\n'
        st.markdown(prompts_str)


def top_layer():
    c1, c2 = top_level_container.columns([3,1], vertical_alignment="bottom")
    with c1:
        st.header("Hosanna Skit Prompts")
    with c2:
        st.button("Randomize Prompts", on_click=randomize_prompts)

def randomize_prompts():
    bottom_container.divider()

    prompts_dict = {}

    while len(cell_groups) > 0:
        group = random.choice(cell_groups)
        prompt = random.choice(prompts)
        prompts_dict[group] = prompt

        cell_groups.remove(group)
        prompts.remove(prompt)

    prompts_df = p.DataFrame(prompts_dict.items())
    prompts_df.columns = ["Cell Group", "Prompt"]
    bottom_container.markdown(prompts_df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

    prompts_df.index += 1    
    
    with bottom_container:
        ste.download_button('Download Config',
                                     tabulate(prompts_df, headers='keys', tablefmt='psql'),
                                     "skis_order.txt")

def run():
    show_tables()
    top_layer()
   

if __name__ == "__main__":
    run()


