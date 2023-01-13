import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from dbset.nutrients import nutrients

def show_result(ansname, anscal, anspro):
    st.markdown("# 結果！！")
    st.markdown("**この写真は{}％の確率で{}です。**".format(anspro, ansname)); st.markdown("**{}の場合、カロリーは{}kcalとなります。**".format(ansname, anscal))

def show_chart(foodvalue):
    values = nutrients(foodvalue)
    labels = ["たんぱく質", "脂質", "炭水化物", "糖質", "食物繊維"]
    radar_values = np.concatenate([values, [values[0]]])
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
    rgrids = [0, 20, 40, 60, 80, 100]
    fig = plt.figure(facecolor="w")
    
    ax = fig.add_subplot(1, 1, 1, polar=True)
    ax.plot(angles, radar_values)
    ax.fill(angles, radar_values, alpha=0.2)
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontname="MS Gothic")
    ax.set_rgrids([])
    ax.spines['polar'].set_visible(False)
    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)

    for grid_value in rgrids:
        grid_values = [grid_value] * (len(labels)+1)
        ax.plot(angles, grid_values, color="gray",  linewidth=0.5)

    for t in rgrids: ax.text(x=0, y=t, s=t)

    ax.set_rlim([min(rgrids), max(rgrids)])
    ax.set_title("{}1個あたりの栄養素".format(foodvalue), pad=20, fontname="MS Gothic")
    st.pyplot(fig)
