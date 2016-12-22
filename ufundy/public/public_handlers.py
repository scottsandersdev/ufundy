import webapp2
import logging

from ufundy import basehandler

import public_forms as forms

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')


class HomeHandler(basehandler.BaseHandler):
    def get(self):
        page_title = 'uFundy - Portal'
        page_description = 'uFundy - Portal'

        context = {'page_title': page_title,
                    'page_description': page_description,
                    'form_contact': self.form_contact,
                    'form_waiting': self.form_waiting,
                    'waiting_action': webapp2.uri_for('waiting_list_submit', _full=True),
                    'contact_action': webapp2.uri_for('contact_submit', _full=True),
                   }

        self.render_response('public/splash.html', **context)

    @webapp2.cached_property
    def form_contact(self):
        try:
            return forms.ContactuFundyForm(self.request.POST)
        except Exception, e:
            logging.error('_uFundy Error - blah %s' % str(e))
            self.abort(403)

    @webapp2.cached_property
    def form_waiting(self):
        try:
            return forms.WaitingListForm(self.request.POST)
        except Exception, e:
            logging.error('_uFundy Error - blah %s' % str(e))
            self.abort(403)


class WaitingListSubmitHandler(basehandler.BaseHandler):
    def post(self):
        if self.form.validate():
            email = self.form.email.data

            added = True

            if added:

                complete = True
                if not complete:
                    self.add_message(u'whoops')
            else:
                self.add_message(u'error')

        for field, errors in self.form.errors.items():
            for error in errors:
                self.add_message(u'Error')

        self.redirect(webapp2.uri_for('home', _full=True))

    @webapp2.cached_property
    def form(self):
        try:
            return forms.WaitingListForm(self.request.POST)
        except Exception, e:
            logging.error('error')
            self.abort(403)


class ContactSubmitHandler(basehandler.BaseHandler):
    def post(self):
        if self.form.validate():
            name = self.form.name.data
            city = self.form.city.data
            email = self.form.email.data
            message = self.form.message.data

            complete = True
            if not complete:
                    self.add_message(u"whoops", "error")

        for field, errors in self.form.errors.items():
            for error in errors:
                self.add_message(u"Error in field", "error")

        self.redirect(webapp2.uri_for('home', _full=True))

    @webapp2.cached_property
    def form(self):
        try:
            return forms.ContactuFundyForm(self.request.POST)
        except Exception, e:
            logging.error('error')
            self.abort(403)



