# BeautifulSoup library facilitates parsing of XML response
import bs4 as bs

# This library faciliates 2-dimensional array operations and visualization
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

# For API call request
import requests


## Age Group:
age_group_list = ["1-4","5-14","15-24","25-34","35-44","45-54","55-64","65-74","75-84","85+"]


def parameters_input(year: int, age_group: list):
    # by-variables" or those parameters selected in the "Group Results By" and the "And By" drop-down lists 
# in the "Request Form." These "by-variables" are the cross-tabulations, stratifications or indexes 
# to the query results. Expect the results data table to show a row for each category in the by-variables, 
# and a column for each measure. For example, if you wish to compare data by sex, then "group results by" gender, 
# to get a row for females and a row for males in the output.
# M_ are measures to return, the default measures plus any optional measures.

# For this example, will group by race and age group

    b_parameters = {
    "B_1": "D76.V8",   #Race
    "B_2": "D76.V17",  #Ethnicity
    "B_3": "D76.V7",   #Gender
    "B_4": "*None*", 
    "B_5": "*None*"
    }

# measures to return, the default measures plus any optional measures

# For this example, include deaths, population

    m_parameters = {
        "M_1": "D76.M1",   # Deaths, must be included
        "M_2": "D76.M2",   # Population, must be included
        "M_3": "D76.M3"   # Crude rate, must be included
        #"M_31": "D76.M31",        # Standard error (crude rate)
        #"M_32": "D76.M32"         # 95% confidence interval (crude rate)
        #"M_41": "D76.M41", # Standard error (age-adjusted rate)
        #"M_42": "D76.M42"  # 95% confidence interval (age-adjusted rate)
    }

# values highlighted in a "Finder" control for hierarchical lists, 
# such as the "Regions/Divisions/States/Counties hierarchical" list.

# For this example, include all years, months, census regions, hhs regions, states.
    f_parameters = {
        "F_D76.V1": [f"{year}"], # year/month
        "F_D76.V10": ["*All*"], # Census Regions - dont change
        "F_D76.V2": ["*All*"], # ICD-10 Codes
        "F_D76.V27": ["*All*"], # HHS Regions - dont change
        "F_D76.V9": ["*All*"] # State County - dont change    
    }

    # contents of the "Currently selected" information areas next to "Finder" controls in the "Request Form."

# For this example, include all dates, census regions, hhs regions, and states.
# Only include ICD-10 code K00-K92 for disease of the digestive system

    i_parameters = {
        "I_D76.V1": "*All* (All Dates)",  # year/month
        "I_D76.V10": "*All* (The United States)", # Census Regions - dont change
        "I_D76.V27": "*All* (The United States)", # HHS Regions - dont change
        "I_D76.V9": "*All* (The United States)" # State County - dont change
    }

    # variable values to limit in the "where" clause of the query, found in multiple select 
# list boxes and advanced finder text entry boxes in the "Request Form."

# For this example, we want to include ten-year age groups for ages 15-44.
# For all other categories, include all values

    

    v_parameters = {
        "V_D76.V1": "",         # Year/Month
        "V_D76.V10": "",        # Census Regions
        "V_D76.V11": "*All*",   # 2006 Urbanization
        "V_D76.V12": "*All*",   # ICD-10 130 Cause List (Infants)
        "V_D76.V17": "*All*",   # Hispanic Origin
        "V_D76.V19": "*All*",   # 2013 Urbanization
        "V_D76.V2": "",         # ICD-10 Codes
        "V_D76.V20": "*All*",   # Autopsy
        "V_D76.V21": "*All*",   # Place of Death
        "V_D76.V22": "*All*",   # Injury Intent
        "V_D76.V23": "*All*",   # Injury Mechanism and All Other Leading Causes
        "V_D76.V24": "*All*",   # Weekday
        "V_D76.V25": "*All*",   # Drug/Alcohol Induced Causes
        "V_D76.V27": "",        # HHS Regions
        "V_D76.V5": age_group, # Ten-Year Age Groups
        "V_D76.V51": "*All*",   # Five-Year Age Groups
        "V_D76.V52": "*All*",   # Single-Year Ages
        "V_D76.V6": "00",       # Infant Age Groups
        "V_D76.V7": "*All*",    # Gender
        "V_D76.V8": "*All*",    # Race
        "V_D76.V9": ""          # State/County
    }

    ## Abstract Away

# other parameters, such as radio buttons, checkboxes, and lists that are not data categories

