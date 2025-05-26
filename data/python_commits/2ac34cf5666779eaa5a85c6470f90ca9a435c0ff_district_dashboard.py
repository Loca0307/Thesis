monthly_fig.update_traces(textposition='top center')  # Adjust label positioning

col2.subheader("Monthly Accident Trend")
col2.plotly_chart(monthly_fig)

# Weekly Trend
st.subheader("Weekly Accident Trend")
weekday_counts = final_filtered_df['Weekday'].value_counts().sort_index()
weekday_fig = px.bar(
    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    y=weekday_counts.values,
    labels={'x': 'Day of the Week', 'y': 'Number of Accidents'}
)
st.plotly_chart(weekday_fig)

# Urban/Rural & Vehicle Breakdown
col3, col4 = st.columns(2)
urban_rural_counts = final_filtered_df['Urban_or_Rural_Area'].value_counts()
urban_rural_fig = px.bar(x=urban_rural_counts.index, y=urban_rural_counts.values, text=urban_rural_counts.values,
                          labels={'x': 'Location Type', 'y': 'Number of Accidents'})
col3.subheader("Urban vs. Rural Accidents")
col3.plotly_chart(urban_rural_fig)

vehicle_category_counts = final_filtered_df['Vehicle_Category'].value_counts()
vehicle_category_fig = px.bar(x=vehicle_category_counts.index, y=vehicle_category_counts.values, text=vehicle_category_counts.values,
                              labels={'x': 'Vehicle Type', 'y': 'Number of Accidents'})
col4.subheader("Vehicle Type Breakdown")
col4.plotly_chart(vehicle_category_fig)

# Light Conditions vs Severity & Road Surface Conditions vs Severity
col5, col6 = st.columns(2)
light_severity_fig = px.histogram(final_filtered_df, x='Light_Conditions', color='Accident_Severity', barmode='group',
                                  labels={'Light_Conditions': 'Lighting', 'Accident_Severity': 'Severity'})
col5.subheader("Light Conditions vs. Severity")
col5.plotly_chart(light_severity_fig)

road_surface_fig = px.histogram(final_filtered_df, x='Road_Surface_Conditions', color='Accident_Severity', barmode='group',
                                labels={'Road_Surface_Conditions': 'Road Surface', 'Accident_Severity': 'Severity'})
col6.subheader("Road Surface Conditions vs. Severity")
col6.plotly_chart(road_surface_fig)