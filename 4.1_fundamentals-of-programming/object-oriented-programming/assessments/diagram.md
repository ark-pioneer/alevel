@startuml
' Legend:
' + public    (no leading underscore in Python)
' # protected (single leading underscore)
' - private   (double leading underscore; name-mangled

classDiagram
    class SMS {
        #to
        #from
        #body
        +__init__(to, from, body)
        +send()
        -__format_message()
    }

    class Email {
        #_to
        #_from
        #_body
        #_cc
        #_bcc
        +__init__(to, from, body, cc, bcc)
        +send()
        -__format_message()
