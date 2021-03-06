# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import (IntegerField, StringWidget,
                                       BooleanField, BooleanWidget,
                                       DateTimeField, CalendarWidget,
                                       TextField, RichWidget, TextAreaWidget, StringField, LinesField, LinesWidget, MultiSelectionWidget,
                                       Schema)
from Products.ATContentTypes.content.base import registerATCT
from Products.ATContentTypes.content.folder import ATFolder
from Products.CMFCore.permissions import ModifyPortalContent
from Products.CMFCore.utils import getToolByName
from Products.PloneFormGen.content.form import (FormFolder,
                                                FormFolderSchema)
from Products.ATContentTypes import ATCTMessageFactory as _E

from zope.interface import implements
from zope.component import getMultiAdapter

from collective.signupsheet import signupsheetMessageFactory as _
from collective.signupsheet.config import PROJECTNAME, logger
from collective.signupsheet.interfaces import ISignupSheet
from collective.signupsheet.interfaces import ISignupSheetInitializer


SignupSheetSchema = FormFolderSchema.copy() + Schema((
    IntegerField('eventsize',
        required=1,
        default=0,
        read_permission="SignupSheet: View Registration Info",
        validators=('isInt',),
        widget=StringWidget(
            visible={'edit': 'visible', 'view': 'invisible'},
            size=6,
            label=_('field_eventsize',
                    default=u'Number of registrants'),
            description=_('fieldhelp_eventsize',
                          default=u"Set to 0 for unlimited registration",)
             )
       ),
    IntegerField('waitlist_size',
        required=1,
        default=0,
        read_permission="SignupSheet: View Registration Info",
        validators=('isInt',),
        widget=StringWidget(
            visible={'edit': 'visible', 'view': 'invisible'},
            size=6,
            label=_('field_waitlist_size',
                    default=u'Size of wait list',),
            )
        ),
    BooleanField('display_size_left',
        default=False,
        widget=BooleanWidget(
            visible={'edit': 'visible', 'view': 'invisible'},
            label=_('field_display_size_left', default=u'Display seats left'),
            description=_('fieldhelp_display_size_left',
                          default=u"Choose to show in the subscription page the number of seats left",)
            )
        ),
    LinesField('speakers',
        searchable=True,
        widget=LinesWidget(
            label=_('field_speakers', default=u'Input people'),
            description=_('fieldhelp_speakers',
                          default=u"The input people; one per line",)
            )
        ),
    StringField('facilitator',
        searchable=True,
        widget=StringWidget(
            label=_('field_facilitator', default=u'Facilitator'),
            description=_('fieldhelp_facilitator',
                          default=u"The facilitator",)
            )
        ),
    StringField('organizer',
        searchable=True,
        widget=StringWidget(
            label=_('field_organizer', default=u'Organizer'),
            description=_('fieldhelp_organizer',
                          default=u"The organizer",)
            )
        ),
    LinesField('theme',
        searchable=True,
        widget=MultiSelectionWidget(
            label=_('field_theme', default=u'Theme'),
            description=_('fieldhelp_theme',
                          default=u"Theme",),
            format='checkbox',

            ),
        multivalued=1,
        vocabulary=['Wages','Employment relationships','Worker safety','Future structure']
        ),
    LinesField('cross_cutting_issue',
        searchable=True,
        widget=MultiSelectionWidget(
            label=_('field_cross_cutting_issue', default=u'Cross cutting issue'),
            description=_('fieldhelp_cross_cutting_issue',
                          default=u"Cross cutting issue",),
            format='checkbox',

            ),
        multivalued=1,
        vocabulary=['Gender','Freedom of Association','Global Bargaining','Migrants']
        ),
    LinesField('workshop_type',
        searchable=True,
        widget=MultiSelectionWidget(
            label=_('field_workshop_type', default=u'Workshop Type'),
            description=_('fieldhelp_workshop_type',
                          default=u"Workshop Type",),
            format='checkbox',

            ),
        multivalued=1,
        vocabulary=['Plenary','Topical','Regional','Social','Side meeting']
        ),

    DateTimeField('startDate',
        required=False,
        searchable=False,
        accessor='start',
        write_permission=ModifyPortalContent,
        languageIndependent=True,
        widget=CalendarWidget(
            description='',
            label=_E(u'label_event_start', default=u'Event Starts')
            )
        ),
    DateTimeField('endDate',
        required=False,
        searchable=False,
        accessor='end',
        write_permission=ModifyPortalContent,
        languageIndependent=True,
        widget=CalendarWidget(
            description='',
            label=_E(u'label_event_end', default=u'Event Ends')
            )
        ),
    DateTimeField('earlyBirdDate',
        required=0,
        default=None,
        read_permission="View",
        widget=CalendarWidget(
            label=_('field_early_bird_phase', default=u"Early bird phase until"),
            visible={'edit': 'visible', 'view': 'invisible'},
            size=6,
            )
        ),
    DateTimeField('registrationDeadline',
        required=0,
        default=None,
        read_permission="View",
        widget=CalendarWidget(
            label=_('field_registration_deadline',
                    default=u'Registration deadline'),
            description=_("fieldhelp_registration_deadline",
                          default=u"Registrations will be stopped after this date"),
            visible={'edit': 'visible', 'view': 'invisible'},
            size=6,
            )
        ),
    TextField('text',
        accessor='getBodyText',
        required=True,
        searchable=True,
        primary=True,
        validators=('isTidyHtmlWithCleanup',),
        default_content_type='text/html',
        default_output_type='text/x-html-safe',
        allowable_content_types=('text/html',
                                 'text/plain',),
        widget=RichWidget(
            label=_("label_body_text", default=u"Body Text"),
            description=_("help_body_text",
                          default=u"Text for front page of signup",),
            rows=25,
           ),
        ),
))

