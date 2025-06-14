import calendar

def format_week(week):
    return ' | '.join(f"{day:2}" if day != 0 else '  ' for day in week)

def generate_calendar(year):
    with open("school_year_calendar.txt", "w") as file:
        # Loop through each month of the year
        for month in range(1, 13):
            # Write the month header
            file.write(f"\n{calendar.month_name[month]} {year}\n")
            file.write("Mo | Tu | We | Th | Fr\n")
            file.write("-" * 23 + "\n")  # Separator line

            # Generate calendar for the month
            month_calendar = calendar.monthcalendar(year, month)
            
            for week in month_calendar:
                file.write(format_week(week) + "\n")
            
            file.write("\n")  # Add an extra newline for spacing

# Define the start year
start_year = 2024
generate_calendar(start_year)

print("Calendar has been created and saved to 'school_year_calendar.txt'.")

