#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Teus Jan 21 23:34:00 2025

@Author: Caleb Kilonzi
"""
import sys


status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # keep count of the number lines counted

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            if status_code in status_codes_dict.keys():
                status_codes_dict[status_code] += 1

            total_size += file_size

            count += 1

        if count == 10:
            count = 0
            print('File size: {}'.format(total_size))

            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as error:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
