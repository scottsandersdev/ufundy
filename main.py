#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import webapp2

from webapp2_extras import routes

from ufundy.public import public_handlers

DEBUG = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')

webapp2_config = {}
webapp2_config['webapp2_extras.sessions'] = {
    'secret_key': '3SWyTjcrNsR2CUjpsyyv',
}

app = webapp2.WSGIApplication([
    webapp2.Route(r'/', handler=public_handlers.HomeHandler, name='home'),
    webapp2.Route(r'/contact_submit', handler=public_handlers.ContactSubmitHandler, name='contact_submit'),
    webapp2.Route(r'/waiting_list_submit', handler=public_handlers.WaitingListSubmitHandler, name='waiting_list_submit'),
    ],
    config=webapp2_config, debug=DEBUG)









