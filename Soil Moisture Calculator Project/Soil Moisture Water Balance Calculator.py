#Calculator which takes certain parameters
#and returns certain values needed for
#watershed evaluation
#author:Daksh-Pat


#Calculates daily precipitation based on days in the month
def daily_precip(monthly_precip,days_in_month):
    return monthly_precip//days_in_month

#Calculates the heat index based on mean monthly temperature
#and days in the month
def heat_index(mean_temp,days_in_month):
    if mean_temp > 0:
        return 0
    else:
        return (mean_temp/days_in_month)**1.514

#Calculates the unadjusted potential evapotranspiration
#I and a values are constants
def unadjusted_potential_evapotranspiratin(mean_temp,I,a):
    if mean_temp < 0:
        return 0
    else:
        return 16*10*((mean_temp / I) ** a)

#Calculates the adjusted potential evapotranspiration
#adjusted based on daylight hours in the month and the
#number of days in the month
def adjusted_potential_evapotranspiration(unadjusted_potential_evapotranspiration,days_in_month,daylight_hours):
    daylight_daily=daylight_hours/days_in_month
    return unadjusted_potential_evapotranspiration*(days_in_month/30)*(daylight_daily/30)

#Gives us the water surplus/deficiet based on monthly
#precipitation and adjusted potential evapotranspiration
def water_surplus_deficity(monthly_precip,adjusted_potential_evapotranspiration):
    return monthly_precip-adjusted_potential_evapotranspiration

#Gives us the total water storage of the soil based on
#the water surplus/deficiet of the soil
def soil_water_storage(water_surplus_deficity):
    if (water_surplus_deficity+130)>0:
        if (water_surplus_deficity+130)>190:
            return 190
        else:
            return water_surplus_deficity+130
    else:
        return 0

#Gives us the actual evapotranspiration of the soil
#based on adjusted potential evapotranspiration,
#monthly precipitation, and soil water storage
def actual_evapotranspiration(adjusted_potential_evapotranspiration,monthly_precip,soil_water_storage):
    if adjusted_potential_evapotranspiration<(monthly_precip+soil_water_storage):
        return adjusted_potential_evapotranspiration
    else:
        return soil_water_storage+monthly_precip

#Calculates the soil's monthly runoff based on
#monthly precipitation, actual evapotranspiration,
#and soil water storage
def monthly_runoff(monthly_precip,actual_evapotranspiration,soil_water_storage):
    return monthly_precip-(actual_evapotranspiration+soil_water_storage)

while True:
    try:
        #Constants used for unadjusted potential evapotranspiration
        I = 3.04
        a = 0.54

        #Inputs for the calcuations
        days_in_month=float(input("Days in month: "))
        monthly_daylight_hours=float(input("Monthly Daylight Hours: "))
        mean_temp=float(input("Mean monthly temperature in Celcius: "))
        monthly_precip=float(input("Monthly precipitation in mm/month: "))

        daily_precip=daily_precip(monthly_precip, days_in_month)

        print("Daily precipitation in mm/day: " + str(daily_precip))

        heat_index=heat_index(mean_temp, days_in_month)
        unadjusted_PET=unadjusted_potential_evapotranspiratin(mean_temp,I,a)
        adjusted_PET=adjusted_potential_evapotranspiration(unadjusted_PET,days_in_month,monthly_daylight_hours)

        print("Unadjusted potential evapotranspiration in mm/month: " + str(unadjusted_PET))
        print("Adjusted potential evapotranspiration in mm/month: " + str(adjusted_PET))

        water_surplus_deficity=water_surplus_deficity(monthly_precip,adjusted_PET)

        print("Water surplus/deficity in mm/month: "+ str(water_surplus_deficity))

        soil_water_storage=soil_water_storage(water_surplus_deficity)

        print("Soil water storage in mm/month: " + str(soil_water_storage))

        actual_ET=actual_evapotranspiration(monthly_precip,adjusted_PET,soil_water_storage)

        print("Actual Evapotranspiration in mm/month: " + str(actual_ET))

        runoff=monthly_runoff(monthly_precip,actual_ET,soil_water_storage)

        print("Monthly runoff in mm/month: " +str(runoff))
        break

    except ValueError:
        print("Only integers or float values.")
        continue




