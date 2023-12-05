*** Settings ***
Library  main.py

*** Test Cases ***
limit max
    [Documentation]
    ...
    ${limit}=  get_characters
    Should Be Equal  ${limit}  ${826}


