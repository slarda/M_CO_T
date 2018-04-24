# pylint: disable=C0103
# pylint: disable=C0111
# pylint: disable=E1101
"""add countries

Revision ID: 595f8f83132f
Revises: ebc03d2ac58a
Create Date: 2017-08-17 16:11:33.188203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '595f8f83132f'
down_revision = 'ebc03d2ac58a'
branch_labels = None
depends_on = None


countries = sa.table('countries',
                     sa.column('code', sa.String(3)),
                     sa.column('name', sa.String(100)))


def upgrade():
    op.bulk_insert(countries, [
        {"name": "Afghanistan", "code": "AFG"},
        {"name": "Åland Islands", "code": "ALA"},
        {"name": "Albania", "code": "ALB"},
        {"name": "Algeria", "code": "DZA"},
        {"name": "American Samoa", "code": "ASM"},
        {"name": "Andorra", "code": "AND"},
        {"name": "Angola", "code": "AGO"},
        {"name": "Anguilla", "code": "AIA"},
        {"name": "Antarctica", "code": "ATA"},
        {"name": "Antigua and Barbuda", "code": "ATG"},
        {"name": "Argentina", "code": "ARG"},
        {"name": "Armenia", "code": "ARM"},
        {"name": "Aruba", "code": "ABW"},
        {"name": "Australia", "code": "AUS"},
        {"name": "Austria", "code": "AUT"},
        {"name": "Azerbaijan", "code": "AZE"},
        {"name": "Bahamas", "code": "BHS"},
        {"name": "Bahrain", "code": "BHR"},
        {"name": "Bangladesh", "code": "BGD"},
        {"name": "Barbados", "code": "BRB"},
        {"name": "Belarus", "code": "BLR"},
        {"name": "Belgium", "code": "BEL"},
        {"name": "Belize", "code": "BLZ"},
        {"name": "Benin", "code": "BEN"},
        {"name": "Bermuda", "code": "BMU"},
        {"name": "Bhutan", "code": "BTN"},
        {"name": "Bolivia (Plurinational State of)", "code": "BOL"},
        {"name": "Bonaire, Sint Eustatius and Saba", "code": "BES"},
        {"name": "Bosnia and Herzegovina", "code": "BIH"},
        {"name": "Botswana", "code": "BWA"},
        {"name": "Bouvet Island", "code": "BVT"},
        {"name": "Brazil", "code": "BRA"},
        {"name": "British Indian Ocean Territory", "code": "IOT"},
        {"name": "Brunei Darussalam", "code": "BRN"},
        {"name": "Bulgaria", "code": "BGR"},
        {"name": "Burkina Faso", "code": "BFA"},
        {"name": "Burundi", "code": "BDI"},
        {"name": "Cambodia", "code": "KHM"},
        {"name": "Cameroon", "code": "CMR"},
        {"name": "Canada", "code": "CAN"},
        {"name": "Cabo Verde", "code": "CPV"},
        {"name": "Cayman Islands", "code": "CYM"},
        {"name": "Central African Republic", "code": "CAF"},
        {"name": "Chad", "code": "TCD"},
        {"name": "Chile", "code": "CHL"},
        {"name": "China", "code": "CHN"},
        {"name": "Christmas Island", "code": "CXR"},
        {"name": "Cocos (Keeling) Islands", "code": "CCK"},
        {"name": "Colombia", "code": "COL"},
        {"name": "Comoros", "code": "COM"},
        {"name": "Congo", "code": "COG"},
        {"name": "Congo (Democratic Republic of the)", "code": "COD"},
        {"name": "Cook Islands", "code": "COK"},
        {"name": "Costa Rica", "code": "CRI"},
        {"name": "Côte d'Ivoire", "code": "CIV"},
        {"name": "Croatia", "code": "HRV"},
        {"name": "Cuba", "code": "CUB"},
        {"name": "Curaçao", "code": "CUW"},
        {"name": "Cyprus", "code": "CYP"},
        {"name": "Czech Republic", "code": "CZE"},
        {"name": "Denmark", "code": "DNK"},
        {"name": "Djibouti", "code": "DJI"},
        {"name": "Dominica", "code": "DMA"},
        {"name": "Dominican Republic", "code": "DOM"},
        {"name": "Ecuador", "code": "ECU"},
        {"name": "Egypt", "code": "EGY"},
        {"name": "El Salvador", "code": "SLV"},
        {"name": "Equatorial Guinea", "code": "GNQ"},
        {"name": "Eritrea", "code": "ERI"},
        {"name": "Estonia", "code": "EST"},
        {"name": "Ethiopia", "code": "ETH"},
        {"name": "Falkland Islands (Malvinas)", "code": "FLK"},
        {"name": "Faroe Islands", "code": "FRO"},
        {"name": "Fiji", "code": "FJI"},
        {"name": "Finland", "code": "FIN"},
        {"name": "France", "code": "FRA"},
        {"name": "French Guiana", "code": "GUF"},
        {"name": "French Polynesia", "code": "PYF"},
        {"name": "French Southern Territories", "code": "ATF"},
        {"name": "Gabon", "code": "GAB"},
        {"name": "Gambia", "code": "GMB"},
        {"name": "Georgia", "code": "GEO"},
        {"name": "Germany", "code": "DEU"},
        {"name": "Ghana", "code": "GHA"},
        {"name": "Gibraltar", "code": "GIB"},
        {"name": "Greece", "code": "GRC"},
        {"name": "Greenland", "code": "GRL"},
        {"name": "Grenada", "code": "GRD"},
        {"name": "Guadeloupe", "code": "GLP"},
        {"name": "Guam", "code": "GUM"},
        {"name": "Guatemala", "code": "GTM"},
        {"name": "Guernsey", "code": "GGY"},
        {"name": "Guinea", "code": "GIN"},
        {"name": "Guinea-Bissau", "code": "GNB"},
        {"name": "Guyana", "code": "GUY"},
        {"name": "Haiti", "code": "HTI"},
        {"name": "Heard Island and McDonald Islands", "code": "HMD"},
        {"name": "Holy See", "code": "VAT"},
        {"name": "Honduras", "code": "HND"},
        {"name": "Hong Kong", "code": "HKG"},
        {"name": "Hungary", "code": "HUN"},
        {"name": "Iceland", "code": "ISL"},
        {"name": "India", "code": "IND"},
        {"name": "Indonesia", "code": "IDN"},
        {"name": "Iran (Islamic Republic of)", "code": "IRN"},
        {"name": "Iraq", "code": "IRQ"},
        {"name": "Ireland", "code": "IRL"},
        {"name": "Isle of Man", "code": "IMN"},
        {"name": "Israel", "code": "ISR"},
        {"name": "Italy", "code": "ITA"},
        {"name": "Jamaica", "code": "JAM"},
        {"name": "Japan", "code": "JPN"},
        {"name": "Jersey", "code": "JEY"},
        {"name": "Jordan", "code": "JOR"},
        {"name": "Kazakhstan", "code": "KAZ"},
        {"name": "Kenya", "code": "KEN"},
        {"name": "Kiribati", "code": "KIR"},
        {"name": "Korea (Democratic People's Republic of)", "code": "PRK"},
        {"name": "Korea (Republic of)", "code": "KOR"},
        {"name": "Kuwait", "code": "KWT"},
        {"name": "Kyrgyzstan", "code": "KGZ"},
        {"name": "Lao People's Democratic Republic", "code": "LAO"},
        {"name": "Latvia", "code": "LVA"},
        {"name": "Lebanon", "code": "LBN"},
        {"name": "Lesotho", "code": "LSO"},
        {"name": "Liberia", "code": "LBR"},
        {"name": "Libya", "code": "LBY"},
        {"name": "Liechtenstein", "code": "LIE"},
        {"name": "Lithuania", "code": "LTU"},
        {"name": "Luxembourg", "code": "LUX"},
        {"name": "Macao", "code": "MAC"},
        {"name": "Macedonia (the former Yugoslav Republic of)", "code": "MKD"},
        {"name": "Madagascar", "code": "MDG"},
        {"name": "Malawi", "code": "MWI"},
        {"name": "Malaysia", "code": "MYS"},
        {"name": "Maldives", "code": "MDV"},
        {"name": "Mali", "code": "MLI"},
        {"name": "Malta", "code": "MLT"},
        {"name": "Marshall Islands", "code": "MHL"},
        {"name": "Martinique", "code": "MTQ"},
        {"name": "Mauritania", "code": "MRT"},
        {"name": "Mauritius", "code": "MUS"},
        {"name": "Mayotte", "code": "MYT"},
        {"name": "Mexico", "code": "MEX"},
        {"name": "Micronesia (Federated States of)", "code": "FSM"},
        {"name": "Moldova (Republic of)", "code": "MDA"},
        {"name": "Monaco", "code": "MCO"},
        {"name": "Mongolia", "code": "MNG"},
        {"name": "Montenegro", "code": "MNE"},
        {"name": "Montserrat", "code": "MSR"},
        {"name": "Morocco", "code": "MAR"},
        {"name": "Mozambique", "code": "MOZ"},
        {"name": "Myanmar", "code": "MMR"},
        {"name": "Namibia", "code": "NAM"},
        {"name": "Nauru", "code": "NRU"},
        {"name": "Nepal", "code": "NPL"},
        {"name": "Netherlands", "code": "NLD"},
        {"name": "New Caledonia", "code": "NCL"},
        {"name": "New Zealand", "code": "NZL"},
        {"name": "Nicaragua", "code": "NIC"},
        {"name": "Niger", "code": "NER"},
        {"name": "Nigeria", "code": "NGA"},
        {"name": "Niue", "code": "NIU"},
        {"name": "Norfolk Island", "code": "NFK"},
        {"name": "Northern Mariana Islands", "code": "MNP"},
        {"name": "Norway", "code": "NOR"},
        {"name": "Oman", "code": "OMN"},
        {"name": "Pakistan", "code": "PAK"},
        {"name": "Palau", "code": "PLW"},
        {"name": "Palestine, State of", "code": "PSE"},
        {"name": "Panama", "code": "PAN"},
        {"name": "Papua New Guinea", "code": "PNG"},
        {"name": "Paraguay", "code": "PRY"},
        {"name": "Peru", "code": "PER"},
        {"name": "Philippines", "code": "PHL"},
        {"name": "Pitcairn", "code": "PCN"},
        {"name": "Poland", "code": "POL"},
        {"name": "Portugal", "code": "PRT"},
        {"name": "Puerto Rico", "code": "PRI"},
        {"name": "Qatar", "code": "QAT"},
        {"name": "Réunion", "code": "REU"},
        {"name": "Romania", "code": "ROU"},
        {"name": "Russian Federation", "code": "RUS"},
        {"name": "Rwanda", "code": "RWA"},
        {"name": "Saint Barthélemy", "code": "BLM"},
        {"name": "Saint Helena, Ascension and Tristan da Cunha", "code": "SHN"},
        {"name": "Saint Kitts and Nevis", "code": "KNA"},
        {"name": "Saint Lucia", "code": "LCA"},
        {"name": "Saint Martin (French part)", "code": "MAF"},
        {"name": "Saint Pierre and Miquelon", "code": "SPM"},
        {"name": "Saint Vincent and the Grenadines", "code": "VCT"},
        {"name": "Samoa", "code": "WSM"},
        {"name": "San Marino", "code": "SMR"},
        {"name": "Sao Tome and Principe", "code": "STP"},
        {"name": "Saudi Arabia", "code": "SAU"},
        {"name": "Senegal", "code": "SEN"},
        {"name": "Serbia", "code": "SRB"},
        {"name": "Seychelles", "code": "SYC"},
        {"name": "Sierra Leone", "code": "SLE"},
        {"name": "Singapore", "code": "SGP"},
        {"name": "Sint Maarten (Dutch part)", "code": "SXM"},
        {"name": "Slovakia", "code": "SVK"},
        {"name": "Slovenia", "code": "SVN"},
        {"name": "Solomon Islands", "code": "SLB"},
        {"name": "Somalia", "code": "SOM"},
        {"name": "South Africa", "code": "ZAF"},
        {"name": "South Georgia and the South Sandwich Islands", "code": "SGS"},
        {"name": "South Sudan", "code": "SSD"},
        {"name": "Spain", "code": "ESP"},
        {"name": "Sri Lanka", "code": "LKA"},
        {"name": "Sudan", "code": "SDN"},
        {"name": "Suriname", "code": "SUR"},
        {"name": "Svalbard and Jan Mayen", "code": "SJM"},
        {"name": "Swaziland", "code": "SWZ"},
        {"name": "Sweden", "code": "SWE"},
        {"name": "Switzerland", "code": "CHE"},
        {"name": "Syrian Arab Republic", "code": "SYR"},
        {"name": "Taiwan, Province of China", "code": "TWN"},
        {"name": "Tajikistan", "code": "TJK"},
        {"name": "Tanzania, United Republic of", "code": "TZA"},
        {"name": "Thailand", "code": "THA"},
        {"name": "Timor-Leste", "code": "TLS"},
        {"name": "Togo", "code": "TGO"},
        {"name": "Tokelau", "code": "TKL"},
        {"name": "Tonga", "code": "TON"},
        {"name": "Trinidad and Tobago", "code": "TTO"},
        {"name": "Tunisia", "code": "TUN"},
        {"name": "Turkey", "code": "TUR"},
        {"name": "Turkmenistan", "code": "TKM"},
        {"name": "Turks and Caicos Islands", "code": "TCA"},
        {"name": "Tuvalu", "code": "TUV"},
        {"name": "Uganda", "code": "UGA"},
        {"name": "Ukraine", "code": "UKR"},
        {"name": "United Arab Emirates", "code": "ARE"},
        {"name": "United Kingdom of Great Britain and Northern Ireland", "code": "GBR"},
        {"name": "United States of America", "code": "USA"},
        {"name": "United States Minor Outlying Islands", "code": "UMI"},
        {"name": "Uruguay", "code": "URY"},
        {"name": "Uzbekistan", "code": "UZB"},
        {"name": "Vanuatu", "code": "VUT"},
        {"name": "Venezuela (Bolivarian Republic of)", "code": "VEN"},
        {"name": "Viet Nam", "code": "VNM"},
        {"name": "Virgin Islands (British)", "code": "VGB"},
        {"name": "Virgin Islands (U.S.)", "code": "VIR"},
        {"name": "Wallis and Futuna", "code": "WLF"},
        {"name": "Western Sahara", "code": "ESH"},
        {"name": "Yemen", "code": "YEM"},
        {"name": "Zambia", "code": "ZMB"},
        {"name": "Zimbabwe", "code": "ZWE"},
    ])


def downgrade():
    op.execute(countries.delete())