# For this example, include age-adjusted rates, use ten-year age groups (D76.V5), use state location by default, 
# show rates per 100,000, use 2013 urbanization and use ICD-10 Codes (D76.V2) for cause of death category

    o_parameters = {
        "O_V10_fmode": "freg",    # Use regular finder and ignore v parameter value
        "O_V1_fmode": "freg",     # Use regular finder and ignore v parameter value
        "O_V27_fmode": "freg",    # Use regular finder and ignore v parameter value
        "O_V2_fmode": "freg",     # Use regular finder and ignore v parameter value
        "O_V9_fmode": "freg",     # Use regular finder and ignore v parameter value
        #"O_V7_fmode": "freg",     # Use regular finder and ignore v parameter value
        "O_aar": "aar_std",       # age-adjusted rates
        "O_aar_pop": "0000",      # population selection for age-adjusted rates
        "O_age": "D76.V5",        # select age-group (e.g. ten-year, five-year, single-year, infant groups)
        "O_javascript": "on",     # Set to on by default
        "O_location": "D76.V9",   # select location variable to use (e.g. state/county, census, hhs regions)
        "O_precision": "1",       # decimal places
        "O_rate_per": "100000",   # rates calculated per X persons
        "O_show_totals": "false",  # Show totals for 
        "O_timeout": "300",
        "O_title": "Male Population and Death Rate, by Age Group and Race",    # title for data run
        "O_ucd": "D76.V2",        # select underlying cause of death category
        "O_urban": "D76.V19"      # select urbanization category
    }

    # values for non-standard age adjusted rates (see mortality online databases).

    # For this example, these parameters are ignored as standard age adjusted rates are used

    vm_parameters = {
        "VM_D76.M6_D76.V10": "",        # Location
        "VM_D76.M6_D76.V17": "*All*",   # Hispanic-Origin
        "VM_D76.M6_D76.V1_S": "*All*",  # Year
        "VM_D76.M6_D76.V7": "*All*",    # Gender
        "VM_D76.M6_D76.V8": "*All*"     # Race
    }

    # Miscellaneous hidden inputs/parameters usually passed by web form. These do not change.
    misc_parameters = {
        "action-Send": "Send",
        "finder-stage-D76.V1": "codeset",
        "finder-stage-D76.V1": "codeset",
        "finder-stage-D76.V2": "codeset",
        "finder-stage-D76.V27": "codeset",
        "finder-stage-D76.V9": "codeset",
        "stage": "request"
    }

    return (b_parameters, m_parameters, f_parameters, i_parameters, o_parameters, vm_parameters, v_parameters, misc_parameters)


def createParameterList(parameterList):
    """Helper function to create a parameter list from a dictionary object"""
    
    parameterString = ""
    
    for key in parameterList:
        parameterString += "<parameter>\n"
        parameterString += "<name>" + key + "</name>\n"
        
        if isinstance(parameterList[key], list):
            for value in parameterList[key]:
                parameterString += "<value>" + value + "</value>\n"
        else:
            parameterString += "<value>" + parameterList[key] + "</value>\n"
        
        parameterString += "</parameter>\n"
        
    return parameterString


def parse_xml_request(parameters_tuple):
    xml_request = "<request-parameters>\n"
    
    for i in range(len(parameters_tuple)):
        xml_request += createParameterList(parameters_tuple[i])
    
    xml_request += "</request-parameters>"

    return xml_request


def get_xml_response(xml_request):
    url = "https://wonder.cdc.gov/controller/datarequest/D76"
    response = requests.post(url, data={"request_xml": xml_request, "accept_datause_restrictions": "true"})

    if response.status_code == 200:
        data = response.text
        return data
    else:
        print("something went wrong")


def xml2df(xml_data):
    """ This function grabs the root of the XML document and iterates over
        the 'r' (row) and 'c' (column) tags of the data-table
        Rows with a 'v' attribute contain a numerical value
        Rows with a 'l attribute contain a text label and may contain an
        additional 'r' (rowspan) tag which identifies how many rows the value
        should be added. If present, that label will be added to the following
        rows of the data table.
    
        Function returns a two-dimensional array or data frame that may be 
        used by the pandas library."""
    
    root = bs.BeautifulSoup(xml_data,"lxml")
    all_records = []
    row_number = 0
    rows = root.find_all("r")
    
    for row in rows:
        if row_number >= len(all_records):
            all_records.append([])
              
        for cell in row.find_all("c"):
            if 'v' in cell.attrs:
                try:
                    all_records[row_number].append(float(cell.attrs["v"].replace(',','')))
                except ValueError:
                    all_records[row_number].append(cell.attrs["v"])
            else:
                if 'r' not in cell.attrs:
                    all_records[row_number].append(cell.attrs["l"])
                else:
                
                    for row_index in range(int(cell.attrs["r"])):
                        if (row_number + row_index) >= len(all_records):
                            all_records.append([])
                            all_records[row_number + row_index].append(cell.attrs["l"])
                        else:
                            all_records[row_number + row_index].append(cell.attrs["l"])
                                           
        row_number += 1
    return all_records


def parse_dataframe(data, age_group:str):

    data_frame = xml2df(data)

    df = pd.DataFrame(data=data_frame, columns=["Race", "Ethnicity", "Gender", "Deaths", "Population", "Crude Rate", "Age-adjusted Rate"])

    df = df.query('Gender == "Male"')

    df["Age Group"] = age_group

    return df


def start_query(year: int, age_group_list=age_group_list):

    df_list = list()

    # Call the parameters input function to set up the parameters
    for i in range(0, len(age_group_list)-1, 2):

        parameters = parameters_input(year=year, age_group=age_group_list[i:i+2])

        xml_request = parse_xml_request(parameters_tuple=parameters)

        data = get_xml_response(xml_request)

        if (i+1) < 9:
            age_group_string = age_group_list[i].split('-')[0] + '-' + age_group_list[i+1].split('-')[1]
        else:
            age_group_string = age_group_list[i].split('-')[0] + '-' + age_group_list[i+1]

        df = parse_dataframe(data, age_group_string)

        df_list.append(df)

    df_current = df_list[0]

    for j in range(0, len(df_list)-1, 1):
        
        df_current = pd.concat([df_current, df_list[j+1]], ignore_index=True)

    return df_current

