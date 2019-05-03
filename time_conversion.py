def timeConversion(s):
    cTime = {'12AM' : '00', '01AM' : '01', '02AM' : '02', '03AM' : '03', '04AM' : '04', '05AM' : '05', '06AM' : '06', '07AM' : '07', '08AM': '08', '09AM' : '09', '10AM' : '10', '11AM' : '11', '12PM' : '12', '01PM' : '13', '02PM' : '14', '03PM' : '15', '04PM' : '16', '05PM' : '17', '06PM' : '18', '07PM' : '19', '08PM': '20', '09PM' : '21', '10PM' : '22', '11PM' : '23'}
    idty = s.split(':')
    hr, cHr, cSec, nTime = 0, "", "", ""
    if idty[-1].endswith("AM"):
        hr = idty[0]+"AM"
        cSec = idty[2].replace("AM", "")
    else:
        hr = idty[0]+"PM"
        cSec = idty[2].replace("PM", "")
    cHr = cTime.get(str(hr))
    nTime = cHr + ":" + idty[1] + ":" + cSec
    return nTime
