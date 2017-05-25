import sys
import csv
import re


def jobcat(f_jobcat):
    jobcat_dict = {}
    next(f_jobcat)
    for line in f_jobcat:
        cats = line.strip().split(',')[0:2]
        jobcat_dict[cats[0]] = cats[1]
    return jobcat_dict


def jobcat_cnt(f_jobinfo, jobcat_dict):
    jobcat_cnt_dict = {}
    next(f_jobinfo)
    for line in f_jobinfo:
        jobcats = line.strip().split('|')[3:6]
        for jobcat in jobcats:
            if re.search(r'2\d{9}', jobcat):
                prefix = str(int(int(jobcat) / 1000000)) + '.'
                jobcat = prefix + jobcat_dict[jobcat]
                if jobcat in jobcat_cnt_dict:
                    jobcat_cnt_dict[jobcat] += 1
                else:
                    jobcat_cnt_dict[jobcat] = 1
    return jobcat_cnt_dict


if __name__ == '__main__':
    with open(sys.argv[2].strip(), 'r') as f_jobcat:
        jobcat_dict = jobcat(f_jobcat)
    with open(sys.argv[1].strip(), 'r') as f_jobinfo:
        jobcat_cnt_dict = jobcat_cnt(f_jobinfo, jobcat_dict)

    with open('jobcat.csv', 'w') as f_csv:
        writer = csv.writer(f_csv)
        writer.writerow(['id', 'value'])
        for key in sorted(jobcat_cnt_dict.keys()):
            writer.writerow(['jobcat.' + key, jobcat_cnt_dict[key]])
