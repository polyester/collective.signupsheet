��    3      �      L      L     M     U     ^     o  $   t     �     �     �     �  	   �     �     �       
        *     F     Z     v     �     �      �     �     �     �     �  %        4     C     Y     l     x  	   �     �     �     �     �     �       &   )     P  '   n     �     �     �  	   �     �     �     �     
     !  �  2     �     �     �     	  )   	     I	     a	  	   x	     �	  
   �	     �	     �	     �	     �	     �	      �	  C   
  *   c
     �
     �
  1   �
     �
  /   �
            R   !     t     �     �     �     �     �  
   �     �     �       	          
   #     .     4     C     K    R  
   p     {  a   �     �             Confirm Download Early bird until Edit Please correct the indicated errors. Registration deadline The registration is closed colon comma confirmed field_display_size_left field_early_bird_phase field_eventsize field_name field_registration_deadline field_waitlist_size fieldhelp_display_size_left fieldhelp_eventsize heading_action heading_created heading_import_contacts_step_one heading_review_state help_body_text label_body_text label_delimiter mailer_registration_subject_overrides no registrants pfg_registrants_title pfg_thankyou_title registrants seats_left_message semicolon sign_up sign_up_for_waitinglist signupsheet_emailfield_title signupsheet_formfolder_reset signupsheet_formfolder_signup signupsheet_namefield_title signupsheet_statusfield_registered_opt signupsheet_statusfield_title signupsheet_statusfield_waitinglist_opt signupsheet_surnamefield_title space subscribtion_mail tabulator text_registration_full thanks_prologue unconfirmed view_export_registrant view_registrants Project-Id-Version: 1
POT-Creation-Date: 2013-01-18 14:00+0000
PO-Revision-Date: 2013-01-16 13:45 +ZONE
Last-Translator: Luca Bellenghi luica.bellenghi@redturtle.it
Language-Team: ITALIAN sviluppo@redturtle.it
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=1; plural=0
Language-Code: it
Language-Name: Italian
Preferred-Encodings: utf-8 latin1
Domain: collective.signupsheet
 Conferma Download Iscrizioni scontate fino al Edit Per favore correggere gli errori indicati Scadenza dell'scrizione L'iscrizione è chiusa Due punti Virgola confermati Visualizza posti rimanenti Iscrizioni scontate fino al Numero di iscritti Campo Scadenza dell'iscrizione Dimensione della lista di attesa Scegli se visualizzare nella pagina di iscrizione i posti rimanenti Impostare a 0 per un'iscrizione illimitata Azione Creato Seleziona i campi da esportare e scaricare in csv Stato Testo per la pagina principale dell'iscrizione. Corpo del testo Delimitatore string:La tua registrazione per ${here/aq_inner/aq_parent/Title} è stata ricevuta Nessuna registrazione Iscritti Grazie! Iscritti ${seats} posti rimanenti. Punto e virgola Iscriviti! Iscriviti in lista di attesa Il tuo indirizzo e-mail Reset Iscriviti Nome Registrato Stato Lista d'attesa Cognome Spazio <html xmlns='http://www.w3.org/1999/xhtml'>

<head><title></title></head>

<body>
<p tal:content='here/getBody_pre |nothing' />
Grazie per essersi registrato a<tal:title tal:replace='here/aq_inner/aq_parent/Title'/>
<dl>
<tal:block repeat='field options/wrappedFields | nothing'>
<dt tal:content='field/fgField/widget/label' />
<dd tal:content='structure python:field.htmlValue(request)' />
</tal:block>
</dl>
<p tal:content='here/getBody_post | nothing' />
<pre tal:content='here/getBody_footer | nothing' />
</body>
</html> Tabulatore L'iscrizione è chiusa La ringraziamo per la registrazione, verrà contattato a breve. <br/>
Ha fornito i seguenti dati: non confermato Esporta i dati Vedi gli iscritti 