SignupSheetSchema.moveField('speakers', after='description')
SignupSheetSchema.moveField('facilitator', after='speakers')
SignupSheetSchema.moveField('organizer', after='facilitator')
SignupSheetSchema.moveField('theme', after='organizer')
SignupSheetSchema.moveField('cross_cutting_issue', after='theme')
SignupSheetSchema.moveField('workshop_type', after='cross_cutting_issue')
SignupSheetSchema.moveField('eventsize', after='workshop_type')
SignupSheetSchema.moveField('waitlist_size', after='eventsize')
SignupSheetSchema.moveField('display_size_left', after='waitlist_size')
SignupSheetSchema.moveField('startDate', after='display_size_left')
SignupSheetSchema.moveField('endDate', after='startDate')
SignupSheetSchema.moveField('earlyBirdDate', after='endDate')
SignupSheetSchema.moveField('registrationDeadline', after='earlyBirdDate')
SignupSheetSchema.moveField('text', after='registrationDeadline')


class SignupSheet(FormFolder):
    implements(ISignupSheet)

    schema = SignupSheetSchema

    def initializeArchetype(self, **kwargs):
        """ Create initial SignupSheet configuration
        """
        ATFolder.initializeArchetype(self, **kwargs)
        pm = getToolByName(self, 'portal_membership')
        portal_factory = getToolByName(self, 'portal_factory')
        if not pm.isAnonymousUser() and not portal_factory.isTemporary(self):
            ISignupSheetInitializer(self).form_initializer(**kwargs)
        else:
            logger.debug("Anonymous user: not allowed to create fields")

    def no_seat_left(self):
        """
        use this method to provide a some like a validation when we have two user
        that are both trying to subscribe the form
        """
        base_view = getMultiAdapter((self, self.REQUEST),
                                     name='susbase_utiltities_view')
        left = base_view.getSeatsLeft()
        if self.getEventsize() and left <= 0:
            return True
        return False

registerATCT(SignupSheet, PROJECTNAME)
