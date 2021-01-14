import requests

url = 'https://docs.google.com/forms/d/e/1FAIpQLSf7Cz4ezVNmN5953f7YmfA01AG4I3hg-Hu8MbcFglbGPGHF5A/formResponse'

values = {
    # page 1
    "emailAddress" : 'paopeaw8246@gmail.com',
    "entry.72918931" : 'นาย',
    "entry.751458963" : 'มัธยมศึกษาปีที่ 5',
    "entry.372182226" : '6',
    "entry.829337025" : '10',
    "entry.814157305" : 'รุจิภัส ทองเป้า',
    #page 2
    'entry.1194415485' : '0623329111',
    'entry.1345463338' : '44/3',
    'entry.1522295025' : 'กรุงเทพ',
    'entry.1572349720' : 'บางเขน',
    'entry.589741780' : 'ท่าแร้ง',
    'entry.65583610' : '5',
    'entry.736930435' : '10220',
    #page 3
    'entry.187932221':'36',
    'entry.371010062' : 'ไม่มีอาการ',
    'entry.1905210885' : 'ไม่มีอาการ',
    'entry.1407629932' : 'ไม่มีอาการ',
    'entry.1994207189' : 'ไม่มีอาการ',
    'entry.582311905' : 'ไม่มีอาการ',
    'entry.1109590249' : 'ไม่มีอาการ',
    'entry.1790123196' : 'ไม่มีอาการ',
    #page 4
    'entry.1962229773':'ไม่มีการเดินทาง อยู่ที่พักอาศัยตลอดทั้งวัน',
    'entry.773862454' : 'ไม่มี',
    'entry.1728023076' : 'ไม่มี'
}




for v in values:
    try:
        requests.post(url, data=v)
        print('Submitted')
    except:
        print("Error Occured")


