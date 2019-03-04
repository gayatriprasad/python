# import re

def referenceSpectra(filepath):
    key_dict = {}
    with open(filepath, 'r') as f:
        for line in f:
            items = line.split()
            key, values = items[0], items[1]
            values = (values.split(','))
            for i in range (0, len(values)):
                values[i] = float(values[i]) 
            values = tuple(sorted(values))
            key_dict[key] = values
            
    return key_dict
 
def referenceLines(spec_r, spec_m, eps =0.1):
    count = 0
    # spec_m = list(spec_m)
    # spec_r = list(spec_r)
    # eps = eps
    # print('ref-spec:',spec_ref)
    # print('mes-spec:',spec_mes)
    for i in range(len(spec_r)):
        for j in range(len(spec_m)):
            if abs(spec_r[i] - spec_m[j]) <= eps:
                # print('spec_m:',spec_m[j])
                # print('spec_r:',spec_r[i])
                count += 1
    return count

def decomposition(spec, referenceSpectrum, eps = 0.1, minimum=None):
    # print(type(spec))
    spec = list(spec)
    eps = eps
    my_dict = referenceSpectrum
    dec = []
    for key, value in my_dict.items():
        count = referenceLines(spec, my_dict[key], eps)
        if minimum == None:
            if count == len(my_dict[key]):
                dec.append(key)
        elif count >= minimum:
            dec.append(key)
    dec = sorted(dec)        
    # print(dec)
    return dec
    
referenceSpectrum10 = referenceSpectra('spectra10.txt')
# print(referenceSpectrum)
spectrum1 = (410.1055, 434.1126, 434.1427, 486.171, 656.224)
spectrum = (402.5579, 410.1914, 413.162, 434.1243, 486.0598, 504.7387, 610.157, 610.562, 656.354, 670.578, 670.991)
#print(referenceLines(spectrum1, referenceSpectrum['H']))
# print(referenceSpectrum['H'])
# print(spectrum1)
spectrum2 = (140.61, 164.41, 346.974, 369.691, 375.217, 398.252, 410.768, 424.54, 433.718, 542.365, 563.833, 573.85, 586.017, 594.192, 603.628, 635.811, 637.865, 640.153, 683.08, 694.492, 696.258, 699.009, 706.147, 707.567, 722.643, 766.864, 789.367, 857.236, 865.301, 891.966, 903.941, 956.798, 990.594, 1028.683, 1435.196, 4603.616, 4662.43, 6400.89, 9625.29, 12512.877)
spectrum10 = (108.352, 121.771, 135.44, 196.125, 206.233, 219.188, 326.875, 350.734, 366.911, 367.057, 390.156, 396.688, 408.593, 417.818, 423.466, 430.879, 448.41, 465.813, 468.892, 491.571, 515.908, 525.188, 551.417, 557.587, 585.076, 602.338, 603.231, 605.408, 626.727, 631.577, 650.259, 655.356, 671.691, 696.363, 741.915, 765.999, 780.622, 840.301, 862.073, 866.433, 877.614, 879.626, 932.43, 974.716, 975.127, 1491.888, 1495.364, 2044.96, 2401.135, 2809.553, 2896.506, 3973.63, 5242.28, 5659.23, 6484.1, 6987.22, 8542.09, 9510.78)
print(decomposition(spectrum10, referenceSpectrum10))