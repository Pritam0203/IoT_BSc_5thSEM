import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    st.title("Real-time DHT Sensor Readings Dashboard")

    try:
        df = pd.read_csv('dht_readings.csv', parse_dates=['Timestamp'], index_col='Timestamp')
    except FileNotFoundError:
        st.write("No data available yet.")
        return

    # Chart for Temperature
    st.subheader("Temperature Chart (°C)")
    st.line_chart(df['Temperature'])

    # Histogram for Temperature
    st.subheader("Temperature Histogram (°C)")
    fig_hist_temp = px.histogram(df, x='Temperature', nbins=20, labels={'Temperature': 'Temperature (°C)'})
    st.plotly_chart(fig_hist_temp)

    # Chart for Humidity
    st.subheader("Humidity Chart (gm/kg)")
    st.line_chart(df['Humidity'])

    # Histogram for Humidity
    st.subheader("Humidity Histogram (gm/kg)")
    fig_hist_humidity = px.histogram(df, x='Humidity', nbins=20, labels={'Humidity': 'Humidity (gm/kg)'})
    st.plotly_chart(fig_hist_humidity)

if __name__ == '__main__':
    main()
