# -*- coding: utf-8 -*-
from collective.signupsheet.config import (INITIAL_MAIL,
                                           INITIAL_MAIL_MESSAGE,
                                           MANAGER_MAIL,
                                           MANAGER_MAIL_MESSAGE)
from collective.signupsheet.tests.base import FunctionalTestCase


class TestForm(FunctionalTestCase):
    """
    Use this test class to test SignupSheet form configuration
    """

    def afterSetUp(self):
        FunctionalTestCase.afterSetUp(self)
        self.setRoles(['Manager', ])
        self.create = self.portal.invokeFactory
        self.newid = self.create(type_name='SignupSheet', id='a-new-form')
        self.form = getattr(self.portal, self.newid)

    def test_create_form_folder(self):
        self.failUnless('a-new-form' in self.portal.objectIds())

    def test_set_default_page(self):
        self.assertEqual(self.form.canSetDefaultPage(), False)

    def test_form_setup_labels(self):
        signup = self.form.getSubmitLabel()
        reset = self.form.getResetLabel()
        self.assertEqual('Sign up', signup)
        self.assertEqual('Reset', reset)

    def test_name_field(self):
        self.failUnless(hasattr(self.form, 'name'))
        name = getattr(self.form, 'name')
        self.assertEqual(u'Your Name',
                            name.Title())
        self.assertNotEqual('here/@@default_name_value',
                            name.getFgTDefault())

    def test_surname_field(self):
        self.failUnless(hasattr(self.form, 'surname'))
        surname = getattr(self.form, 'surname')
        self.assertEqual(u'Your surname',
                            surname.Title())
        self.assertNotEqual('here/@@default_surname_value',
                            surname.getFgTDefault())

    def test_ssfg_status_field(self):
        self.failUnless(hasattr(self.form, 'ssfg_status'))
        status = getattr(self.form, 'ssfg_status')
        self.assertEqual(u'Status',
                            status.Title())
        self.assertEqual(('registered|Registered',
                             'waitinglist|Waiting list'),
                            status.getFgVocabulary())
        self.assertEqual('radio',
                            status.getFgFormat())
        self.assertEqual('here/@@check_state_field_is_visible',
                            status.fgTEnabled.text)

    def test_email_field(self):
        self.failUnless(hasattr(self.form, 'email'))
        email = getattr(self.form, 'email')
        self.assertEqual(u'E-Mail Address',
                            email.Title())
        self.assertEqual(True,
                        email.fgField.required)
        self.assertEqual('isEmail',
                             email.getFgStringValidator())
        self.assertEqual('here/@@default_email_value',
                         email.fgTDefault.text)

    def test_registrant_adapter(self):
        self.failUnless(hasattr(self.form, 'registrants'))
        registrant = getattr(self.form, 'registrants')
        self.assertEqual('Registrants',
                             registrant.Title())
        self.assertEqual('registrant',
                            registrant.getEntryType())
        self.assertEqual('email',
                            registrant.getTitleField())
        self.assertEqual(True,
                            registrant.getNiceIds())
        self.assertEqual(u'here/@@set_registrant_title',
                         registrant.dynamicTitle.text)

    def test_user_notification_mailer_adapter(self):
        self.failUnless(hasattr(self.form, 'user_notification_mailer'))
        mailer = getattr(self.form, 'user_notification_mailer')
        self.assertEqual(u'User notification mailer ',
                         mailer.Title())
        self.assertEqual(False,
                            mailer.getIncludeEmpties())
        self.assertEqual(u'E-Mails Form Input for subscribers',
                            mailer.Description())
        self.assertEqual('email',
                            mailer.getReplyto_field())
        self.assertEqual('here/@@user_mailer_subject',
                            mailer.subjectOverride.text)
        self.assertTrue("\nThank you for registering to" in mailer.getBody_pt())

    def test_manager_notification_mailer_adapter(self):
        self.failUnless(hasattr(self.form, 'manager_notification_mailer'))
        mailer = getattr(self.form, 'manager_notification_mailer')
        self.assertEqual(u'Manager notification mailer',
                             mailer.Title())
        self.assertEqual(False,
                            mailer.getIncludeEmpties())
        self.assertEqual(u'E-Mails Form Input for signup sheet editors: this mailer send notifications to signupsheet managers',
                            mailer.Description())
        self.assertEqual('#NONE#',
                            mailer.getReplyto_field(),)
        self.assertEqual('here/@@manager_mailer_subject',
                            mailer.subjectOverride.text)
        self.assertTrue("\nNew registrant registered for" in mailer.getBody_pt())

    def test_thankyou_page(self):
        self.failUnless(hasattr(self.form, 'thank-you'))
        thx = getattr(self.form, 'thank-you')
        self.assertEqual(u'Thank You',
                         thx.Title())
        self.assertEqual(False,
                            thx.getIncludeEmpties())
        self.assertEqual("Thank you for registering, we will contact you shortly. <br/>\nYou provided the following information:",
                        thx.getThanksPrologue())

    def test_actions(self):
        self.assertTrue('registrants' in self.form.actionAdapter)
        self.assertTrue('user_notification_mailer' in self.form.actionAdapter)
        self.assertTrue('manager_notification_mailer' in self.form.actionAdapter)
        self.assertEqual(self.form.thanksPage, 'thank-you')