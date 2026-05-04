# ====================== WEEKLY SPEND DATA ======================
spend_data = {
    "User": ["narossoh", "gpliegom", "stajenni", "iqrayuss", "matstrak", "nkaibrah", "mnimhas", 
             "arrizola", "hasnsai", "uiyps", "mtiband r", "elizev", "danijac", "hersmary", 
             "abdiosmg", "jnoonoor", "musaom"],
    "Pick Opportunities": [0, 362, 804, 37, 186, 255, 97, 614, 214, 208, 68, 176, 169, 69, 44, 110, 55],
    "Stow Opportunities": [1068, 580, 127, 758, 594, 518, 668, 57, 416, 330, 445, 204, 168, 246, 214, 63, 0],
    "Total Opportunities": [1814, 942, 931, 795, 780, 773, 765, 671, 630, 538, 513, 380, 337, 315, 258, 173, 55],
    "% of Total Volume": [17.00, 8.83, 8.73, 7.45, 7.31, 7.24, 7.17, 6.29, 5.90, 5.04, 4.81, 3.56, 3.16, 2.95, 2.42, 1.62, 0.52],
    "Estimated Spend": [1624.18, 843.62, 834.06, 711.77, 698.40, 691.71, 685.02, 600.95, 563.69, 481.52, 459.55, 340.12, 301.91, 281.84, 231.21, 154.77, 49.68]
}

df_spend = pd.DataFrame(spend_data)

# NEW: Rename column and add 32-hour ratio (only for narossoh)
df_spend = df_spend.rename(columns={"Estimated Spend": "Estimated Value"})

# Add ratio column - only populated for narossoh (based on 32 hours worked)
df_spend["Value per 32h (Ratio)"] = ""
# For narossoh: Estimated Value normalized to his 32 hours (Value per 32 hours)
narossoh_mask = df_spend["User"] == "narossoh"
if narossoh_mask.any():
    nar_value = df_spend.loc[narossoh_mask, "Estimated Value"].iloc[0]
    df_spend.loc[narossoh_mask, "Value per 32h (Ratio)"] = f"${nar_value:,.2f}"
