#!/usr/bin/python
#   Copyright 2012-2013 STACKOPS TECHNOLOGIES S.L.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import imp
import json
import os

import providers

import yaml


class Component(object):

    services = {}
    methods = {}
    module = None

    """Parses component files and extracts its data"""
    def __init__(self, comp_dir):
        self._comp_dir = comp_dir
        self._config_path = os.path.join(comp_dir, 'component.yml')
        self.provider = providers.FabricProvider()
        with open(self._config_path) as f:
            self._config = yaml.load(f.read())

        self._check_component_coherency()
        self._load_methods()
        self._load_services()
        self._load_module()
        self._set_attributes()

    def set_environment(self, env):
        self.provider.set_environment(env)

    @property
    def name(self):
        return self._config['name']

    @property
    def path(self):
        return os.path.join(self._comp_dir, self._config['file'])

    def _set_attributes(self):
        for service, tup in self.services.items():
            description, methods = tup
            setattr(self, service, self._execute_service(service))

    def __repr__(self):
        return json.dumps(self._config, indent=4)

    def _load_methods(self):
        self.methods = {}
        for method in self._config['Methods']:
            method_name = method['name']
            desc = method['description']
            list_params = []
            if 'params' in method:
                for param in method['params']:
                    list_params.append((param['name'], param['description']))

            self.methods[method_name] = (desc, list_params)

    def _load_services(self):
        self.services = {}
        for service in self._config['Services']:
            name = service['name']
            list_methods = []
            description = ''
            for method in service['methods']:
                list_methods.append(method)
                description += self.methods[method][0] + '\n'
            self.services[name] = (description, list_methods)

    def _load_module(self):
        self.module = imp.load_source(self.name, self.path)

    def _check_component_coherency(self):
        """ Checks if the component has coherency.

        According with the fabuloso doc [todo link here], this method
        checks if the component has coherency.
        """
        pass

    def _execute_service(self, service_name):
        def wrapper_method(**kwargs):
            description, methods = self.services[service_name]
            for method in methods:
                service_args = self._build_args(method, kwargs)
                self.provider.execute_method(getattr(self.module, method),
                                             **service_args)

        return wrapper_method

    def _build_args(self, method, kwargs):
        """ Build appropiate args depending on the method

        The execute service receives a list of arguments that may be
        useful for one or more methods. This function filters only
        the ones that are needed for the current 'method'
        """
        method_args = {}
        parameters = self.methods[method][1]
        for parameter in parameters:
            param_name, description = parameter
            if param_name in kwargs:
                method_args[param_name] = kwargs[param_name]
        return method_args
