#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

import demjson
import openam
import requests

START_URL = 'https://ess.liantis.be/'
MIJNPRESTATIES_URL = START_URL + 'MijnPrestaties/'
MIJNKALENDER_URL = START_URL + 'mijnkalender/'


class MijnPrestaties:

    def __init__(self):
        self.session = requests.Session()

    def login(self, login, password):
        am = openam.Openam(
            openam_url='https://login.liantis.be/idp/json/authenticate?realm=/liantis&forward'
                       '=true&spEntityID=undefined')
        x = am.authenticate(username=login, password=password)
        self.session.cookies.set('iPlanetDirectoryPro', x['tokenId'])
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'iPlanetDirectoryPro': x['tokenId']
        }
        # return the open session object for future handling
        # TODO implement returning error if login fails
        return self.session.get(MIJNPRESTATIES_URL, headers=headers)

    def get_employee_id(self):
        html = self.session.get(MIJNPRESTATIES_URL).text
        regex = '(?<=var mdwID = )[^;]+'
        match = re.findall(regex, html)
        return_id = demjson.decode(match[0])
        return str(return_id)

    def get_api_version(self):
        html = self.session.get(MIJNPRESTATIES_URL).text
        regex = '(?<=var apiVersion = \')[^\';]+'
        match = re.findall(regex, html)
        return_id = demjson.decode(match[0])
        return str(return_id)

    def get_todays_logs(self, employee_id):
        """
        :param employee_id: Required: ID of the employee
        :return: List containing dictionary objects with log information for today.
        """
        todays_logs = self.session.get(
            MIJNPRESTATIES_URL + 'api/TijdLog/GetTijdLogsVanMedewerker/' + employee_id)
        # Convert the javascript object to Python object
        return demjson.decode(todays_logs.text)

    def get_time_to_work(self):
        """
        :return: Dictionary containing information about the hours to work for today.
        """
        time_to_work = self.session.get(
            MIJNPRESTATIES_URL + 'api/TijdLog/GetTimeToWork/')
        return demjson.decode(time_to_work.text)

    def get_organisation_counter_settings(self, employee_id):
        """
        :param employee_id: Required: ID of the employee
        :return: Dictionary containing information about the settings for the timer.
        """
        counter_settings = self.session.get(
            MIJNPRESTATIES_URL + 'api/TijdLog/orgCon_counterSettings?mdwid=' + employee_id)
        # Convert the javascript object to Python object
        return demjson.decode(counter_settings.text)

    def get_is_location_mandatory(self, employee_id, api_version):
        """
        :param employee_id: Required: ID of the employee
        :param api_version: Required: Version number of the API
        :return: Dictionary containing information about location setting
        """
        is_location_mandatory = self.session.get(
            MIJNPRESTATIES_URL + 'api/TijdLog/GetIsLocatieVerplicht/?id=' + employee_id +
            '&apiVersie=' + api_version)
        # Convert the javascript object to Python object
        return demjson.decode(is_location_mandatory.text)


class MijnKalender:
    def __init__(self):
        self.session = requests.Session()
