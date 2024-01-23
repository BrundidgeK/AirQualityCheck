import matplotlib.pyplot as plt

def create_bar_chart():
    # Data for carbon emissions from different sectors
    sectors = ['Transportation', 'Industry', 'Energy Production']
    emissions = [30, 40, 30]  # Example values, you can replace with actual data

    # Plotting the bar chart
    plt.bar(sectors, emissions, color=['blue', 'orange', 'green'])

    # Adding labels and title
    plt.xlabel('Sectors')
    plt.ylabel('Carbon Emissions (%)')
    plt.title('Carbon Emissions by Sector')

    # Display the bar chart
    plt.show()

# Call the function to create and display the bar chart
create_bar_chart()
