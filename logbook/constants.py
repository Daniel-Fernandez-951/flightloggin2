NON_FLYING_CHOICES = (
    (1, "1st Class Medical"),
    (2, "2nd Class Medical"),
    (3, "3rd Class Medical"),
    (4, "CFI Refresher"),
    (5, "Student Signoff"),
)

FIELDS = [
          'date', 'plane', 'route',
          'total', 'pic', 'sic', 'solo', 'night', 'dual_r','dual_g', 'xc','act_inst', 'sim_inst', 'night_l','day_l', 'app',
          'p2p',
          'multi', 'm_pic',
          'sea', 'sea_pic', 'mes', 'mes_pic',
          'turbine', 't_pic', 'mt', 'mt_pic',
          'person', 'remarks',
          ]
          
FIELD_TITLES = {
    "date": "Date",
    "plane": "Plane",
    "route": "Route",
    "total": "Total",
    "pic": "PIC",
    "sic": "SIC",
    "solo": "Solo",
    "night": "Night",
    "dual_r": "Dual Received",
    "dual_g": "Dual Given",
    "xc": "Cross Country",
    "act_inst": "Actual Instrument",
    "sim_inst": "Simulated Instrument",
    "night_l": "Night Landings",
    "day_l": "Day Landings",
    "app": "Approaches",
    "p2p": "Point to Point Cross Country",
    "multi": "Milti-Engine",
    "m_pic": "Milti-Engine PIC",
    "sea": "Seaplane",
    "sea_pic": "Seaplane PIC",
    "mes": "Milti-Engine Seaplane",
    "mes_pic": "Milti-Engine Seaplane PIC",
    "turbine": "Turbine",
    "t_pic": "Turbine PIC",
    "mt": "Multi-Engine Turbine",
    "mt_pic": "Multi-Engine Turbine PIC",
    "person": "Person",
    "remarks": "Remarks",
}

FIELD_ABBV = {
    "date": "Date",
    "plane": "Plane",
    "route": "Route",
    "total": "Total",
    "pic": "PIC",
    "sic": "SIC",
    "solo": "Solo",
    "night": "Night",
    "dual_r": "Dual R.",
    "dual_g": "Dual G.",
    "xc": "XC",
    "act_inst": "Actual",
    "sim_inst": "Hood",
    "night_l": "Night L.",
    "day_l": "Day L.",
    "app": "App's",
    "p2p": "P2P",
    "multi": "Milti",
    "m_pic": "Milti PIC",
    "sea": "Sea",
    "sea_pic": "Sea PIC",
    "mes": "Milti Sea",
    "mes_pic": "Milti Sea PIC",
    "turbine": "Turbine",
    "t_pic": "Turbine PIC",
    "mt": "Multi Turbine",
    "mt_pic": "Multi Turbine PIC",
    "person": "Person",
    "remarks": "Remarks",
}

EDITABLE_FIELDS = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,27]
